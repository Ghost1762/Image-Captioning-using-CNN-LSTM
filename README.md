# Image-Captioning-using-CNN-LSTM

This project is focused on developing a model that can generate descriptive captions for given images. By analyzing the content of an image, the model will be able to predict an appropriate and accurate caption that reflects the scene or objects depicted.

## Architecture
![Architecture](Architecture.png)


## Description
During the training step, the image is passed through the Inception V3 model to extract features and characteristics, resulting in a feature map matrix. Simultaneously, the captions are divided into tokens and passed through the LSTM model to train it on generating accurate text, producing another matrix containing the characteristics of those captions.

Both the feature map and the caption characteristic matrix are combined (added element-wise) to create a new matrix, which serves as the input to the fully connected layers equipped with a softmax layer.

In the prediction step, the image is inserted into the Inception V3 model to extract the feature map and then input into the fully connected layers, which, with the help of the softmax activation, generates a probability distribution. This distribution helps determine the next word in the caption based on its word ID.

Note: The first word is always < start >.