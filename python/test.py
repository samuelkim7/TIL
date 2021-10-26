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

# defining dilation mask to apply dilation 
dilation_mask = np.zeros((height, width), dtype='bool')
border_area = 0.03
border_height = round(height * border_area)

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
closing_ref = np.ones((2,round(width * 0.3),1), dtype=int)

index = 0
while True:
  hasFrame, img_frame = cap.read()
  if not hasFrame:
    print('no more frame to be processed')
    break
  
  # segment and change by deeplabv3
  # output_deeplab = change_bg.change_frame_bg(img_frame, bg_path)
  
  # segment and change by pointrend 
  result = ins.segmentFrame(img_frame.copy(), segment_target_classes=target_classes)
  person_mask = result[0]['masks'][:, :, 0]
  person_mask = np.expand_dims(person_mask, axis=-1)
  
  # applying closing and dilation
  person_mask_clos = ndimage.binary_closing(person_mask, 
                                           iterations=1,
                                           structure=closing_ref)
  
  person_mask_dil = ndimage.binary_dilation(person_mask_clos,
                                            iterations=2,
                                            mask=dilation_mask)

  output_pr = np.where(person_mask, img_frame, bg_img_resized)
  output_pr_cvt = cv2.cvtColor(output_pr, cv2.COLOR_BGR2RGB)
  fig = plt.figure(figsize=(30, 20))
  ax1 = fig.add_subplot(1, 3, 1)
  ax1.imshow(output_pr_cvt)

  output_pr_dil = np.where(person_mask_dil, img_frame, bg_img_resized)
  output_pr_dil_cvt = cv2.cvtColor(output_pr_dil, cv2.COLOR_BGR2RGB)
  ax1 = fig.add_subplot(1, 3, 2)
  ax1.imshow(output_pr_dil_cvt)

  # combine the two results
  # final_output = np.where(person_mask, output_pr, output_deeplab)
  # final_output = cv2.cvtColor(final_output, cv2.COLOR_BGR2RGB)
  # ax2 = fig.add_subplot(1, 3, 3)
  # ax2.imshow(final_output)
  break

  writer.write(output_pr)

  index += 1
  if index % 20 == 0:
    print('{}th output frame processed'.format(index))

print('video writing done!!')
writer.release()
cap.release()
