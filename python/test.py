# import the needed packages
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow
from scipy import ndimage
import torch
import torchvision

import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer, ColorMode
from detectron2.data import MetadataCatalog
coco_metadata = MetadataCatalog.get("coco_2017_val")

# import PointRend project
from detectron2.projects import point_rend

# get the pretrained model
config_R50 = "projects/PointRend/configs/InstanceSegmentation/pointrend_rcnn_R_50_FPN_3x_coco.yaml"
config_R101 = "projects/PointRend/configs/InstanceSegmentation/pointrend_rcnn_R_101_FPN_3x_coco.yaml"
config_X101 = "projects/PointRend/configs/InstanceSegmentation/pointrend_rcnn_X_101_32x8d_FPN_3x_coco.yaml"
weights_R50 = "detectron2://PointRend/InstanceSegmentation/pointrend_rcnn_R_50_FPN_3x_coco/164955410/model_final_edd263.pkl"
weights_R101 = "detectron2://PointRend/InstanceSegmentation/pointrend_rcnn_R_101_FPN_3x_coco/28119983/model_final_3f4d2a.pkl"
weights_X101 = "detectron2://PointRend/InstanceSegmentation/pointrend_rcnn_X_101_32x8d_FPN_3x_coco/28119989/model_final_ba17b9.pkl"

cfg = get_cfg()
point_rend.add_pointrend_config(cfg)
cfg.merge_from_file(config_R101)
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
cfg.MODEL.WEIGHTS = weights_R101
predictor = DefaultPredictor(cfg)


def get_void_from_mask(person_mask_closed, height, 
                       void_cri_top, void_cri_bottom):
    top_void = 0
    bottom_void = 0

    for h_count in range(height):
        line_mask_int = person_mask_clos[h_count, :, 0].astype(int)

        if h_count < height * 0.5:
            if np.sum(line_mask_int) <= void_cri_top:
                top_void += 1
        else:
            if np.sum(line_mask_int) <= void_cri_bottom:
                bottom_void += 1

    return top_void, bottom_void


def get_dilation_mask(height, width
                      void_top, void_bottom,  
                      padding_top, padding_bottom):
dilation_mask_top = np.zeros((height, width, 1), dtype='bool')
dilation_mask_bottom = np.zeros((height, width, 1), dtype='bool')

dilation_mask_top[:top_void+padding_top, :, 0] = True
dilation_mask_bottom[height-(bottom_void+padding_bottom):, :, 0] = True

return dilation_mask_top, dilation_mask_bottom


bg_path = 'imgs/summer/sample_summer.png'
bg_img = cv2.imread(bg_path)
bg_img_resized = cv2.resize(bg_img, (width, height))

# default setting for closing and dilation
closing_str = np.ones((3,round(width * 0.3),1), dtype=int)

void_cri_top = 40
void_cri_bottom = 60
padding_top = 2
padding_bottom = 2

index = 0
while True:
    hasFrame, img_frame = cap.read()
    if not hasFrame:
        print('no more frame to be processed')

    # get the segmentation mask
    output = predictor(img_frame)
    person_mask = output['instances'].pred_masks[0, :, :].detach().cpu().numpy()
    person_mask = np.expand_dims(person_mask, axis=-1)

    # apply closing
    person_mask_closed = ndimage.binary_closing(person_mask, 
                                                iterations=1,
                                                structure=closing_str)
    
    # apply dilation
    void_top, void_bottom = get_void_from_mask(person_mask_closed, height,
                                               void_cri_top, void_cri_bottom)

    d_mask_top, d_mask_bottom = get_dilation_mask(height, width,
                                                  void_top, void_bottom, 
                                                  padding_top, padding_bottom)
    
    
    person_mask_dilated = ndimage.binary_dilation(person_mask_closed,
                                                  iterations=void_top+padding_top,
                                                  mask=d_mask_top)

    person_mask_dilated = ndimage.binary_dilation(person_mask_dilated,
                                                  iterations=void_bottom+padding_bottom,
                                                  mask=d_mask_bottom)

    # change the background based on the mask
    frame_bg_changed = np.where(person_mask_dilated, img_frame, bg_img_resized)

    writer.write(frame_bg_changed)

    index += 1
    if index % 20 == 0:
        print('{}th output frame processed'.format(index))

print('video writing done!!')
writer.release()
cap.release()


def get_uncertain_point_coords_with_randomness(
      coarse_logits, uncertainty_func, num_points, oversample_ratio, importance_sample_ratio
):
      """
      Sample points in [0, 1] x [0, 1] coordinate space based on their uncertainty. 
      The unceratinties are calculated for each point using 'uncertainty_func' function 
      that takes point's logit prediction as input.
      """
      assert oversample_ratio >= 1
      assert importance_sample_ratio <= 1 and importance_sample_ratio >= 0
      num_boxes = coarse_logits.shape[0]
      num_sampled = int(num_points * oversample_ratio)
      point_coords = torch.rand(num_boxes, num_sampled, 2, device=coarse_logits.device)
      
      point_logits = point_sample(coarse_logits, point_coords, align_corners=False)
      
      point_uncertainties = uncertainty_func(point_logits)
      
      num_uncertain_points = int(importance_sample_ratio * num_points)
      num_random_points = num_points - num_uncertain_points
      idx = torch.topk(point_uncertainties[:, 0, :], k=num_uncertain_points, dim=1)[1]
      shift = num_sampled * torch.arange(num_boxes, dtype=torch.long, device=coarse_logits.device)
      idx += shift[:, None]
      point_coords = point_coords.view(-1, 2)[idx.view(-1), :].view(
        num_boxes, num_uncertain_points, 2
      )
      if num_random_points > 0:
            point_coords = cat(
                  [
                        point_coords,
                        torch.rand(num_boxes, num_random_points, 2, device=coarse_logits.device),
                  ],
                  dim=1,
            )
      return point_coords





class StandardPointHead(nn.Module):
    """
    A point head multi-layer perceptron which we model with conv1d layers with kernel 1. The head
    takes both fine-grained and coarse prediction features as its input.
    """

    def __init__(self, cfg, input_shape: ShapeSpec):
        super(StandardPointHead, self).__init__()
        # fmt: off
        num_classes                 = cfg.MODEL.POINT_HEAD.NUM_CLASSES
        fc_dim                      = cfg.MODEL.POINT_HEAD.FC_DIM
        num_fc                      = cfg.MODEL.POINT_HEAD.NUM_FC
        cls_agnostic_mask           = cfg.MODEL.POINT_HEAD.CLS_AGNOSTIC_MASK
        self.coarse_pred_each_layer = cfg.MODEL.POINT_HEAD.COARSE_PRED_EACH_LAYER
        input_channels              = input_shape.channels
        # fmt: on

        fc_dim_in = input_channels + num_classes
        self.fc_layers = []
        for k in range(num_fc):
            fc = nn.Conv1d(fc_dim_in, fc_dim, kernel_size=1, stride=1, padding=0, bias=True)
            self.add_module("fc{}".format(k + 1), fc)
            self.fc_layers.append(fc)
            fc_dim_in = fc_dim
            fc_dim_in += num_classes if self.coarse_pred_each_layer else 0

        num_mask_classes = 1 if cls_agnostic_mask else num_classes
        self.predictor = nn.Conv1d(fc_dim_in, num_mask_classes, kernel_size=1, stride=1, padding=0)

        for layer in self.fc_layers:
            weight_init.c2_msra_fill(layer)
        # use normal distribution initialization for mask prediction layer
        nn.init.normal_(self.predictor.weight, std=0.001)
        if self.predictor.bias is not None:
            nn.init.constant_(self.predictor.bias, 0)

    def forward(self, fine_grained_features, coarse_features):
        x = torch.cat((fine_grained_features, coarse_features), dim=1)
        for layer in self.fc_layers:
            x = F.relu(layer(x))
            if self.coarse_pred_each_layer:
                x = cat((x, coarse_features), dim=1)
        return self.predictor(x)
