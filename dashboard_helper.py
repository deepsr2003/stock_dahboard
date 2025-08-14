# dashboard_helper.py

import yfinance as yf
import pandas as pd
import pandas_ta as ta
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def fetch_data(ticker_symbol):
    """Fetches historical data and company info for a given ticker."""
    ticker = yf.Ticker(ticker_symbol)
    # Use "5y" for a good range of data, "max" can be too large
    hist_data = ticker.history(period="5y")

    if hist_data.empty:
        return None, None

    info = ticker.info
    return hist_data, info


def calculate_technicals(data):
    """Calculates technical indicators (RSI and MACD) and adds them to the dataframe."""
    data.ta.rsi(append=True)
    data.ta.macd(append=True)
    return data


def create_price_chart(data, info):
    """Creates the main price chart with moving averages."""
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.05, row_heights=[0.7, 0.3])

    # Plot Price
    fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'],
                                 name='Price'), row=1, col=1)

    # Add Moving Averages
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'].rolling(window=20).mean(),
                             mode='lines', name='20-Day MA', line=dict(color='orange', width=1)), row=1, col=1)
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'].rolling(window=50).mean(),
                             mode='lines', name='50-Day MA', line=dict(color='yellow', width=1)), row=1, col=1)

    # Plot Volume
    fig.add_trace(go.Bar(
        x=data.index, y=data['Volume'], name='Volume', marker_color='lightblue'), row=2, col=1)

    # Update layout
    company_name = info.get('shortName', 'Stock')
    fig.update_layout(
        title=f'{company_name} Price and Volume',
        yaxis_title='Price (USD)',
        xaxis_rangeslider_visible=False,
        template='plotly_dark'
    )
    fig.update_yaxes(title_text="Volume", row=2, col=1)

    return fig


def create_indicator_charts(data):
    """Creates charts for RSI and MACD."""
    # Create a figure for MACD
    macd_fig = go.Figure()
    macd_fig.add_trace(go.Scatter(
        x=data.index, y=data['MACD_12_26_9'], name='MACD', line=dict(color='blue', width=1)))
    macd_fig.add_trace(go.Scatter(
        x=data.index, y=data['MACDs_12_26_9'], name='Signal', line=dict(color='orange', width=1)))
    macd_fig.add_trace(go.Bar(
        x=data.index, y=data['MACDh_12_26_9'], name='Histogram', marker_color='grey'))
    macd_fig.update_layout(title_text='MACD', template='plotly_dark')

    # Create a figure for RSI
    rsi_fig = go.Figure()
    rsi_fig.add_trace(go.Scatter(
        x=data.index, y=data['RSI_14'], name='RSI', line=dict(color='purple', width=1)))
    rsi_fig.add_hline(y=70, line_dash="dash", line_color="red",
                      annotation_text="Overbought (70)")
    rsi_fig.add_hline(y=30, line_dash="dash", line_color="green",
                      annotation_text="Oversold (30)")
    rsi_fig.update_layout(
        title_text='RSI (Relative Strength Index)', template='plotly_dark')

    return macd_fig, rsi_fig
