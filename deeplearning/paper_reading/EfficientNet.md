### Compund Model Scaling

![image](https://user-images.githubusercontent.com/65876994/110277745-44b23700-8019-11eb-8f16-77637aea7c45.png)

![image](https://user-images.githubusercontent.com/65876994/110277763-4b40ae80-8019-11eb-8a32-d3a280bbfff5.png)


### Conclusion
- In this paper, we systematically study ConvNet scaling and identify that carefully balancing network width, depth, and resolution is an important but missing piece, preventing us
from better accuracy and efficiency. 
- To address this issue, we propose a simple and highly effective compound scaling method, which enables us to easily scale up a baseline ConvNet to any target resource constraints in a more principled
way, while maintaining model efficiency. 
- Powered by this compound scaling method, we demonstrate that a mobile-size EfficientNet model can be scaled up very effectively, surpassing state-of-the-art accuracy with an order of magnitude fewer parameters and FLOPS, on both ImageNet and five commonly used transfer learning datasets.
