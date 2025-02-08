import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
import pickle

# Load the dataset
file_path = "pocketplanner_dataset.csv"
df = pd.read_csv(file_path)

# Handle missing values (if any)
df = df.fillna(df.mean())  # Fills NaN values with the column-wise mean

# Define features (X) and target variables (y)
X = df[['Monthly Budget', 'Saving Goal']].values
y = df[['Food', 'Electronics', 'Online Shopping', 'Monthly Bill', 'Groceries', 'Transport', 'Housing', 'Miscellaneous']].values

# Feature Scaling (Standardization)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Add a column of ones to X for the intercept term (bias)
X_scaled = np.c_[np.ones(X_scaled.shape[0]), X_scaled]

# Split dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Linear Regression Model (Gradient Descent)
class LinearRegressionModel:
    def __init__(self, learning_rate=0.001, iterations=500000, alpha=0.1):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.alpha = alpha  # Regularization strength
        self.theta = None
    
    def fit(self, X, y):
        m, n = X.shape
        self.theta = np.random.randn(n, y.shape[1]) * 0.01  # Initialize with small random values
        
        for i in range(self.iterations):
            predictions = X.dot(self.theta)  # Linear model prediction
            errors = predictions - y
            gradient = (1/m) * X.T.dot(errors)  # Compute gradient

            # Regularization term (L2)
            gradient += (self.alpha / m) * self.theta
            
            # Monitor gradient magnitude
            gradient_magnitude = np.linalg.norm(gradient)
            if gradient_magnitude > 50000:  # Adjust this threshold as necessary
                print(f"Warning: Gradient explosion detected (iteration {i})")
                break  # Stop training if gradient is too large
            
            self.theta -= self.learning_rate * gradient  # Update theta
    
    def predict(self, X):
        return X.dot(self.theta)

# Initialize the model with a smaller learning rate and L2 regularization
model = LinearRegressionModel(learning_rate=0.0001, iterations=500000, alpha=0.1)

# Train the model
model.fit(X_train, y_train)

# Predict the target values on the test set
y_pred = model.predict(X_test)


# Save the model to a .pkl file
with open('linear_regression_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved as 'linear_regression_model.pkl'")
