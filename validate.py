import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load the processed training and validation datasets
train_data = pd.read_csv("./data/processed_train_data.csv")
validation_data = pd.read_csv("./data/processed_validation_data.csv")

# Feature selection
features = ['bedrooms', 'house_type', 'area', 'city']

# Extract features and target variable from the training data
X_train = train_data[features]
y_train = train_data['sale_price']

# Create and fit the Random Forest Regressor model
model_compare = RandomForestRegressor(random_state=42)
model_compare.fit(X_train, y_train)

# Make predictions on the validation data
X_validation = validation_data[features]
compare_predictions = model_compare.predict(X_validation)

# Create a DataFrame with house_id and predicted price
compare_result = pd.DataFrame({'house_id': validation_data['house_id'], 'predicted_price': compare_predictions})

# Display the result
print(compare_result.head())

# Save the result to a CSV file
# compare_result.to_csv('compare_result.csv', index=False)
