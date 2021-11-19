import streamlit as st
import numpy as np
import pandas as pd
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown("""# Taxi Fare Prediction
## Parameters
Please enter the following information:""")

st.markdown('date and time')
user_input1 = st.date_input("Date")
user_input2 = st.time_input("time")

st.markdown('Pickup')
user_input3 = st.number_input("pickup_longitude")
user_input4 = st.number_input("pickup_latitude")

st.markdown('Dropoff')
user_input5 = st.number_input("dropoff_longitude")
user_input6 = st.number_input("dropoff_latitude")

st.markdown('Passenger count')
user_input7 = st.number_input("Number of Passengers")


mydict = {
    'date': user_input1,
    'time': user_input2,
    'p_longitute': user_input3,
    'p_latitute': user_input4,
    'd_longitute': user_input5,
    'd_latitute': user_input6,
    'p_count': user_input7
}

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':
    x = requests.post(url, data=mydict)
    print(x.text)
