import streamlit as st
import pickle
import numpy as np
import os

# Get the folder where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build the full path to model_pickle
model_path = os.path.join(BASE_DIR, "model_pickle")

# Load model
with open(model_path, "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

st.title("🏠 House Price Prediction App")

st.write("Enter the house details below.")

area = st.number_input("Area (sq ft)", min_value=100, step=50)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=20, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=20, step=1)

if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted House Price: ₹{prediction:,.2f}")
