import streamlit as st
import requests
from datetime import datetime

'''
# Taxi Fare
'''

st.markdown("## Select the parameters for the ride:")

pickup_date = st.date_input("Pickup Date", value=datetime.now().date())
pickup_time = st.time_input("Pickup Time", value=datetime.now().time())
pickup_longitude = st.number_input("Pickup Longitude", format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", format="%.6f")
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=10, value=1)

pickup_datetime = f"{pickup_date} {pickup_time}"

url = 'https://taxifare.lewagon.ai/predict'

if st.button("Get Prediction"):
    # Build the dictionary to send to the API
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # Call the API using the `requests` package
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        prediction = response.json().get("fare", "Error: Prediction not found")

        # Display the prediction
        st.markdown(f"## Predicted Fare: **${prediction:.2f}**")

    except Exception as e:
        st.error(f"An error occurred: {e}")
