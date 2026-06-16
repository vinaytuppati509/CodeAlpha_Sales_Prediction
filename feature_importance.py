import pandas as pd
import matplotlib.pyplot as plt
import joblib

model = joblib.load("sales_model.pkl")

features = ["TV", "Radio", "Newspaper"]

importance = model.feature_importances_

plt.figure(figsize=(8,5))

bars = plt.barh(features, importance)

plt.title("Feature Importance")

for bar in bars:
    width = bar.get_width()
    plt.text(
        width,
        bar.get_y() + bar.get_height()/2,
        f"{width:.3f}"
    )

plt.savefig("screenshots/feature_importance.png")
plt.show()

print("Feature Importance Saved!")