## About
In the data science world, the amount of data can play a crucial role in performing various analysis. But in fields such as Mining, Pharmaceutics and Medicine, the amount of data available is very less and recording extra data is very expensive or sometimes just impossible. Synthetic Data Generator webapp is useful in developing new data using AI. Synthetically generated data is statistically similar to the original data but is entirely different from the original data. 

## Technology used:
The core technology used behind Synthetic data generation is CTGANs (Conditional Tabular Generative Adversarial Networks). CTGANs are basically GAN models modified for accepting and generating tabular data. GANs are generative models used to generate images, sound, text and now tabular data. GANs are made from combining two Neural Networks models and training them against each other. One is Generator and other is Discriminator. Generator's task is to generate fake data that can resemble the real data such that it can fool the Discriminator model while Discriminator model's task is to Discriminate between real and generated fake data. Generator is penalised if fake data is detected by discriminator. Both these models are trained simultaneously, where generator becomes better and better in generating fake data such that it can fool the discriminator.

![gan](https://github.com/yash-shimpi/TMLC/blob/main/images/GANs.png)

## About the project: 

This webapp is developed by Yash Shimpi under the guidance of TMLC ([The Machine Learning Co.](https://themlco.com/)) Fellowship Programme. 

Reference Links:
- Generative Adversarial Networks - [**GANs**](https://arxiv.org/pdf/1406.2661.pdf)
- Conditional Tabular GANs - [**CTGAN**](https://proceedings.neurips.cc/paper/2019/file/254ed7d2de3b23ab10936522dd547b78-Paper.pdf)
- TabGANs by diyago - [Github](https://github.com/Diyago/GAN-for-tabular-data)



[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://yash-shimpi-tmlc-home-qahryb.streamlit.app/)
 
