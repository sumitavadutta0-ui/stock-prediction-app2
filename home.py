import streamlit as st
import pandas as pd
import numpy as np

st.title("🏢 Market Overview Dashboard")
st.markdown("Real-time summary tracking framework for target stock assets.")

# Target stock tickers metadata
STOCKS = {
    "AAPL": {"name": "Apple Inc.", "current": 185.92, "change": "+1.24%"},
    "GOOGL": {"name": "Alphabet Inc.", "current": 174.45, "change": "-0.58%"},
    "RELIANCE.NS": {"name": "Reliance Industries Ltd.", "current": 2450.10, "change": "+2.15%"}
}

cols = st.columns(3)
for col, (ticker, info) in zip(cols, STOCKS.items()):
    with col:
        st.metric(label=f"{info['name']} ({ticker})", value=f"${info['current']}" if "NS" not in ticker else f"₹{info['current']}", delta=info['change'])

st.markdown("---")
st.subheader("Historical Context Pipeline (Placeholder Mockup Data)")
selected_stock = st.selectbox("Select Asset Context", list(STOCKS.keys()))

# Generate baseline mockup chart data
dates = pd.date_range(end="2026-10-04", periods=100)
base_val = 150 if "RELIANCE" not in selected_stock else 2300
mock_history = pd.DataFrame({
    "Date": dates,
    "Close Price": base_val + np.cumsum(np.random.normal(0.5, 2, 100))
}).set_index("Date")

st.line_chart(mock_history)
