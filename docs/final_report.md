
## Image Caption Generator

### Team: Sravya Pamula and Hema Kavuri

An image caption generator basically generates decsriptions of what is going on in a given image. This is a natural human ability to look at an image and pay attention to the curcial information in the image and describe it in just a few words. Can a machine do this? Using tools such as natural language processing and object detection (computer vision), it is possible to train a model to do this task. This will be explored in this project.

Image caption generator bears applications in assistive technology and can help visually imapired to infer their surroundings. It can also be extended to uses such as map descriptions for users/self-driven cars. The primary goal of the project will be to learn Deep learning and NLP tools to build a model that can analyse the images and comprehend the meaning from given captions.

#### Dataset:

The dataset that will be used for this is the Flickr8k which can be found here: https://www.kaggle.com/datasets/e1cd22253a9b23b073794872bf565648ddbe4f17e7fa9e74766ad3707141adeb. This dataset consists of about 8000 image files and captions for the same. The captions are in a csv file which has around 40,000 records implying that the each image has more than one caption. 
Apart from these we also have a test examplex dataset with 8 images for which captions need to be generated.

#### Pre-processing:

- Vocabulary Class: Tokens are created for words that occur more than a chosen threshold frequency. String to index (stoi) and Index to string (itos) dictionaries are created to switch from string to index for these tokens. This is needed as the machine inputs numbers and hence we need to convert the words to indices. Pad token, start of sentence, end of sentence and unknown are defined to help the model make decisions about start, end and padding in captions. 

- FlickrDataset Class: In this class we define dataset attributes such as root directory, captions file, etc. This class will be used later on to get the data ready and load the data using getloader class. This class retrieves the image and caption from the dataset and numericalizes it. It returns a PyTorch Tensor that can be used for pytorch modeling. 

- MyCollate Class: Converts all the images into the same dimensions for modeling. Pads the target captions to the same length for modeling.

- GetLoader Class: This class defines a FlickrDataset class object and uses the inbuilt PyTorch DataLoader to get the data ready for modeling in PyTorch.

#### Modeling:

The model will be in the form of an encoder-decoder. 
- Encoder CNN:  The encoder will be a Convolutional neural network. This part will be used to understand the images and detect the core information in them by encoding them. Pretrained CNN model inception v3 model is used to learn the information from the images. Last Fully Connected (Linear) layer of the pretrained model is modified to return a tensor of the size that goes into the RNN (LSTM).

- Decoder RNN: The output of the CNN will be input to the decoder RNN. The decoder will be a series of LSTM's (Long short term memory - a recurrent neiral network - https://en.wikipedia.org/wiki/Long_short-term_memory), which will generate the caption based on the output information from the encoder. LSTM is the most used RNN for natural language processing as it retains context/information in long-term memory along with the short-term memory from the previous time step. LSTM takes in output from the encoder CNN and uses it along with Vocabulary to generate captions based on context. We will be using PyTorch to implement these models.

- CNNtoRNN: Combines both the EncoderCNN and DecoderRNN models. Words of the caption are generated one by one. The initial input is the output of the EncoderCNN which is used to generate the first word of the caption. This word is sent to the DecoderRNN again and is used to generate the next words. 

We will be training our model using mini-batch gradient descent. We will be training our model in epochs. The optimizer will train the model by reducing the loss function which is calculated using the generated words and the words in the exisitng captions (while training).

#### Results:

We train our model for 1, 10 and 30 epochs. The observations we made based on the captions generated are:

1. As our dataset consists of images with people, the model tends to recognise people easily and also brings up people in images where there are no people. 
2. For the same reason as above, our model easily identifies people, balls, grass. 
3. When trained for only one epoch, the model learns only a few words and generates the same caption for different images although not for all of them. 
4. When the number of epochs are increased from 1 to 10 and 30, we see imrpovement. The model generates unique captions for each of the test images and does a good job of identifying some core elements of the image.  


#### Deployment:
A simple web application will be built using streamlit that will ask the user for an image and generate a caption for the given image.

#### References:

https://arxiv.org/pdf/1502.03044.pdf
https://github.com/Siddharth1698/Image-Captioning-with-Inception-LSTM
