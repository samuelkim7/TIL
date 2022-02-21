![image](https://user-images.githubusercontent.com/65876994/154869409-3c8e21dc-cb4a-4bc7-8f9e-404bc7da4f54.png)  
ICRL 2020

![image](https://user-images.githubusercontent.com/65876994/154869456-3fbc242b-4bfe-4fd9-8b9a-791ccea49a39.png)

### Related work
- To test novelty, an input value is fed to the autoencoder to produce a reconstructed value and calculate the distance between the input and reconstructed values. This distance is the reconstruction error. A higher reconstruction error means that the input value cannot be encoded onto the lower-dimensional space that represents normal data.

### RAPP
- The main idea is to compare hidden activations of an input and its hidden reconstructions along the projection pathway of the autoencoder.
- To be precise, we project the input and its autoencoder reconstruction onto the hidden spaces to obtain pairs of activation values, and aggregate them to quantify the novelty of the input. For the aggregation, we present two metrics to measure the total amount of difference within each pair.
- Specifically, training an autoencoder on normal data samples, novelty of a test sample x is measured by the following reconstruction error:
![image](https://user-images.githubusercontent.com/65876994/154869747-20ca130f-0458-4dd2-9678-56ea2b57ab9c.png)
- The test sample x is more likely to be novel as the error becomes larger, because it means that x is farther from the manifold that the autoencoder describes.

#### Simple Aggregation along Pathway (SAP)
- For a data sample x, SAP is defined by summing the square of Euclidean distances for all pairs in H:
![image](https://user-images.githubusercontent.com/65876994/154869970-17119e7a-eb70-4dad-9957-3e0143e09946.png)
- where h(x) and hˆ(x) are the concatenations of [h0(x), · · · , hl(x)] and [hˆ0(x); · · · ; hˆl(x)], respectively.

#### Normalized Aggregation along Pathway (NAP)
- Distance distributions of pairs in H may be different depending on the individual hidden spaces. To capture clearer patterns, we propose to normalize the distances via two steps: orthogonalization and scaling.

### Evaluation
- Novelty detection detects novel patterns by focusing on deviations from model-learned normal patterns. Thus, training sets contain only normal samples and test sets contain both normal and anomaly samples in our evaluation setups.
- We compare RAPP and the other methods using Area Under Receiver Operating Characteristic (AUROC). 
- We use symmetric architecture with fully-connected layers for the three base models, AE, VAE, and AAE. Each encoder and decoder has 10 layers with different bottleneck size.
- Leaky-ReLU (Xu et al., 2015a) activation and batch normalization (Ioffe & Szegedy, 2015) layers are appended to all layers except the last layer.
- We train AE, VAE and AAE with Adam optimizer (Kingma & Ba, 2015), and select the model with the lowest validation loss as the best model.
- For training stability of VAE, 10 Monte Carlo samples were averaged in the reparamterization trick (Kingma & Welling, 2014) to obtain reconstruction from the decoder.
