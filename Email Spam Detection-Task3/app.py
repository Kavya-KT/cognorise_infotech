import streamlit as st
import pickle
from PIL import Image
import re
import pandas as pd
from nltk.stem import SnowballStemmer
from nltk import TweetTokenizer
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# Initialize stemmer, tokenizer, and stopwords
s=SnowballStemmer('english')
t=TweetTokenizer()
sw=set(stopwords.words('english'))

# Load vectorizer and model
tfidf=pickle.load(open('vector.pkl','rb'))
model=pickle.load(open('model1.pkl','rb'))

st.title('EMAIL SPAM DETECTION')
img=Image.open('spam-filter.png')
st.image(img,width=250,use_column_width=True)

input_sms=st.text_area('enter the Email')

def preprocess_text(text):
    text = re.sub("[^a-zA-Z0-9 ]", " ", text)  # Clean text
    tokens = t.tokenize(text)  # Tokenize text
    tokens = [token.lower() for token in tokens if token.lower() not in sw and len(token) > 2]  # Remove stopwords and short tokens
    tokens = [s.stem(token) for token in tokens]  # Apply stemming
    return ' '.join(tokens)  # Join tokens back into a single string

pred=st.button('Predict')
if pred:
    transform_sms=preprocess_text(input_sms)
    vector=tfidf.transform([transform_sms])
    prediction=model.predict(vector)[0]

    if (prediction==1):
        st.header('SPAM')
    else:
        st.header('NOT SPAM')
