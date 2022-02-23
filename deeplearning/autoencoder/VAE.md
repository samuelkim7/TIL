- In a nutshell, a VAE is an autoencoder whose encodings distribution is regularised during the training in order to ensure that its latent space has good properties allowing us to generate some new data.

### Dimentionality reduction
#### PCA
- The idea of PCA is to build n_e new independent features that are linear combinations of the n_d old features and so that the projections of the data on the subspace defined by these new features are as close as possible to the initial data (in term of euclidean distance).
- PCA is looking for the best linear subspace of the initial space (described by an orthogonal basis of new features) such that the error of approximating the data by their projections on this subspace is as small as possible.
- These n_e eigenvectors can be chosen as our new features and, so, the problem of dimension reduction can then be expressed as an eigenvalue/eigenvector problem.

#### Autoencoder
- linear autoencoder
  - Let’s first suppose that both our encoder and decoder architectures have only one layer without non-linearity (linear autoencoder).
  - Just like PCA does, we are looking for the best linear subspace to project data on with as few information loss as possible when doing so.
  - Several basis can be chosen to describe the same optimal subspace. Moreover, for linear autoencoders and contrarily to PCA, the new features we end up do not have to be independent.
- nonlinear case  
  - Now, let’s assume that both the encoder and the decoder are deep and non-linear. 
  - In such case, the more complex the architecture is, the more the autoencoder can proceed to a high dimensionality reduction while keeping reconstruction loss low. 

### VAE
- Autoencoder for data generation
  - it is pretty difficult (if not impossible) to ensure, a priori, that the encoder will organize the latent space in a smart way compatible with the generative process we just described.
  - The autoencoder is solely trained to encode and decode with as few loss as possible, no matter how the latent space is organised.
  - It is natural that, during the training, the network takes advantage of any overfitting possibilities to achieve its task as well as it can unless we explicitly regularise it!
- A variational autoencoder can be defined as being an autoencoder whose training is regularised to avoid overfitting and ensure that the latent space has good properties that enable generative process.
- In order to introduce some regularisation of the latent space, we proceed to a slight modification of the encoding-decoding process: instead of encoding an input as a single point, we encode it as a distribution over the latent space.
- A VAE model is trained as follows:  
![image](https://user-images.githubusercontent.com/65876994/154873287-0873d8a7-dc27-4091-80d6-941a6a7b08a5.png)
- In practice, the encoded distributions are chosen to be normal so that the encoder can be trained to return the mean and the covariance matrix that describe these Gaussians.
- A “regularisation term” (on the latent layer), that tends to regularise the organisation of the latent space by making the distributions returned by the encoder close to a standard normal distribution.  
![image](https://user-images.githubusercontent.com/65876994/154873598-56a994b6-e884-42cd-8a7e-bbf7441e2a56.png)
- Without a well defined regularisation term, the model can learn, in order to minimise its reconstruction error, to “ignore” the fact that distributions are returned and behave almost like classic autoencoders (leading to overfitting).
- So, in order to avoid these effects we have to regularise both the covariance matrix and the mean of the distributions returned by the encoder.
- In practice, this regularisation is done by enforcing distributions to be close to a standard normal distribution (centred and reduced).
- With this regularisation term, we prevent the model to encode data far apart in the latent space and encourage as much as possible returned distributions to “overlap”, satisfying this way the expected continuity and completeness conditions.

### Probabilistic Explanation of VAE
- Two assumptions: a latent representation z is sampled from the prior distribution p(z) / the data x is sampled from the conditional likelihood distribution p(x|z).
- The “probabilistic decoder” is naturally defined by p(x|z), that describes the distribution of the decoded variable given the encoded one.
- whereas the “probabilistic encoder” is defined by p(z|x), that describes the distribution of the encoded variable given the decoded one.  
![image](https://user-images.githubusercontent.com/65876994/154876075-af8e021f-84e1-4a67-a583-3df00a61f278.png)  
![image](https://user-images.githubusercontent.com/65876994/154876065-39d7b048-5180-4421-93a6-042014a02ec3.png)  
- Using Bayes theorem to comput p(z|x) is often intractable (because of the integral at the denominator) and require the use of approximation techniques such as variational inference.

#### Variational inference formulation
- In statistics, variational inference (VI) is a technique to approximate complex distributions.
- The best element in the family is one that minimise a given approximation error measurement (most of the time the Kullback-Leibler divergence between approximation and target) and is found by gradient descent over the parameters that describe the family.
- We want to choose the function f that maximises the expected log-likelihood of x given z when z is sampled from q_x(z).
- In other words, for a given input x, we want to maximise the probability to have x̂ = x when we sample z from the distribution q_x(z) and then sample x̂ from the distribution p(x|z).


### Summary
![image](https://user-images.githubusercontent.com/65876994/154874867-7d1c0f75-0d05-4375-9188-99524b5c4e89.png)


### Reference
[Link](https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73#:~:text=In%20a%20nutshell%2C%20a%20VAE,to%20generate%20some%20new%20data.)