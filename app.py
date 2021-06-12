from PIL import Image
import numpy as np
import streamlit as st
import tensorflow as tf


def predict(image, model):
	img = image.resize((100, 100))
	img = np.asarray(img).reshape((1, 100, 100, 3)) / 255
	prediction = np.squeeze(model.predict(img))
	return 0 if prediction < 0.5 else 1



st.write("""
         # Malaria Classification
         """
         )

file = st.file_uploader("Please upload an image file", type=["png"])

model = tf.keras.models.load_model('model.h5')

labels = ['Normal', 'Malaria']

if file is None:
	st.text("Please upload an image file")

else:
	image = Image.open(file)
	prediction = predict(image, model)
	st.image(image, width=260, caption="Prediction : " + labels[prediction])

