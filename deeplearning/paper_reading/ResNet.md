## Deep Residual Learning for Image Recognition
Kaiming He, ...

## Introduction
- Driven by the significance of depth, a question arises: Is learning better networks as easy as stacking more layers?
- When deeper networks are able to start converging, a degradation problem has been exposed: with the network depth increasing, accuracy gets saturated (which might be unsurprising) and then degrades rapidly.
- In this paper, we address the degradation problem by introducing a deep residual learning framework. 
- The original mapping is recast into F(x)+x. We hypothesize that it is easier to optimize the residual mapping than to optimize the original, unreferenced mapping.  
- To the extreme, if an identity mapping were optimal, it would be easier to push the residual to zero than to fit an identity mapping by a stack of nonlinear layers.
- In our case, the shortcut connections simply perform identity mapping, and their outputs are added to the outputs of the stacked layers.
- 1) Our extremely deep residual nets are easy to optimize, but the counterpart “plain” nets (that simply stack layers) exhibit higher training error when the depth increases; 
- 2) Our deep residual nets can easily enjoy accuracy gains from greatly increased depth, producing results substantially better than previous networks.

