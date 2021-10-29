import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from pixellib.tune_bg import alter_bg
from pixellib.torchbackend.instance import instanceSegmentation


ins = instanceSegmentation()
ins.load_model("checkpoints/pointrend_resnet50.pkl")

input_path = 'imgs/charlie_video.mp4'
output_path = 'results/summer2winter/charlie_summer_pr.mp4'

cap = cv2.VideoCapture(input_path)

codec = cv2.VideoWriter_fourcc(*'XVID')
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
vid_size = (width, height)
vid_fps = cap.get(cv2.CAP_PROP_FPS)
writer = cv2.VideoWriter(output_path, codec, vid_fps, vid_size)

frame_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print('Number of frame: {} / FPS: {} / Frame size: {}' \
      .format(frame_cnt, round(vid_fps), vid_size))

# defining closing structure and dilation mask 
closing_ref = np.ones((2,round(width * 0.3),1), dtype='bool')

dilation_mask = np.zeros((height, width), dtype='bool')
border_height = round(height * 0.03)
dilation_mask[:border_height, :] = True
dilation_mask[height-border_height:, :] = True
dilation_mask = np.expand_dims(dilation_mask, axis=-1)

# generating the output video with segmentation
bg_path = 'imgs/summer/sample_summer.png'
bg_img = cv2.imread(bg_path)
target_classes = {
    'person': 'valid',
    'tie': 'invalid'
}
bg_img_resized = cv2.resize(bg_img, (width, height))


index = 0
while True:
  hasFrame, img_frame = cap.read()
  if not hasFrame:
    print('no more frame to be processed')
    break
  
  # segment by PointRend 
  result = ins.segmentFrame(img_frame.copy(), segment_target_classes=target_classes)
  person_mask = result[0]['masks'][:, :, 0]
  person_mask = np.expand_dims(person_mask, axis=-1)
  
  # closing and dilation
  person_mask_clos = ndimage.binary_closing(person_mask, 
                                           iterations=1,
                                           structure=closing_ref)
  
  person_mask_dil = ndimage.binary_dilation(person_mask_clos,
                                            iterations=2,
                                            mask=dilation_mask)

  output_dil = np.where(person_mask_dil, img_frame, bg_img_resized)
  writer.write(output_pr)

  index += 1
  if index % 20 == 0:
    print('{}th output frame processed'.format(index))

print('video writing done!!')
writer.release()
cap.release()


img = Image.fromarray(img_array).convert('RGB')
img = transform(img)
img = img.unsqueeze(0)

data = {'A': img, 'A_paths': None}
model.set_input(data)
model.test()

img_output = model.get_current_visuals()['fake']
img_output = util.tensor2im(img_output)
img_output = Image.fromarray(img_output).convert('RGB')
output_path = 'gan_output.jpg'
img_output.save(output_path)


def get_uncertain_point_coords_with_randomness(
    coarse_logits, uncertainty_func, num_points, oversample_ratio, importance_sample_ratio
):
      """
      Sample points in [0, 1] x [0, 1] coordinate space based on their uncertainty. The unceratinties
        are calculated for each point using 'uncertainty_func' function that takes point's logit
        prediction as input.
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
