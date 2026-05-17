import streamlit as st
import pickle

# Page config
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# Custom CSS styling
st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}
.title {
    text-align: center;
    font-size: 40px;
    color: #00ffcc;
    font-weight: bold;
}
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 15px #00ffcc;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("car_price.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

# Title
st.markdown('<div class="title">🚗 Car Price Prediction App</div>', unsafe_allow_html=True)

st.write("---")

# Card UI
st.markdown('<div class="card">', unsafe_allow_html=True)

car_class = st.selectbox("🚘 Select Car Class", le.classes_)

mileage = st.number_input("⛽ Enter Mileage", min_value=0)

age = st.slider("📅 Select Car Age", 0, 7)

st.markdown("</div>", unsafe_allow_html=True)

# Button
if st.button("💰 Predict Price"):

    car_class_encoded = le.transform([car_class])[0]

    input_data = [[car_class_encoded, mileage, age]]

    predicted_price = model.predict(input_data)[0]

    st.success(f"💵 Estimated Price: ${predicted_price:,.2f}")
