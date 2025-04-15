import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

# Set MLflow tracking URI and experiment name
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("Default")  # Make sure it matches what you see in the MLflow UI

# Generate dummy dataset
X = np.random.rand(100, 1)
y = 3 * X.squeeze() + 2 + np.random.randn(100) * 0.1

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Start MLflow experiment
with mlflow.start_run():
    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)

    mlflow.log_param("fit_intercept", model.fit_intercept)
    mlflow.log_metric("mse", mse)
    mlflow.sklearn.log_model(model, "linear_model")

    print(f"Logged model and MSE: {mse:.4f}")

