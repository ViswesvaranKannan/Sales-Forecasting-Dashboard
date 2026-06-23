import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(
    BASE_DIR,
    "data",
    "Sample - Superstore.csv"
)
model_path = os.path.join(
    BASE_DIR,
    "models",
    "sales_forecast_model.pkl"
)
st.set_page_config(page_title="Sales Forecast Dashboard", page_icon="📈", layout="wide")
st.markdown("""
<style>
.main {
    background-color: #F8FAFC;
}
div[data-testid="metric-container"] {
    background-color: white;
    border: 1px solid #E2E8F0;
    padding: 18px;
    border-radius: 15px;
    box-shadow: 0px 3px 8px rgba(0,0,0,0.05);
}
h1 {
    color: #1E293B;
}
</style>
""", unsafe_allow_html=True)
df = pd.read_csv(data_path, encoding="latin1")
df["Order Date"] = pd.to_datetime(df["Order Date"])
st.sidebar.title("📊 Dashboard Filters")
region = st.sidebar.selectbox("Region", ["All"] + sorted(df["Region"].unique()))
category = st.sidebar.selectbox("Category", ["All"] + sorted(df["Category"].unique()))
filtered_df = df.copy()
if region != "All": filtered_df = filtered_df[filtered_df["Region"] == region]
if category != "All": filtered_df = filtered_df[filtered_df["Category"] == category]
st.title("📈 Sales Forecasting Dashboard")
st.caption("Business Intelligence & Forecasting using Holt-Winters Exponential Smoothing")
st.markdown("---")
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
profit_margin = (total_profit / total_sales) * 100
col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("📈 Total Profit", f"${total_profit:,.0f}")
col3.metric("🛒 Orders", f"{total_orders:,}")
col4.metric("📊 Profit Margin", f"{profit_margin:.2f}%")
st.markdown("")
monthly_sales = (filtered_df.groupby(pd.Grouper(key="Order Date", freq="ME"))["Sales"].sum().reset_index())
monthly_profit = (filtered_df.groupby(pd.Grouper(key="Order Date", freq="ME"))["Profit"].sum().reset_index())
col1, col2 = st.columns(2)
with col1:
    st.subheader("📈 Monthly Sales Trend")
    fig = px.line(
        monthly_sales,
        x="Order Date",
        y="Sales"
    )
    fig.update_layout(
        height=350,
        margin=dict(l=10,r=10,t=30,b=10)
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )
with col2:
    st.subheader("💹 Monthly Profit Trend")
    fig = px.line(
        monthly_profit,
        x="Order Date",
        y="Profit"
    )
    fig.update_layout(
        height=350,
        margin=dict(l=10,r=10,t=30,b=10)
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )
col1, col2 = st.columns(2)
with col1:
    category_sales = (
        filtered_df.groupby("Category")
        ["Sales"]
        .sum()
        .reset_index()
    )
    fig = px.bar(
        category_sales,
        x="Category",
        y="Sales"
    )
    fig.update_layout(height=350)
    st.subheader("📦 Sales by Category")
    st.plotly_chart(
        fig,
        use_container_width=True
    )
with col2:
    region_sales = (
        filtered_df.groupby("Region")
        ["Sales"]
        .sum()
        .reset_index()
    )
    fig = px.bar(
        region_sales,
        x="Region",
        y="Sales"
    )
    fig.update_layout(height=350)
    st.subheader("🌎 Sales by Region")
    st.plotly_chart(
        fig,
        use_container_width=True
    )
top_states = (filtered_df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10).reset_index())
fig = px.bar(
    top_states,
    x="State",
    y="Sales"
)
fig.update_layout(height=350)
st.subheader("🏆 Top 10 States by Sales")
st.plotly_chart(
    fig,
    use_container_width=True
)
st.subheader("🔮 6-Month Sales Forecast")
forecast_model = joblib.load(model_path)
future_forecast = forecast_model.forecast(6)
forecast_df = pd.DataFrame({
    "Month": [
        "Month 1",
        "Month 2",
        "Month 3",
        "Month 4",
        "Month 5",
        "Month 6"
    ],
    "Forecast Sales": future_forecast
})
fig = px.line(
    forecast_df,
    x="Month",
    y="Forecast Sales",
    markers=True
)
fig.update_layout(
    height=400
)
st.plotly_chart(
    fig,
    use_container_width=True
)
st.info(
"""
Forecast generated using Holt-Winters Exponential Smoothing.
The model captures long-term trend and seasonality patterns
observed in historical sales data.
"""
)
st.subheader("💡 Business Insights")
st.markdown("""
✅ Technology generates the highest revenue.

✅ West region consistently leads total sales.

⚠️ Furniture contributes significant sales but lower profitability.

📈 Sales tend to peak during year-end periods.

🎯 Regional and category filters can be used to explore trends.
""")

st.markdown("---")
st.caption("Developed by Viswesvaran | Data Analytics & Forecasting Project")