import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Current script folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create screenshots folder
screenshots_dir = os.path.join(BASE_DIR, "screenshots")
os.makedirs(screenshots_dir, exist_ok=True)

# Load dataset
df = pd.read_csv(os.path.join(BASE_DIR, "Advertising.csv"))

# Drop unwanted column
df.drop("Unnamed: 0", axis=1, inplace=True)

# Correlation Matrix
corr = df.corr()

# Plot Heatmap
plt.figure(figsize=(8, 6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Sales Prediction Correlation Heatmap")
plt.tight_layout()

# Save image
save_path = os.path.join(screenshots_dir, "heatmap.png")
plt.savefig(save_path)

plt.show()

print(f"Heatmap saved at: {save_path}")