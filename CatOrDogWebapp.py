# Building a Streamlit UI for the WebApp
import numpy as np
import os 
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow import keras
import streamlit as st
from PIL import Image
from keras.utils import load_img,img_to_array, save_img
from keras.models import model_from_json
import webbrowser

# #Loading our previously created trained model
# model=keras.models.load_model('my_model.h5',custom_objects={'KerasLayer':hub.KerasLayer})

#Defining a predictor function
def Cat_Or_Dog(image_path):
    img = load_img(image_path, target_size=(224, 224), color_mode="rgb")
    img_array = img_to_array(img)
    img_array = img_array/255.0
    img_array = img_array.reshape(1,224,224,3) # 1 indicates that we are making predictions for 1 image
    prediction=loaded_model.predict(img_array)
    pred_label = np.argmax(prediction)
    if pred_label==0:
        st.write("""
	    	## Its a DOG 🐶... Woof!!!
	    	""")
    else:
        st.write("""
	    	## Meowwww... Its a CAT 🐱!!!
	    	""")
    

 #This is the frontend UI interface. Build it according to your preferences.
 #creating a title
st.title('CatsVsDogs')

st.header("I know sometimes it's hard to tell a cat from a dog.To make sure you dont adopt the wrong one, we can help you identify it.")
st.write("I swear I'm not being sarcastic :smirk_cat:")
st.markdown('##')
    
#Getting the input data from the user where they are supposed to upload an image to be predicted
input_image= st.file_uploader('Upload an Image',['jpg','png'],accept_multiple_files=False,help='Just one image at a time please. Will work on the multiple scene if necessary.')
try:

    image = Image.open(input_image)
    img_array = np.array(image)
    
    st.write("""A Preview Of The Given Image! 👀""")
    if image is not None:
        st.image(image,use_column_width=True)
            
        st.write("""
            **Just Click The 'Lets Find Out' Button To See The Prediction. 😄**
            """)
except:
    st.write("""
		**Please Select an Appropriate Image 😄**
		""")

#creating a button for prediction
if st.button('lets Find Out...'):
    st.write("Predicting...")
    save_img("test_image.png",img_array)
    image_path = "test_image.png"
    model_path_h5 = "sequential_model.h5"
    model_path_json = "sequential_model.json"
    json_file = open(model_path_json, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json,custom_objects={'KerasLayer':hub.KerasLayer})
    loaded_model.load_weights(model_path_h5)
        
    loaded_model.compile(loss='SparseCategoricalCrossentropy', metrics=['accuracy'],optimizer='adam')
        
    prediction = print(Cat_Or_Dog(image_path))
        
