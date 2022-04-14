import streamlit as st
import pandas as pd
import numpy as np
#import sklearn
import joblib
#import sklearn


st.title("Salary Prediction app")

#st.text_input("Your name", key="name")
# You can access the value at any point with:
# st.session_state.name


# turns a list into a dataframe #
def make_list_to_df(list):
    df = pd.DataFrame(columns=['Country', 'Employment', 'FormalEducation', 'DevType',
                               'YearsCodingProf', 'Age'])
    df.loc[len(df)] = list
    return df

# model prediction #


def salary_prediction(model, new_data):
    salary = model.predict(new_data)
    return salary


with st.form("my_form"):
    Country = st.selectbox(
        'Please select a Country',
        ('United States', 'India', 'United Kingdom', 'Germany', 'Canada'))
#    st.write('You selected:', Country)

    Employment = st.selectbox(
        'Please select a Type of Employment',
        ('Employed full-time', 'Independent contractor', 'Employed part-time', 'looking for work'))
#    st.write('You selected:', Employment)

    FormalEducation = st.selectbox(
        'Please select a Education Level: (High-->PhD) (Medium-->Masters) (Low-->Bachelors or lower)',
        ('High', 'Medium', 'Low'))
#    st.write('You selected:', FormalEducation)

    DevType = st.selectbox(
        'Please select Dev Type',
        ('Database administrator', 'Back-end developer', 'Mobile developer',
         'Full-stack developer', 'Designer', 'Front-end developer',
         'Engineering manager',
         'Embedded applications or devices developer',
         'Data scientist or machine learning specialist',
         'Desktop or enterprise applications developer',
         'C-suite executive (CEO, CTO, etc.)', 'QA or test developer',
         'System administrator', 'Data or business analyst',
         'DevOps specialist', 'Educator or academic researcher', 'Student',
         'Game or graphics developer', 'Product manager',
         'Marketing or sales professional'))
    st.write('You selected:', DevType)

    YearsCodingProf = st.slider(
        'Select closest years of coding', 0, 30)
    if YearsCodingProf == 0:
        YearsCodingProf = "0"
    elif YearsCodingProf == 1:
        YearsCodingProf = "1"
    elif YearsCodingProf <= 5:
        YearsCodingProf = "5"
    elif YearsCodingProf <= 7:
        YearsCodingProf = "7"
    elif YearsCodingProf <= 10:
        YearsCodingProf = "10"
    elif YearsCodingProf <= 13:
        YearsCodingProf = "13"
    elif YearsCodingProf <= 16:
        YearsCodingProf = "16"
    elif YearsCodingProf <= 19:
        YearsCodingProf = "19"
    elif YearsCodingProf <= 22:
        YearsCodingProf = "22"
    elif YearsCodingProf <= 25:
        YearsCodingProf = "25"
    elif YearsCodingProf <= 28:
        YearsCodingProf = "28"
    elif YearsCodingProf <= 30:
        YearsCodingProf = "30"
#    st.write('years coding:', YearsCodingProf)

    Age = st.slider(
        'How old are you?', 0, 65)
    if Age <= 18:
        Age = "18"
    elif Age <= 21:
        Age = "21"
    elif Age <= 30:
        Age = "30"
    elif Age <= 40:
        Age = "40"
    elif Age <= 50:
        Age = "50"
    elif Age <= 64:
        Age = "60"
    elif Age == 65:
        Age = "65"
#    st.write("years old: ", age)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        new_entry = [Country, Employment, FormalEducation, DevType,
                     YearsCodingProf, Age]
#        st.write(new_entry)

        # make new_entry into a DataFrame #
#        st.write(make_list_to_df(new_entry))
        new_entry_df = make_list_to_df(new_entry)
        # Load model #
        filename = 'linear_reg_model.sav'
        linear_reg_model_reloaded = joblib.load(filename, 'r')

        # function to calculate salary #
        salary = salary_prediction(linear_reg_model_reloaded, new_entry_df)

        st.write(" ### Salary: ", salary[0].round(2))
