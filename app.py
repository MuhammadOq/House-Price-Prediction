import streamlit as st
import pickle
with open("housing.pkl",mode='rb') as f:
    model = pickle.load(f)
st.title('House Price Prediction')

area = st.number_input("Area (in sq.ft)", min_value=100, max_value=10000, value=1000)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
stories = st.number_input("Stories", min_value=1, max_value=5, value=1)
parking = st.number_input("Parking spots", min_value=0, max_value=5, value=1)

# Categorical inputs (beginner-friendly)
mainroad = st.selectbox("Main Road?", ["Yes", "No"])
guestroom = st.selectbox("Guest Room?", ["Yes", "No"])
basement = st.selectbox("Basement?", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating?", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning?", ["Yes", "No"])
prefarea = st.selectbox("Preferred Area?", ["Yes", "No"])
furnishingstatus = st.selectbox("Furnishing Status", ["Unfurnished", "Semi-Furnished", "Furnished"])

# Convert Yes/No to 1/0
binary_map = {"Yes": 1, "No": 0}
mainroad = binary_map[mainroad]
guestroom = binary_map[guestroom]
basement = binary_map[basement]
hotwaterheating = binary_map[hotwaterheating]
airconditioning = binary_map[airconditioning]
prefarea = binary_map[prefarea]

# Furnishing status to numeric
furnishing_map = {"Unfurnished": 0, "Semi-Furnished": 1, "Furnished": 2}
furnishingstatus = furnishing_map[furnishingstatus]

# Predict
if st.button("Predict Price"):
    price_predicted = model.predict([[area, bedrooms, bathrooms, stories,
                                  mainroad, guestroom, basement, hotwaterheating,
                                  airconditioning, parking, prefarea, furnishingstatus]])

    st.success(f"Predicted House Price: {price_predicted[0]:.2f}")
