# Diabetes Prediction App

This web application predicts the likelihood of diabetes based on input features such as age, gender, medical history, BMI, and blood glucose levels. It utilizes machine learning models trained on a diabetes prediction dataset.

## Features

### Input Features

- **Age**: Numeric input for age in years.
- **Gender**: Radio button for selecting gender (Female/Male).
- **Hypertension**: Radio button for hypertension status (Yes/No).
- **Heart Disease**: Radio button for heart disease status (Yes/No).
- **Smoking History**: Dropdown for smoking history (never smoker, ever smoker, former smoker, current smoker, No Info).
- **BMI**: Numeric input for Body Mass Index (BMI).
- **HbA1c Level**: Numeric input for HbA1c (glycated hemoglobin) level.
- **Blood Glucose Level**: Numeric input for blood glucose level.

## Technologies Used

- **Python**: Main programming language used for backend logic and model deployment.
- **Streamlit**: Framework used for creating a user-friendly web application interface.
- **Pickle**: Python module used for serializing and deserializing Python objects (used for saving trained models and preprocessing scalers).
- **Scikit-learn**: Machine learning library in Python used for model training, evaluation, and preprocessing.
- **Pandas**: Python library for data manipulation and preprocessing.

## Dataset

- The dataset used for training the model can be found [here](link-to-your-dataset).
- It includes features such as age, gender, BMI, hypertension, heart disease, smoking history, HbA1c level, and blood glucose level.

## Model Deployment

- The RandomForestClassifier model achieved high accuracy and was chosen for deployment.
- Model and scaler were serialized using Pickle for deployment in the Streamlit app.


