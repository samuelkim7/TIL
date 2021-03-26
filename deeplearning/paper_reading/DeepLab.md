## SEMANTIC IMAGE SEGMENTATION WITH DEEP CONVOLUTIONAL NETS AND FULLY CONNECTED CRFS
- Liang-Chieh Chen et al.

### Introduction
- While this invariance is clearly desirable for high-level vision tasks, it can hamper low-level tasks, such as pose estimation (Chen & Yuille, 2014; Tompson et al., 2014) and semantic segmentation - where we want precise localization, rather than abstraction of spatial details.
- We use the fully connected pairwise CRF proposed by Krahenb ¨ uhl & Koltun (2011) for its efficient computation, and ability to capture fine edge details while also catering for long range dependencies.


### CNN
- We finetune the model weights of the Imagenet-pretrained VGG-16 network to adapt it to the image classification task in a straightforward fashion, following the procedure of Long et al. (2014). We replace the 1000-way Imagenet classifier in the last layer of VGG-16 with a 21-way one.

### FC CRF
- Their increased invariance and large receptive fields make the problem of inferring position from the scores at their top output levels more challenging.
- Deeper models with multiple max-pooling layers have proven most successful in classification tasks, however their increased invariance and large receptive fields make the problem of inferring position from the scores at their top output levels more challenging.
- Traditionally, conditional random fields (CRFs) have been employed to smooth noisy segmentation maps (Rother et al., 2004; Kohli et al., 2009). Typically these models contain energy terms that couple neighboring nodes, favoring same-label assignments to spatially proximal pixels. 

### Atrous algorithm
-  This approach is generally applicable and allows us to efficiently compute dense CNN feature maps at any target subsampling rate without introducing any approximations.

### Field of View
- The ‘atrous algorithm’ we employed allows us to arbitrarily control the Field-ofView (FOV) of the models by adjusting the input stride.
