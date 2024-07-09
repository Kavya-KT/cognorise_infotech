
# Email Spam Detection App

This application uses machine learning techniques to classify emails as either spam or not spam (ham). It includes a simple user interface built with Streamlit for easy interaction.

## Features

1. **Text Preprocessing:**
   Cleans and preprocesses the input email text by removing special characters, stopwords, and applying stemming.

2. **Machine Learning Model:**
   Uses a logistic regression model trained on a dataset of pre-labeled emails.

3. **Prediction:**
   Displays the prediction result (spam or not spam) based on the input email text.

## Technologies Used

- Python
- Streamlit: For building the web application interface.
- NLTK: For natural language processing tasks such as tokenization and stemming.
- Scikit-learn: For machine learning model training and evaluation.
- Pandas: For data manipulation and preprocessing.
