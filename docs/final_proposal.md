## Image Caption Generator

Team: Sravya Pamula and Hema Kavuri

An image caption generator basically generates decsriptions of what is going on in a given image. This is a natural human ability to look at an image and pay attention to the curcial information in the image and describe it in just a few words. Can a machine do this? Using tools such as natural language processing and object detection (computer vision), it is possible to train a model to do this task. This will be explored in this project. 

Image caption generator bears applications in assistive technology and can help visually imapired to infer their surroundings. 
It can also be extended to uses such as map descriptions for users/self-driven cars. 
The primary goal of the project will be to learn Deep learning and NLP tools to build a model that can analyse the images and comprehend the meaning from given captions.

<img src="draftproposalimage.jpg" width="800"/>

### Dataset:

The dataset that will be used for this is the Flickr8k which can be found here:
https://www.kaggle.com/datasets/e1cd22253a9b23b073794872bf565648ddbe4f17e7fa9e74766ad3707141adeb
This dataset consists of about 8000 image files and captions for the same. 

References that will be used are:
1. https://arxiv.org/pdf/1502.03044.pdf
2. https://github.com/Siddharth1698/Image-Captioning-with-Inception-LSTM

### Methods:

The model will be in the form of an decoder-encoder. The decoder will be a Convolutional neural network. This part will be used to understand the images and detect the core information in them. Pretrained CNN models such as VGG, AlexNet or LeeNet will be used to learn the information from the images. The output of the CNN will be input to the encoder. The encoder will be a series of LSTM's (Long short term memory - a recurrent neiral network - https://en.wikipedia.org/wiki/Long_short-term_memory), which will generate the caption based on the output information from the decoder. We will be using PyTorch to implement these models. 

We will be training our model using mini-batch gradient descent. We will be training our model in epochs. The optimizer will train the model by reducing the loss function which is calculated using the generated words and the words in the exisitng captions (while training). These are aspects of the project that we will figure out as we go along working on the project.


### Deployment:

A simple web application will be built using streamlit that will ask the user for an image and generate a caption for the given image. 

### Outcome:

Through this project we will build an image caption generator that will generate captions for a user given image. 

### Next steps and work distribution:

As our dataset consists of just images (.jpg files)and captions (a text file), we do not have any EDA to perform. The next step would be to start building the decoder. Before this we will be brushing up PyTorch basics and figure out how we should input our data into the decoder (CNN) model.

Work distribution: Hema will figure out how we need to input our data into the model, and the hyperparameters needed for training the model (hyperparameters of the model as well as the optimizing process). I will build the decoder model using pretrained CNN models in PyTorch. 


