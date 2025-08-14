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
