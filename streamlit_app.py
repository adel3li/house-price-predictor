import streamlit as st
import sklearn
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestRegressor

# Load processed training data
train_data = pd.read_csv('./data/processed_train_df.csv')

# Train a simple RandomForestRegressor (replace this with your actual model training)
model = RandomForestRegressor()
features = train_data[['bedrooms', 'house_type_Detached', 'house_type_Semi-detached', 'house_type_Terraced',
                       'area', 'city_Poppleton', 'city_Riverford', 'city_Silvertown', 'city_Teasdale']]
target = train_data['sale_price']
model.fit(features, target)

# Streamlit App
st.title("Real Estate Price Prediction App")

# Sidebar with user input
st.header("User Input Features")

# Collect user input features
bedroom = st.slider("Bedrooms", min_value=1, max_value=10, value=5)
house_type = st.selectbox("House Type", ['Terraced', 'Semi-detached', 'Detached'])
area = st.slider("Area (sq.m.)", min_value=50, max_value=1000, value=200)
city = st.selectbox("City", ['Silvertown', 'Riverford', 'Teasdale', 'Poppleton'])

# Perform one-hot encoding for 'house_type' and 'city'
user_input = pd.DataFrame({
    'bedrooms': [bedroom],
    'house_type_Detached': [1 if house_type == 'Detached' else 0],
    'house_type_Semi-detached': [1 if house_type == 'Semi-detached' else 0],
    'house_type_Terraced': [1 if house_type == 'Terraced' else 0],
    'area': [area],
    'city_Poppleton': [1 if city == 'Poppleton' else 0],
    'city_Riverford': [1 if city == 'Riverford' else 0],
    'city_Silvertown': [1 if city == 'Silvertown' else 0],
    'city_Teasdale': [1 if city == 'Teasdale' else 0]
})

# Make prediction using the trained model
prediction = model.predict(user_input)

# Display the prediction
st.subheader("Predicted Sale Price:")
st.write(f"${prediction[0]:,.2f}")
