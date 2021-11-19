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
user_input7 = st.number_input("Number of Passengers", min_value=1, max_value=8)


mydict = {
    'pickup_datetime': '2012-10-06 12:10:20',
    'pickup_longitude': user_input3,
    'pickup_latitude': user_input4,
    'dropoff_longitude': user_input5,
    'dropoff_latitude': user_input6,
    'passenger_count': user_input7
}

#url = 'https://taxifare.lewagon.ai/predict'
url = "https://taxifaremodel-olgxfxxy2a-ew.a.run.app/predict"

if url == "https://taxifaremodel-olgxfxxy2a-ew.a.run.app/predict":
    response = requests.get(url, params=mydict)
    prediction = response.json()
    st.markdown("""## Prediction""")
    st.markdown(prediction['prediction'])
