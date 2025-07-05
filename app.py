import pandas as pd
import numpy as np
import pickle
import joblib
import streamlit as st
model = joblib.load('pollution_model.pkl')
model_cols = joblib.load('model_columns.pkl')
st.title("Water Pollutants Predictor")
st.write("Predicts the  water pollutants based on Year and Station ID")
year_input =st.number_input("Enter Year",min_value=2022,max_value=2100,value=2022)
station_id = st.text_input("Enter Station ID",value='1')
if st.button("predict"):
    if not station_id:
        st.warning("Please enter a valid Station ID")
    else:
        input_df = pd.DataFrame({'year':[year_input], 'id':[station_id]})
        input_encoded = pd.get_dummies(input_df, columns=['id'])

        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[model_cols]   
        predicted_pollutants = model.predict(input_encoded)[0]
        pollutants=['O2','NO3','NO2','SO4','PO4','CL']
        st.subheader(f"Predicted Pollutants for station {station_id} in year {year_input}:")
        predicted_values={}
        for p, val in zip(pollutants, predicted_pollutants):
            st.write(f"{p}: {val:.2f}")