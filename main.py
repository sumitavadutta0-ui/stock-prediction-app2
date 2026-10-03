import streamlit as st

st.set_page_config(
    page_title="AlphaPredict: Stock Forecasting",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define pages using the modern st.Page routing API
home_page = st.Page("views/home.py", title="Market Overview", icon="🏢", default=True)
prediction_page = st.Page("views/prediction.py", title="TensorFlow AI Forecast", icon="🤖")
metrics_page = st.Page("views/metrics.py", title="Model Evaluation", icon="📊")

# Group pages into navigation blocks
pg = st.navigation({
    "Dashboard": [home_page],
    "Predictive AI Engine": [prediction_page, metrics_page]
})

# Universal sidebar element across all modules
st.sidebar.markdown("## 📈 AlphaPredict v1.0")
st.sidebar.markdown("Powered by **Streamlit** & **TensorFlow**")
st.sidebar.markdown("---")

pg.run()
