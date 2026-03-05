
import streamlit as st
import requests

st.title("Prediction Dashboard")

x1 = st.number_input("Feature 1")
x2 = st.number_input("Feature 2")
x3 = st.number_input("Feature 3")

if st.button("Predict"):

    response = requests.get(
        f"http://localhost:8000/predict?x1={x1}&x2={x2}&x3={x3}"
    )

    st.write(response.json())
