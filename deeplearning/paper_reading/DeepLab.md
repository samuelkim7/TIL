

### Introduction
- While this invariance is clearly desirable for high-level vision tasks, it can hamper low-level tasks, such as pose estimation (Chen & Yuille, 2014; Tompson et al., 2014) and semantic segmentation - where we want precise localization, rather than abstraction of spatial details.
- We use the fully connected pairwise CRF proposed by Krahenb ¨ uhl & Koltun (2011) for its efficient computation, and ability to capture fine edge details while also catering for long range dependencies.


### CNN
- We finetune the model weights of the Imagenet-pretrained VGG-16 network to adapt it to the image classification task in a straightforward fashion, following the procedure of Long et al. (2014). We replace the 1000-way Imagenet classifier in the last layer of VGG-16 with a 21-way one.
- 
