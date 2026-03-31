import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st

# Load dataset
st.title("Linear Regression Implementation")
st.write("Loading dataset...")
data = sns.load_dataset('tips')

# Display dataset
st.write("Dataset Preview:")
st.write(data.head())

# Select features and target
st.write("Selecting features and target...")
X = data[['total_bill']]
y = data['tip']

# Split dataset into training and testing sets
st.write("Splitting dataset...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply Linear Regression
st.write("Applying Linear Regression...")
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
st.write("Making predictions...")
y_pred = model.predict(X_test)

# Results
st.write("Results:")
st.write(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")
st.write(f"R-squared Score: {r2_score(y_test, y_pred):.2f}")

# Display coefficients
st.write("Model Coefficients:")
st.write(f"Intercept: {model.intercept_:.2f}")
st.write(f"Coefficient: {model.coef_[0]:.2f}")

# Visualization
st.write("Visualization:")
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Linear Regression: Total Bill vs Tip')
plt.legend()
st.pyplot(plt)