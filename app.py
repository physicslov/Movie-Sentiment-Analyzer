import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Embedding,Dense,SimpleRNN
from tensorflow.keras.callbacks import EarlyStopping,TensorBoard
import streamlit as st
model = load_model('model.h5')
word_index = imdb.get_word_index()
def preprocess_text(text):
  words = text.lower().split()
  encoded_review = [word_index.get(word,2)+3 for word in words]
  padded_review = sequence.pad_sequences([encoded_review],maxlen=500)
  return padded_review

def predict_sentiment(review):
  preprocessed_input = preprocess_text(review)
  prediction = model.predict(preprocessed_input)
  sentiment = 'Positive' if prediction[0][0]>0.5 else 'Negative'
  return sentiment

st.title("IMDB Movie Review Sentiment Analyzer")
st.write("Enter a movie review to classify it as Positive or Negative")
user_input = st.text_area('Movie_Review')

if st.button('Classify'):
  prediction = predict_sentiment(user_input)
  st.write(prediction)
else:
  st.write('Please Enter the movie review')