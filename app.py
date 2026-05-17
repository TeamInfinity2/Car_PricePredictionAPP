import streamlit as st
import pickle


model = pickle.load(open("car_price.pkl", "rb"))
le = pickle.load(open("label_encoder.pkl", "rb"))

st.title("Car Price Prediction App")

##selection dropdown for car classes(SUV, Sedan, etc.)
car_class = st.selectbox("Select Car Class", le.classes_)


#uer input for car mileage
mileage = st.number_input("Enter Car Mileage (in miles)", min_value=0)

age =st.slider("Select Car Age (in years)", min_value=0, max_value=7)
#user input for car year
# year = st.number_input("Enter Car Year", min_value=1900, max_value=2024)    
if st.button("Predict Price"):
    # Encode the selected car class
    car_class_encoded = le.transform([car_class])[0]
    
    # Prepare the input data for prediction
    input_data = [[car_class_encoded, mileage, age]]
    
    # Make the prediction using the loaded model
    predicted_price = model.predict(input_data)[0]
    
    st.success(f"The predicted price of the car is: ${predicted_price:.2f}")
