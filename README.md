# 📈 Sales Forecasting Dashboard

An end-to-end Business Intelligence and Sales Forecasting project built using Python, Time Series Forecasting, and Streamlit.

The project analyzes historical sales data from a retail superstore, identifies business trends, evaluates multiple forecasting models, and provides future sales predictions through an interactive dashboard.

---

## 🚀 Project Overview

Businesses rely on sales forecasting to make informed decisions regarding inventory, marketing, budgeting, and resource allocation.

This project aims to:

* Analyze historical sales performance
* Discover key business insights
* Compare multiple forecasting approaches
* Predict future sales using time-series forecasting
* Visualize business KPIs through an interactive dashboard

---

## 🎯 Business Problem

Retail businesses often struggle to estimate future sales accurately due to seasonality, market fluctuations, and changing customer demand.

The goal of this project is to:

* Understand historical sales patterns
* Identify high-performing categories and regions
* Forecast future sales trends
* Support data-driven business decisions

---

## 📊 Dataset

**Dataset:** Superstore Sales Dataset

The dataset contains:

* Customer Information
* Product Information
* Regional Sales Data
* Profit Metrics
* Discounts
* Order Details

### Dataset Summary

| Metric       | Value         |
| ------------ | ------------- |
| Records      | 9,994         |
| Features     | 21            |
| Total Sales  | $2.29 Million |
| Total Profit | $286K         |
| Total Orders | 5,009         |

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Plotly

### Machine Learning & Forecasting

* Scikit-Learn
* Statsmodels
* Prophet

### Dashboard

* Streamlit

---

## 📂 Project Structure

```text
Sales-Forecasting-Dashboard/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   └── Sample - Superstore.csv
│
├── models/
│   └── sales_forecast_model.pkl
│
├── notebooks/
│   └── sales_forecasting.ipynb
│
├── README.md
│
├── requirements.txt
│
└── .streamlit/
    └── config.toml
```

---

## 📈 Exploratory Data Analysis

Several business questions were answered through EDA:

### Sales by Category

| Category        | Sales   |
| --------------- | ------- |
| Technology      | Highest |
| Furniture       | Second  |
| Office Supplies | Third   |

### Profit by Category

Technology generated the highest profit.

Furniture generated strong revenue but significantly lower profit margins.

### Regional Analysis

Top performing regions:

1. West
2. East
3. Central
4. South

### State Analysis

Top sales-generating states:

* California
* New York
* Texas
* Washington
* Pennsylvania

### Monthly Trends

Sales displayed:

* Seasonal fluctuations
* Year-end sales spikes
* Consistent growth trends

---

## 🤖 Forecasting Models Evaluated

Multiple forecasting models were compared.

### 1. Linear Regression (Baseline Model)

Features:

* Month Number

Results:

| Metric   | Value  |
| -------- | ------ |
| MAE      | 25,585 |
| R² Score | -0.89  |

#### Observation

Linear Regression failed to capture seasonality and produced poor forecasting performance.

---

### 2. Prophet Forecasting

Results:

| Metric   | Value  |
| -------- | ------ |
| MAE      | 15,165 |
| R² Score | 0.30   |

#### Observation

Prophet improved forecasting accuracy but was slightly less effective than Holt-Winters for this dataset.

---

### 3. Holt-Winters Exponential Smoothing

Results:

| Metric   | Value  |
| -------- | ------ |
| MAE      | 14,333 |
| R² Score | 0.34   |

#### Observation

Holt-Winters achieved the lowest forecasting error and highest predictive performance.

---

## 🏆 Final Model Selection

### Selected Model

**Holt-Winters Exponential Smoothing**

Reasons:

* Lowest MAE
* Highest R² Score
* Captures trend and seasonality effectively
* Performs well on limited monthly observations

---

## 📊 Dashboard Features

### KPI Monitoring

* Total Sales
* Total Profit
* Total Orders
* Profit Margin

### Interactive Visualizations

* Monthly Sales Trend
* Monthly Profit Trend
* Sales by Category
* Sales by Region
* Top 10 States by Sales

### Forecasting

* Next 6 Months Sales Forecast
* Holt-Winters Forecast Visualization

### Business Intelligence

* Revenue Insights
* Profitability Analysis
* Regional Performance Analysis
* Strategic Recommendations

### Filters

* Region Filter
* Category Filter

---

## 💡 Key Business Insights

### Revenue Leader

Technology generated the highest overall revenue.

### Most Profitable Category

Technology also produced the highest profits.

### Profitability Concern

Furniture generated significant sales volume but comparatively low profit margins.

### Strongest Market

The West region contributed the largest share of total sales.

### Sales Seasonality

Sales consistently peaked during year-end periods, indicating seasonal purchasing behavior.

---

## 📷 Dashboard Preview

Add screenshots here after deployment.

```text
dashboard_screenshot.png
```

---

## 🔮 Future Improvements

Potential enhancements:

* Deploy dashboard publicly
* Add forecasting confidence intervals
* Implement XGBoost forecasting
* Real-time data integration
* Advanced customer segmentation
* Automated report generation

---

## 🧠 Skills Demonstrated

### Data Analysis

* Data Cleaning
* Exploratory Data Analysis
* KPI Development
* Business Insights

### Machine Learning

* Time Series Forecasting
* Model Evaluation
* Feature Engineering
* Model Comparison

### Visualization

* Plotly Dashboards
* Interactive Charts
* Business Reporting

### Deployment

* Streamlit Application Development
* Dashboard Design
* Model Integration

---

## 📌 Results Summary

| Model             | MAE    | R² Score |
| ----------------- | ------ | -------- |
| Linear Regression | 25,585 | -0.89    |
| Prophet           | 15,165 | 0.30     |
| Holt-Winters      | 14,333 | 0.34     |

### Final Model

✅ Holt-Winters Exponential Smoothing

---

## 👨‍💻 Author

**Viswesvaran Kannan**

Aspiring AI Engineer | Data Analyst

### Connect

* GitHub: https://github.com/ViswesvaranKannan
* LinkedIn: [www.linkedin.com/in/viswesvaran-kannan-97b8b02a2](http://www.linkedin.com/in/viswesvaran-kannan-97b8b02a2)

---
