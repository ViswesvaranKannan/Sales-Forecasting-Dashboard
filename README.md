

##  Sales Forecasting Dashboard
An end-to-end Business Intelligence and Sales Forecasting project built using Python, Time Series
Forecasting, and Streamlit.
The project analyzes historical sales data from a retail superstore, identifies business trends, evaluates
multiple forecasting models, and provides future sales predictions through an interactive dashboard.
##  Project Overview
Businesses rely on sales forecasting to make informed decisions regarding inventory, marketing,
budgeting, and resource allocation.
This project aims to:
Analyze historical sales performance
Discover key business insights
Compare multiple forecasting approaches
Predict future sales using time-series forecasting
Visualize business KPIs through an interactive dashboard
##  Business Problem
Retail businesses often struggle to estimate future sales accurately due to seasonality, market
fluctuations, and changing customer demand.
The goal of this project is to:
Understand historical sales patterns
Identify high-performing categories and regions
Forecast future sales trends
Support data-driven business decisions
##  Dataset
## Dataset: Superstore Sales Dataset
The dataset contains:
## Customer Information
## Product Information
## Regional Sales Data
## Profit Metrics
## Discounts
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## 1

## Order Details
## Dataset Summary
MetricValue
## Records9,994
## Features21
## Total Sales$2.29 Million
Total Profit$286K
## Total Orders5,009
## ️ Technologies Used
## Programming Language
## Python
## Data Analysis
## Pandas
NumPy
## Data Visualization
## Matplotlib
## Plotly
## Machine Learning & Forecasting
Scikit-Learn
## Statsmodels
## Prophet
## Dashboard
## Streamlit
##  Project Structure
Sales-Forecasting-Dashboard/
## │
├── app/
│   └── streamlit_app.py
## │
├── data/
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## 2

## │   └── Sample - Superstore.csv
## │
├── models/
│   └── sales_forecast_model.pkl
## │
├── notebooks/
│   └── sales_forecasting.ipynb
## │
├── README.md
## │
├── requirements.txt
## │
## └── .streamlit/
└── config.toml
##  Exploratory Data Analysis
Several business questions were answered through EDA:
Sales by Category
CategorySales
TechnologyHighest
FurnitureSecond
Office SuppliesThird
Profit by Category
Technology generated the highest profit.
Furniture generated strong revenue but significantly lower profit margins.
## Regional Analysis
Top performing regions:
## West
## East
## Central
## South
## State Analysis
Top sales-generating states:
## California
## 1.
## 2.
## 3.
## 4.
## •
## 3

## New York
## Texas
## Washington
## Pennsylvania
## Monthly Trends
Sales displayed:
Seasonal fluctuations
Year-end sales spikes
Consistent growth trends
## 烙 Forecasting Models Evaluated
Multiple forecasting models were compared.
- Linear Regression (Baseline Model)
## Features:
## Month Number
## Results:
MetricValue
## MAE25,585
## R² Score-0.89
## Observation
Linear Regression failed to capture seasonality and produced poor forecasting performance.
## 2. Prophet Forecasting
## Results:
MetricValue
## MAE15,165
## R² Score0.30
## Observation
Prophet improved forecasting accuracy but was slightly less effective than Holt-Winters for this dataset.
## •
## •
## •
## •
## •
## •
## •
## •
## 4

- Holt-Winters Exponential Smoothing
## Results:
MetricValue
## MAE14,333
## R² Score0.34
## Observation
Holt-Winters achieved the lowest forecasting error and highest predictive performance.
##  Final Model Selection
## Selected Model
Holt-Winters Exponential Smoothing
## Reasons:
Lowest MAE
## Highest R² Score
Captures trend and seasonality effectively
Performs well on limited monthly observations
##  Dashboard Features
KPI Monitoring
## Total Sales
## Total Profit
## Total Orders
## Profit Margin
## Interactive Visualizations
## Monthly Sales Trend
## Monthly Profit Trend
Sales by Category
Sales by Region
Top 10 States by Sales
## Forecasting
## Next 6 Months Sales Forecast
Holt-Winters Forecast Visualization
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## 5

## Business Intelligence
## Revenue Insights
## Profitability Analysis
## Regional Performance Analysis
## Strategic Recommendations
## Filters
## Region Filter
## Category Filter
##  Key Business Insights
## Revenue Leader
Technology generated the highest overall revenue.
## Most Profitable Category
Technology also produced the highest profits.
## Profitability Concern
Furniture generated significant sales volume but comparatively low profit margins.
## Strongest Market
The West region contributed the largest share of total sales.
## Sales Seasonality
Sales consistently peaked during year-end periods, indicating seasonal purchasing behavior.
##  Dashboard Preview
Add screenshots here after deployment.
dashboard_screenshot.png
##  Future Improvements
Potential enhancements:
Deploy dashboard publicly
## •
## •
## •
## •
## •
## •
## •
## 6

Add forecasting confidence intervals
Implement XGBoost forecasting
Real-time data integration
Advanced customer segmentation
Automated report generation
## 易 Skills Demonstrated
## Data Analysis
## Data Cleaning
## Exploratory Data Analysis
KPI Development
## Business Insights
## Machine Learning
## Time Series Forecasting
## Model Evaluation
## Feature Engineering
## Model Comparison
## Visualization
## Plotly Dashboards
## Interactive Charts
## Business Reporting
## Deployment
## Streamlit Application Development
## Dashboard Design
## Model Integration
##  Results Summary
ModelMAER² Score
## Linear Regression25,585-0.89
## Prophet15,1650.30
Holt-Winters14,3330.34
## Final Model
✅ Holt-Winters Exponential Smoothing
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## •
## 7

## ‍ Author
## Viswesvaran Kannan
Aspiring AI Engineer | Data Analyst
## Connect
GitHub: https://github.com/ViswesvaranKannan
LinkedIn: www.linkedin.com/in/viswesvaran-kannan-97b8b02a2
## •
## •
## 8