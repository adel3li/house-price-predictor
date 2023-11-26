import pandas as pd
from datetime import datetime

# Sample training data
train_data = pd.read_csv("./data/train_data.csv")

# Sample validation data
validation_data = pd.read_csv("./data/validation_data.csv")

# Step 1: Convert 'sale_date' to a consistent format
train_data['sale_date'] = pd.to_datetime(train_data['sale_date']).dt.strftime('%m/%d/%Y')
validation_data['sale_date'] = pd.to_datetime(validation_data['sale_date']).dt.strftime('%m/%d/%Y')

# Step 2: Extract 'year' and 'month' from 'sale_date' in validation data
validation_data['sale_year'] = pd.to_datetime(validation_data['sale_date']).dt.year
validation_data['sale_month'] = pd.to_datetime(validation_data['sale_date']).dt.month

# Step 3: Perform one-hot encoding for 'house_type' and 'city'
train_data = pd.get_dummies(train_data, columns=['house_type', 'city'])
validation_data = pd.get_dummies(validation_data, columns=['house_type', 'city'])

# Step 4: Create DataFrames for training and validation data
train_features = train_data[['bedrooms', 'house_type_Detached', 'house_type_Semi-detached', 'house_type_Terraced',
                             'area', 'city_Poppleton', 'city_Riverford', 'city_Silvertown', 'city_Teasdale']]
train_target = train_data['sale_price']

validation_features = validation_data[['bedrooms', 'house_type_Detached', 'house_type_Semi-detached', 'house_type_Terraced',
                                       'area', 'city_Poppleton', 'city_Riverford', 'city_Silvertown', 'city_Teasdale',
                                       'sale_year', 'sale_month']]

# Save processed training data to a new CSV file
train_data.to_csv('./data/processed_train_df.csv', index=False)

# Save processed validation data to a new CSV file
validation_data.to_csv('./data/processed_validation_df.csv', index=False)

# Now you can use these features in your streamlit app code
