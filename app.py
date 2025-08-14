# app.py

import streamlit as st
from dashboard_helper import (
    fetch_data,
    calculate_technicals,
    create_price_chart,
    create_indicator_charts
)

# Set page configuration for a wide layout
st.set_page_config(layout="wide")

# --- UI AND MAIN APP LOGIC ---

# App Title
st.title("Interactive Market Data Dashboard")

# User input for stock ticker
ticker_input = st.text_input(
    "Enter a stock ticker (e.g., AAPL, MSFT, GOOGL):", "AAPL").upper()

if ticker_input:
    # Show a spinner while data is being fetched
    with st.spinner(f"Loading data for {ticker_input}..."):
        data, info = fetch_data(ticker_input)

    # Check if data was successfully fetched
    if data is None:
        st.error("Invalid ticker or no data found. Please try another one.")
    else:
        # Calculate technical indicators
        data = calculate_technicals(data)

        # --- Display Dashboard ---

        # Header with company name and symbol
        st.header(f"{info.get('shortName', ticker_input)
                     } ({info.get('symbol', '')})")

        # Display key metrics in columns
        col1, col2, col3, col4 = st.columns(4)
       # col1.metric("Last Close", f"${data['Close'][-1]:.2f}")
        col1.metric("Last Close", f"${data['Close'].iloc[-1]:.2f}")
        col2.metric("Market Cap", f"{
                    (info.get('marketCap', 0) / 1_000_000_000):.2f}B")
        col3.metric("P/E Ratio", f"{info.get('trailingPE', 'N/A'):.2f}" if info.get('trailingPE') else "N/A")
        col4.metric("52-Week Range", f"{info.get('fiftyTwoWeekLow', 'N/A'):.2f} - {
                    info.get('fiftyTwoWeekHigh', 'N/A'):.2f}")

        # Create and display charts
        price_chart = create_price_chart(data, info)
        st.plotly_chart(price_chart, use_container_width=True)

        macd_chart, rsi_chart = create_indicator_charts(data)

        # Display indicator charts in columns
        ind_col1, ind_col2 = st.columns(2)
        with ind_col1:
            st.plotly_chart(macd_chart, use_container_width=True)
        with ind_col2:
            st.plotly_chart(rsi_chart, use_container_width=True)

        # Show raw data in an expander
        with st.expander("View Raw Data and Indicators"):
            st.dataframe(data.tail(100))  # Show last 100 rows
