# DS-Project-6-CatVsDog_Transfer_Learning
Engineered a model that can classify between a Cat and a Dog. Deployed a model using streamlit on Heroku.

* Designed an image recognition model that can classify between a cat and a dog. Developed an app using streamlit that takes the picture of a dog or cat as input and the ml model in the backend gives us the approrpiate classification.
* Dataset - Part of a Kaggle Competition. The training archive contains 25,000 images of dogs and cats. Please check the data resources tab below.
* Model - The major aim of in this project is to distinguish between a cat and a dog. Optimized a neural network model using Transfer Learning algorithm, making good use of a pre-trained model.

## Code and Resources Used ##
**Python Version:** 3.10.5 <br />
**Packages:**  numpy, sklearn, matplotlib, PIL,tensorflow,tensorflow_hub,keras streamlit,webbrowser <br />
**For Web Framework Requirements:** _pip install -r requirements.txt_ <br />
**Data Resources:** <https://www.kaggle.com/competitions/dogs-vs-cats/data> <br />
**Pre-Trained Model:** MobileNet_model <https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4>

## About the Dataset ##
- Dataset consists of 25,000 images of cats and dogs in the train.zip folder. We use the images in this folder to train our model. 
- The images in the test folder will be used to evaluate the model.

## Prepocessing the images for the model ## 
1. These images are not in same shape and since our pre=trained model requires a specific shape. We manipulate and resize all images in the required size which is (224,224,3).
2. Separating the cats and dogs in different files so that we can pick equal amounts of pictures to train our model.
3. Since we are using a pre-trained model with pre-trained weights, we dont have to use all the images in our dataset to train our model.I just use 2000 pictures of both cats and dogs for my model.
4. Creating labels for resized images of dogs and cats where cats are represented by 1 and dogs are represented by 0.
5. Converting all resized images to NumPy arrays as our model only takes numpy array as input.
6. Splitting the dataset into training and testing sets using the sklearn library.
7. Feature Scaling- Dividing all values by 255 because the that is my maximum intensity of colors

## Model Building ##
1. Uploading the mobilenet model from the url given above from the tensorflow-hub library 
2. Defining a simple keras Sequential model with the mobilenet model weights and an output layer.
3. Compiling the model accordingly:
    - optimizer : 'adam' - optimization technique for gradient descent
    - loss : 'SparseCategoricalCrossentropy' - as we are dealing with binary classification
    - metrics : 'accuracy' - simple as its just a binary classification

## Model Performance ##
As its a pre=trained model, we dont require a lot of epochs to train our model. After just 5 epochs we get an accuracy score of *0.99* and a loss score of *0.036* on the training data.
After Evaluating it on the test data, we receive an accuracy score of *0.97* and a loss score of *0.066*. That means we predict 97 pictures out of 100 accurately.

## Saving and Loading Model ##
Saved the model in the '.h5' format so that we can use it on the backend for our application.

## Building a Python Application ##
- After we import all the required dependencies listed above, we define a simple predictor function which takes an image as input from the user and after preprocessing is classified as a 'CAT' or 'DOG' by the ml model running in the background.

- Built the front-end UI using the streamlit library. Customize it according to your preferences , don't be afraid from adding your touches :P

- After pushing the the python app , procfile and setup.sh (you will find these files in my repo) to a Github Repository, you can deploy the app on Heroku by creating a free account or any other hosting platform.


