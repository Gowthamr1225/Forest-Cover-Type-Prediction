import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("final.pkl", "rb") as f:   # replace with your actual model file name
    model = pickle.load(f)

# Load label encoder
with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

st.title("🌲:red[Forest Cover Type Prediction]")

st.header(":blue[Enter the values for the following features to predict the forest cover type:]")

# Collecting user inputs
Elevation = st.number_input("Elevation", min_value=0, max_value=5000, value=2000)
Horizontal_Distance_To_Roadways = st.number_input("Horizontal Distance To Roadways", min_value=0, max_value=10000, value=500)
Horizontal_Distance_To_Fire_Points = st.number_input("Horizontal Distance To Fire Points", min_value=0, max_value=10000, value=600)
Horizontal_Distance_To_Hydrology = st.number_input("Horizontal Distance To Hydrology", min_value=0, max_value=10000, value=300)
Vertical_Distance_To_Hydrology = st.number_input("Vertical Distance To Hydrology", min_value=-1000, max_value=1000, value=50)
Wilderness_Area_1 = st.selectbox("Wilderness Area 1", [0, 1])
Wilderness_Area_4 = st.selectbox("Wilderness Area 4", [0, 1])
Hillshade_9am = st.slider("Hillshade 9am", min_value=0, max_value=255, value=150)
Aspect = st.slider("Aspect", min_value=0, max_value=360, value=90)
Hillshade_3pm = st.slider("Hillshade 3pm", min_value=0, max_value=255, value=100)
Hillshade_Noon = st.slider("Hillshade Noon", min_value=0, max_value=255, value=200)
Slope = st.slider("Slope", min_value=0, max_value=90, value=10)
Wilderness_Area_3 = st.selectbox("Wilderness Area 3", [0, 1])
Soil_Type_10 = st.selectbox("Soil Type 10", [0, 1])
Soil_Type_3 = st.selectbox("Soil Type 3", [0, 1])

# Arrange inputs into feature vector
features = np.array([[
    Elevation,
    Horizontal_Distance_To_Roadways,
    Horizontal_Distance_To_Fire_Points,
    Horizontal_Distance_To_Hydrology,
    Vertical_Distance_To_Hydrology,
    Wilderness_Area_1,
    Wilderness_Area_4,
    Hillshade_9am,
    Aspect,
    Hillshade_3pm,
    Hillshade_Noon,
    Slope,
    Wilderness_Area_3,
    Soil_Type_10,
    Soil_Type_3
]])

# Predict
if st.button("Predict Forest Cover Type"):
    prediction_encoded = model.predict(features)  # This gives encoded number
    prediction_label = label_encoder.inverse_transform(prediction_encoded)  # Convert back to class name
    st.success(f"🌳 Predicted Forest Cover Type: **{prediction_label[0]}**")