# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the training and validation datasets
train_data = pd.read_csv("./data/train_data.csv")
validation_data = pd.read_csv("./data/validation_data.csv")

# Feature selection
features = ['bedrooms', 'house_type', 'area', 'city']

# Extract features and target variable from the training data
X_train = train_data[features]
y_train = train_data['sale_price']

# Define a transformer for one-hot encoding the 'house_type' column
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), ['house_type']),
        ('dog', OneHotEncoder(), ['city'])
    ],
    remainder='passthrough'
)

# Create a pipeline with the preprocessor and the linear regression model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Fit the model
model.fit(X_train, y_train)

# Make predictions on the validation data
X_validation = validation_data[features]
base_predictions = model.predict(X_validation)

# Create a dataframe with house_id and predicted price
base_result = pd.DataFrame({'house_id': validation_data['house_id'], 'price': base_predictions})

# Display the result
print(base_result.head())
