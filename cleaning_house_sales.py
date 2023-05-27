import pandas as pd
import math

# Load the dataset
house_sales = pd.read_csv('./data/house_sales.csv')

# Replace values in 'city' and 'house_type'
house_sales['city'].replace('--', 'Unknown', inplace=True)
house_sales['house_type'].replace({'Terr.': 'Terraced', 'Semi': 'Semi-detached', 'Det.': 'Detached'}, inplace=True)

# Fill missing values in 'months_listed' with the mean and round to the nearest tenth
house_sales["months_listed"].fillna(house_sales["months_listed"].mean(), inplace=True)
house_sales["months_listed"] = house_sales["months_listed"].apply(lambda x: round(x, 1))

# Create a clean DataFrame
clean_house_sales = house_sales.copy()

# Display the clean DataFrame
print(clean_house_sales)

# Save the clean DataFrame to a new CSV file in the same directory
clean_house_sales.to_csv('./data/cleaned_house_sales.csv', index=False)
