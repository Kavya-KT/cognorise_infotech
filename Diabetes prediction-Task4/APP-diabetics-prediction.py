import pandas as pd
import streamlit as st
from PIL import Image
import pickle
from sklearn.preprocessing import LabelEncoder

#load
model=pickle.load(open('diabetes_model.save','rb'))
scaler=pickle.load(open('diabetes_scaler.save','rb'))
encod=pickle.load(open('diabetics_encoder.save','rb'))
encod1=pickle.load(open('diabetics_encoder1.save','rb'))


# Define a function to navigate to the selected page
def navigate_to(page):
    st.session_state.current_page = page

# Initialize session state for the current page
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'

with st.sidebar:
    st.title('Navigation')

    if st.button("Home"):
        navigate_to("Home")

    if st.button("Symptoms"):
        navigate_to("Symptoms")

    if st.button("Complications"):
        navigate_to("Complications")

    if st.button("Management and Treatment"):
        navigate_to("Management and Treatment")

    if st.button("Prevention"):
        navigate_to("Prevention")

    if st.button("Dataset"):
        navigate_to("Dataset")

    if st.button("Google Colab"):
        navigate_to("Google Colab")

    if st.button('Check Diabetics'):
        navigate_to(('Check Diabetics'))

# Display the selected page
if st.session_state.current_page == "Home":
    st.title('DIABETES PREDICTION')
    img = Image.open('download.jpg')
    st.image(img, width=500)
    st.write()
    st.write(':point_right: Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high.')
    st.write(':point_right: Glucose is your body’s main source of energy. Your body can make glucose, but glucose also comes from the food you eat.')
    st.write(
        ":point_right: Insulin is a hormone made by the pancreas that helps glucose get into your cells to be used for energy. If you have diabetes, your body doesn’t make enough—or any—insulin, or doesn’t use insulin properly. "
        "Glucose then stays in your blood and doesn’t reach your cells.")
    st.write(':point_right: Diabetes raises the risk for damage to the eyes, kidneys, nerves, and heart. Diabetes is also linked to some types of cancer. Taking steps to prevent or manage diabetes may lower your risk of developing diabetes health problems.')


elif st.session_state.current_page == "Symptoms":
    st.title('Symptoms of Diabetes')
    st.write("1. Increased thirst and hunger")
    st.write("2. Frequent urination")
    st.write("3. Unexplained weight loss")
    st.write("4. Fatigue")
    st.write("5. Blurred vision")
    st.write("6. Slow-healing sores")
    st.write("7. Frequent infections")

elif st.session_state.current_page == "Complications":
    st.title('Complications of Diabetes')
    st.write("If poorly managed, diabetes can lead to complications such as:")
    st.write("1. Cardiovascular disease (heart attack, stroke)")
    st.write("2. Neuropathy (nerve damage)")
    st.write("3. Nephropathy (kidney damage)")
    st.write("4. Retinopathy (eye damage leading to blindness)")
    st.write("5. Foot problems (infections, ulcers)")

elif st.session_state.current_page == "Management and Treatment":
    st.title('Management and Treatment')
    st.write(":point_right: Diet and Exercise: A balanced diet and regular physical activity are crucial in managing diabetes.")
    st.write(":point_right: Medications: Depending on the type, medications can include insulin, metformin, sulfonylureas, and others.")
    st.write(":point_right: Blood Sugar Monitoring: Regular monitoring of blood glucose levels helps in managing the condition effectively.")
    st.write(":point_right: Education and Support: Education on diabetes management and support from healthcare providers, family, and support groups can significantly improve outcomes.")

elif st.session_state.current_page == "Prevention":
    st.title('Prevention of Diabetes')
    st.write("1. Maintain a healthy weight.")
    st.write("2. Follow a balanced diet rich in fruits, vegetables, whole grains, and lean proteins.")
    st.write("3. Exercise regularly.")
    st.write("4. Avoid tobacco use.")
    st.write("5. Limit alcohol consumption.")
    st.write('Early detection and proper management are key to preventing complications associated with diabetes.')

elif st.session_state.current_page == "Dataset":
    st.title('Dataset')
    st.write("You can find the dataset :point_right: [here](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)")
    st.write(':orange[Age]: Age is an important factor in predicting diabetes risk. As individuals get older, their risk of developing diabetes increases. This is partly due to factors such as reduced physical activity, changes in hormone levels, and a higher likelihood of developing other health conditions that can contribute to diabetes.')
    st.write(':orange[Gender]: Gender can play a role in diabetes risk, although the effect may vary. For example, women with a history of gestational diabetes (diabetes during pregnancy) have a higher risk of developing type 2 diabetes later in life. Additionally, some studies have suggested that men may have a slightly higher risk of diabetes compared to women.')
    st.write(":orange[Body Mass Index (BMI)]: BMI is a measure of body fat based on a person's height and weight. It is commonly used as an indicator of overall weight status and can be helpful in predicting diabetes risk. Higher BMI is associated with a greater likelihood of developing type 2 diabetes. Excess body fat, particularly around the waist, can lead to insulin resistance and impair the body's ability to regulate blood sugar levels.")
    st.write(":orange[Hypertension]: Hypertension, or high blood pressure, is a condition that often coexists with diabetes. The two conditions share common risk factors and can contribute to each other's development. Having hypertension increases the risk of developing type 2 diabetes and vice versa. Both conditions can have detrimental effects on cardiovascular health.")
    st.write(":orange[Heart Disease]: Heart disease, including conditions such as coronary artery disease and heart failure, is associated with an increased risk of diabetes. The relationship between heart disease and diabetes is bidirectional, meaning that having one condition increases the risk of developing the other. This is because they share many common risk factors, such as obesity, high blood pressure, and high cholesterol.")
    st.write(":orange[Smoking History]: Smoking is a modifiable risk factor for diabetes. Cigarette smoking has been found to increase the risk of developing type 2 diabetes. Smoking can contribute to insulin resistance and impair glucose metabolism. Quitting smoking can significantly reduce the risk of developing diabetes and its complications.")
    st.write(":orange[HbA1c Level]: HbA1c (glycated hemoglobin) is a measure of the average blood glucose level over the past 2-3 months. It provides information about long-term blood sugar control. Higher HbA1c levels indicate poorer glycemic control and are associated with an increased risk of developing diabetes and its complications.")
    st.write(":orange[Blood Glucose Level]: Blood glucose level refers to the amount of glucose (sugar) present in the blood at a given time. Elevated blood glucose levels, particularly in the fasting state or after consuming carbohydrates, can indicate impaired glucose regulation and increase the risk of developing diabetes. Regular monitoring of blood glucose levels is important in the diagnosis and management of diabetes.")

    st.write()
    #load datasset
    st.write(':red[Dataset]:point_down:')
    df=pd.read_csv(r'C:\Users\user\PycharmProjects\Mechine_Learning\cognorise\Diabetes prediction\diabetes_prediction_dataset.csv')
    st.write(df)
elif st.session_state.current_page == "Google Colab":
    st.title('Google Colab')
    st.write("You can find the Google Colab notebook :point_right: [here](https://colab.research.google.com/drive/1FseBoKYdr9hcN5YD69zhSZ7uznGlcA0e#scrollTo=Lh-k03KExilq)")

elif st.session_state.current_page=="Check Diabetics":
    st.title('Diabetics Prediction')

    #input features

    Gender=st.radio('gender',['Female','Male'])
    # if Gender=='Female':
    #     Gender=0
    # else:
    #     Gender=1
    gen=encod.transform([Gender])[0]

    age=st.text_input('Age','text here')

    hypertension=st.radio('hypertension',['Yes','No'])
    if hypertension=='Yes':
        hypertension=1
    else:
        hypertension=0

    heart_disease=st.radio('heart_disease',['Yes','No'])
    if heart_disease=='Yes':
        heart_disease=1
    else:
        heart_disease=0

    smoking_history=st.selectbox('smoking_history',['not current','former','No Info','current','never','ever'])

    smoke_enco=encod1.transform([smoking_history])[0]


    bmi=st.text_input('BMI','text here')
    HbA1c_level=st.text_input('HbA1c_level','text here')
    bgl=st.text_input('blood glucose level','text here')

    features=[gen,age,hypertension,heart_disease,smoke_enco,bmi,HbA1c_level,bgl]

    predict=st.button('Click')
    if predict:
        pred=model.predict(scaler.transform([features]))

        if pred==1:
            st.header('Indicating the presence of Diabetes')
        else:
            st.header('No  Diabetes')



