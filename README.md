# Interactive Market Data Dashboard

This is a simple web application that displays an interactive dashboard for a given stock ticker. The dashboard includes a price chart, key financial statistics, and common technical indicators like RSI and MACD.

This project demonstrates skills in API integration, data visualization, and web framework basics using a modern Python stack.

## Technologies Used
- **Python**
- **Streamlit:** For the web framework.
- **Pandas:** For data manipulation.
- **yfinance:** For fetching financial data from Yahoo! Finance.
- **Plotly:** For creating interactive charts.
- **pandas-ta:** For calculating technical analysis indicators.

## How to Run
1. Clone this repository or download the source code.
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
The application will open in a new tab in your web browser.


#This project is a web-based, interactive dashboard for visualizing stock market data. A user can enter any valid stock ticker symbol (e.g., AAPL, TSLA, NVDA) and instantly receive a comprehensive dashboard.


The application provides a dynamic and user-friendly interface to analyze stock performance through several key components:

Interactive Price Chart: A candlestick chart displaying the stock's historical price, overlaid with 20-day and 50-day moving averages. Users can zoom, pan, and hover over the chart to inspect data points.

#Volume Indicator: A bar chart integrated below the price chart to show trading volume over time.

Key Financial Metrics: A snapshot of essential company statistics, including the latest closing price, market capitalization, P/E ratio, and the 52-week trading range.
Technical Indicators: Separate, clear charts for the Relative Strength Index (RSI) to identify overbought/oversold conditions and the Moving Average Convergence Divergence (MACD) to gauge momentum.

This project goes beyond simple data analysis in a notebook; it demonstrates the ability to build a full, user-facing product that fetches live data, processes it, and presents it in a clean, professional, and interactive format.


#Technical Summary
This dashboard was built using a modern Python data science and web development stack. It showcases the ability to integrate multiple technologies to create a cohesive and functional application.


#Key Skills Demonstrated

API Integration: Fetching live financial data programmatically using the yfinance library.
Data Manipulation: Using the pandas library to clean, process, and structure the time-series data for analysis and visualization.
Technical Analysis: Calculating common trading indicators (RSI, MACD, Moving Averages) with the pandas-ta library.
Interactive Data Visualization: Creating dynamic, responsive charts with Plotly that allow for user interaction.
Web Application Development: Building a user-friendly front-end and application logic with Streamlit, a powerful framework for rapidly creating data apps.
Dependency Management: Resolving complex version conflicts (e.g., numpy v2.0 breaking changes) and creating a reproducible environment with a requirements.txt file.

#Technologies Used
Language: Python 3
Web Framework: Streamlit
Data Fetching: yfinance
Data Processing: Pandas, Pandas-TA
Visualization: Plotly
Environment: Python Virtual Environment (venv), pip
Version Control: Git, GitHub


