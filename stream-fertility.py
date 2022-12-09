from ast import If
import pickle
import streamlit as st

#Membaca Model
fertility_model = pickle.load(open('fertility_model.sav', 'rb'))

#Judul Web
st.title('DATA MINING PREDIKSI FERTILITY')

st.subheader('NAMA : AYI RIANI')
st.subheader('NIM : 191351009')

Season = st.text_input('Input Nilai Season')

Age = st.text_input ('Input Nilai Age')

Childish_diseases = st.text_input (' Input Nilai Childish diseases')

Accident_or_serious_trauma = st.text_input ('Input Nilai Accident or serious trauma')

Surgical_intervention = st.text_input (' Input Nilai Surgical intervention')

High_fevers_in_the_last_year = st.text_input ('Input Nilai High fevers in the last year')

Frequency_of_alcohol_consumption = st.text_input ('Input Nilai Frequency of alcohol consumption')

Smoking_habit = st.text_input ('Input Nilai Smoking habit') 

Number_of_hours_spent_sitting_per_day = st.text_input ('Input Nilai Number of hours spent sittingper_day') 
#code untuk prediksi
ferti_diagnosis = ''

#membuat tombol
if st.button('Test') :
    fertility_prediction = fertility_model.predict([[Season, Age, Childish_diseases, Accident_or_serious_trauma, Surgical_intervention, High_fevers_in_the_last_year, Frequency_of_alcohol_consumption, Smoking_habit, Number_of_hours_spent_sitting_per_day ]])
    
    if  (fertility_prediction[0] == 1):
           ferti_diagnosis = 'SUBUR'
    else :
           ferti_diagnosis = ' TIDAK SUBUR'

    st.success(ferti_diagnosis)