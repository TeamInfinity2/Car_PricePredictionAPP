import streamlit as st
import pickle

# Load files
try:
    model = pickle.load(open("car_price.pkl", "rb"))
    le = pickle.load(open("label_encoder.pkl", "rb"))
except Exception as e:
    st.error(f"Error loading model files: {e}")

st.title("🚗 Car Price Prediction App")

# Dropdown
car_class = st.selectbox(
    "Select Car Class",
    le.classes_
)

# Mileage
mileage = st.number_input(
    "Enter Car Mileage",
    min_value=0
)

# Age
age = st.slider(
    "Select Car Age",
    min_value=0,
    max_value=7
)

# Prediction
if st.button("Predict Price"):

    car_class_encoded = le.transform([car_class])[0]

    input_data = [[car_class_encoded, mileage, age]]

    predicted_price = model.predict(input_data)[0]

    st.success(
        f"Predicted Price: ${predicted_price:,.2f}"
    )
