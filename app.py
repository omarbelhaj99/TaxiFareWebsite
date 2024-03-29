import streamlit as st
import numpy as np
import pandas as pd
import requests
'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
data_and_time = st.text_input("data and time", 0)
pickup_longitude = st.text_input("pickup longitude",0 )
pickup_latitude = st.text_input("pickup latitude", 0)
dropoff_longitude = st.text_input("dropoff longitude",0 )
dropoff_latitude = st.text_input("dropoff latitude", 0)
passenger_count = st.text_input("passenger count",0)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'

    )
'''

2. Let's build a dictionary containing the parameters for our API...

'''
X = {
    'data and time': data_and_time,
    'pickup latitude': pickup_latitude,
    'pickup longitude': pickup_longitude,
    'dropoff longitude': dropoff_longitude,
    'dropoff latitude': dropoff_latitude,
    'passenger count': passenger_count,
}
'''
3. Let's call our API using the `requests` package...
'''
response = requests.get(url, params=query)
'''
4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
st.markdown('''response.json()''')
