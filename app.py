import streamlit as st
import pickle

# Page config
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# Navy Blue Theme CSS
st.markdown("""
<style>
body {
    background-color: #0b1f3a;
}

.main {
    background-color: #0b1f3a;
    color: white;
}

/* Title */
h1 {
    color: #38bdf8;
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}

/* Card style */
.stApp {
    background: linear-gradient(135deg, #0b1f3a, #102a4c);
}

/* Inputs */
.stSelectbox, .stNumberInput, .stSlider {
    color: white;
}

/* Button */
.stButton > button {
    background-color: #38bdf8;
    color: black;
    border-radius: 10px;
    padding: 10px;
    font-size: 16px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background-color: #0ea5e9;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("car_price.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

# Title
st.title("🚗 Car Price Prediction App")

st.write("---")

# Inputs
car_class = st.selectbox("🚘 Select Car Class", le.classes_)

mileage = st.number_input("⛽ Enter Mileage", min_value=0)

age = st.slider("📅 Select Car Age", 0, 7)

# Prediction
if st.button("💰 Predict Price"):

    car_class_encoded = le.transform([car_class])[0]

    input_data = [[car_class_encoded, mileage, age]]

    predicted_price = model.predict(input_data)[0]

    st.success(f"💵 Estimated Price: ${predicted_price:,.2f}")
