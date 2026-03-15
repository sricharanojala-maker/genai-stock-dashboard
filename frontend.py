# frontend.py

import streamlit as st
import plotly.graph_objects as go

# Import functions from backend
from backend import get_price_data, get_current_price, get_sentiment_score, get_trend_strength

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="GenAI Stock Intelligence Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📊 Generative AI – Sales & Market Intelligence Dashboard")

# ---------------------------
# Sidebar Inputs
# ---------------------------
st.sidebar.header("User Input")

ticker = st.sidebar.text_input("Enter Ticker Symbol", "AAPL")

sector = st.sidebar.selectbox(
    "Select Sector",
    ["Technology", "Healthcare", "Finance", "Energy", "Consumer Goods"]
)

st.sidebar.write("Selected Sector:", sector)

# ---------------------------
# Fetch Data from Backend
# ---------------------------
price_data = get_price_data(ticker)
current_price = get_current_price(ticker)
sentiment_score = get_sentiment_score(ticker)
trend_strength = get_trend_strength(price_data)

# ---------------------------
# Price Trend Chart
# ---------------------------
st.subheader("📈 Price Trend")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=price_data["Date"],
        y=price_data["Close"],
        mode="lines",
        name="Price"
    )
)

fig.update_layout(
    title=f"{ticker} Price Trend",
    xaxis_title="Date",
    yaxis_title="Price",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# Metric Cards
# ---------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Current Price",
        value=f"${current_price}"
    )

with col2:
    st.metric(
        label="Sentiment Score",
        value=sentiment_score
    )

with col3:
    st.metric(
        label="Trend Strength",
        value=trend_strength
    )

# ---------------------------
# Recommendation Section
# ---------------------------
st.subheader("🤖 Recommendation")

if trend_strength > 0:
    st.success("Positive trend detected. This stock shows upward momentum.")
else:
    st.warning("Negative trend detected. Consider analyzing risks before investing.")