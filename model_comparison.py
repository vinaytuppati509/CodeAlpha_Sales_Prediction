import matplotlib.pyplot as plt

models = ["Linear Regression", "Random Forest"]
scores = [0.8994, 0.9813]

plt.figure(figsize=(8,5))

bars = plt.bar(models, scores)

plt.title("Model Comparison")
plt.ylabel("R2 Score")

for bar in bars:
    y = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        y,
        f"{y:.3f}",
        ha="center"
    )

plt.savefig("screenshots/model_comparison.png")
plt.show()

print("Model Comparison Saved!")