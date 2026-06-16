import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# Load Dataset
df = pd.read_csv("Advertising.csv")

# Remove unwanted column
df.drop("Unnamed: 0", axis=1, inplace=True)

# Features & Target
X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

# Random Forest
rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

# Metrics
print("\nLinear Regression")
print("R2 Score :", round(r2_score(y_test, lr_pred), 4))
print("MAE      :", round(mean_absolute_error(y_test, lr_pred), 4))

print("\nRandom Forest")
print("R2 Score :", round(r2_score(y_test, rf_pred), 4))
print("MAE      :", round(mean_absolute_error(y_test, rf_pred), 4))

# Save Best Model
joblib.dump(rf, "sales_model.pkl")

print("\nModel Saved Successfully!")
print("File Created: sales_model.pkl")