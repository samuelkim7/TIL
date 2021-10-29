import cv2
import numpy as np
from PIL import Image

from options.test_options import TestOptions
from data import create_dataset
from data.base_dataset import get_transform
from util import util
from models import create_model


opt = TestOptions().parse()
opt.num_threads = 0   
opt.batch_size = 1    
opt.serial_batches = True  
opt.no_flip = True    
opt.display_id = -1   
model = create_model(opt)
model.setup(opt)

if opt.eval:
    model.eval()

input_nc = opt.output_nc if opt.direction == 'BtoA' else opt.input_nc
transform = get_transform(opt, grayscale=(input_nc == 1))


index = 0
while True:
    hasFrame, img_frame = cap.read()
    if not hasFrame:
        print('no more frame to be processed')
        break
        
    # transform the image frame
    img = Image.fromarray(img_frame).convert('RGB')
    img = transform(img)
    img = img.unsqueeze(0)
    
    data = {
        'A': img, 
        'A_paths': None
    }
    
    # apply CycleGAN on the transformed image frame
    model.set_input(data)
    model.test()
    img_output = model.get_current_visuals()['fake']
    img_output = util.tensor2im(img_output)

    video_writer.write(img_output)

    index += 1
    if index % 20 == 0:
        print('{}th frame processed'.format(index))

print('video writing finished')
video_writer.release()
cap.release()
