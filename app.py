import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Sales Prediction System",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("sales_model.pkl")

# -----------------------------
# Header
# -----------------------------
st.title("📈 Sales Prediction System")

st.markdown("""
## AI Powered Sales Forecasting

Predict product sales based on advertising budgets.

Enter TV, Radio and Newspaper advertising budgets from the sidebar.
""")

# -----------------------------
# Metrics
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="R² Score",
        value="98.13%"
    )

with col2:
    st.metric(
        label="MAE",
        value="0.62"
    )

st.divider()

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("📊 Advertising Budget")

tv_budget = st.sidebar.slider(
    "TV Budget",
    min_value=0.0,
    max_value=300.0,
    value=100.0
)

radio_budget = st.sidebar.slider(
    "Radio Budget",
    min_value=0.0,
    max_value=50.0,
    value=20.0
)

newspaper_budget = st.sidebar.slider(
    "Newspaper Budget",
    min_value=0.0,
    max_value=120.0,
    value=30.0
)

# -----------------------------
# Create Input Data
# -----------------------------
input_data = pd.DataFrame(
    [[tv_budget, radio_budget, newspaper_budget]],
    columns=["TV", "Radio", "Newspaper"]
)

# -----------------------------
# Prediction History
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# Prediction Button
# -----------------------------
if st.button(
    "📈 Predict Sales",
    use_container_width=True
):

    prediction = model.predict(input_data)[0]

    st.success(
        f"🎯 Predicted Sales: {prediction:.2f}"
    )

    st.session_state.history.append({
        "TV Budget": tv_budget,
        "Radio Budget": radio_budget,
        "Newspaper Budget": newspaper_budget,
        "Predicted Sales": round(prediction, 2)
    })

    st.balloons()

# -----------------------------
# Prediction History
# -----------------------------
if len(st.session_state.history) > 0:

    st.divider()

    st.subheader("📜 Prediction History")

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

# -----------------------------
# Visualizations
# -----------------------------
st.divider()

st.header("📊 Model Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.image(
        "screenshots/heatmap.png",
        caption="Correlation Heatmap",
        use_container_width=True
    )

with col2:
    st.image(
        "screenshots/feature_importance.png",
        caption="Feature Importance",
        use_container_width=True
    )

# Model Comparison
st.image(
    "screenshots/model_comparison.png",
    caption="Model Comparison",
    use_container_width=True
)

# -----------------------------
# Insights Box
# -----------------------------
st.divider()

st.subheader("📌 Insights")

st.info("""
📺 TV advertising has the strongest impact on Sales.

📻 Radio advertising positively influences sales performance.

📰 Newspaper advertising contributes less compared to TV and Radio.

🌲 Random Forest achieved the highest prediction accuracy.

🎯 Model Accuracy (R² Score): 98.13%

📉 Mean Absolute Error (MAE): 0.62
""")

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "Built with ❤️ using Python, Scikit-Learn, Joblib and Streamlit"
)