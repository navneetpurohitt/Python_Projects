import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from datetime import datetime, timedelta

import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import re

st.title("Finance Dashboard")
st.write("This is a simple finance dashboard that fetches and displays stock data.")


# Define the ticker symbol
ticker_symbol = st.sidebar.text_input(
    "Enter the ticker symbols as a comma-separated list (e.g., AAPL, MSFT):", "AAPL"
)
if len(ticker_symbol) != 0:

    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)
    period = st.sidebar.selectbox(
        "Select the period for historical data:",
        ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y"],
    )

    historical_data = ticker.history(period=period)  # data for the last year

    st.write(historical_data)
    df = pd.DataFrame(historical_data)

    plt.figure()
    up = df[df.Close >= df.Open]
    down = df[df.Close < df.Open]
    col1 = "green"
    col2 = "red"

    width = 0.3
    width2 = 0.03

    # Plotting up prices of the stock
    plt.bar(up.index, up.Close - up.Open, width, bottom=up.Open, color=col1)
    plt.bar(up.index, up.High - up.Close, width2, bottom=up.Close, color=col1)
    plt.bar(up.index, up.Low - up.Open, width2, bottom=up.Open, color=col1)

    # Plotting down prices of the stock
    plt.bar(down.index, down.Close - down.Open, width, bottom=down.Open, color=col2)
    plt.bar(down.index, down.High - down.Open, width2, bottom=down.Open, color=col2)
    plt.bar(down.index, down.Low - down.Close, width2, bottom=down.Close, color=col2)

    # rotating the x-axis tick labels at 30degree
    # towards right
    plt.xticks(rotation=30, ha="right")

    # displaying candlestick chart of stock data
    # of a week

    st.pyplot(plt.gcf())

    st.title("Prediciton of Future Prices")

    st.sidebar.write("Input for future price prediction")
    selected_date = st.sidebar.date_input(
        "For when you want the price", datetime.now() + timedelta(days=1)
    )
    st.sidebar.write(selected_date)

    # Prediction using a simple machine learning model (e.g., Linear Regression)

    st.write("Predicting the stock price for:", selected_date)

    # Prepare the data for ML model
    if len(historical_data) > 1:
        historical_data["Date"] = historical_data.index
        historical_data["Date"] = historical_data["Date"].map(
            datetime.toordinal
        )  # Convert dates to ordinal for ML

        X = historical_data[["Date"]]
        y = historical_data["Close"]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Standardize the features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Train the Linear Regression model
        model = LinearRegression()
        model.fit(X_train_scaled, y_train)

        # Predict the price for the selected date
        selected_date_ordinal = np.array([[selected_date.toordinal()]])
        selected_date_scaled = scaler.transform(selected_date_ordinal)
        predicted_price = model.predict(selected_date_scaled)[0]
        st.title("Predicted Price")
        # Calculate the accuracy score
        accuracy = model.score(X_test_scaled, y_test)

        st.write(
            f"Predicted price for {ticker_symbol} on {selected_date}: ${predicted_price:.2f}"
        )
        st.write(f"Model Accuracy: {accuracy * 100:.2f}%")
        
    else:
        st.write("Not enough historical data to train the model.")

else:
    st.write("Please enter a valid ticker symbol.")
    st.write("Example: AAPL for Apple Inc.")
    st.write("Example: MSFT for Microsoft Corporation")
    st.write("Example: GOOGL for Alphabet Inc.")
    st.write("Example: AMZN for Amazon.com Inc.")
    st.write("Example: TSLA for Tesla Inc.")
    st.write("Example: META for Meta Platforms Inc.")
    st.write("Example: NFLX for Netflix Inc.")
    st.write("Example: NVDA for NVIDIA Corporation")
    st.write("Example: AMD for Advanced Micro Devices Inc.")
    st.write("Example: INTC for Intel Corporation")
    st.write("Example: CSCO for Cisco Systems Inc.")
    st.write("Example: ORCL for Oracle Corporation")
    st.write("Example: IBM for International Business Machines Corporation")
    st.write("Example: QCOM for Qualcomm Incorporated")
    st.write("Example: TXN for Texas Instruments Incorporated")
    st.write("Example: AVGO for Broadcom Inc.")
    st.write("Example: ADI for Analog Devices Inc.")
    st.write("Example: MU for Micron Technology Inc.")
    st.write("Example: AMAT for Applied Materials Inc.")
    st.write("Example: LRCX for Lam Research Corporation")
    st.write("Example: KLAC for KLA Corporation")
    st.write("Example: SWKS for Skyworks Solutions Inc.")
    st.write("Example: QRVO for Qorvo Inc.")
    st.write("Example: NXPI for NXP Semiconductors NV")
    st.write("Example: STX for Seagate Technology Holdings PLC")
    st.write("Example: WDC for Western Digital Corporation")
    st.write("Example: STLD for Steel Dynamics Inc.")
    st.write("Example: NUE for Nucor Corporation")
    st.write("Example: X for United States Steel Corporation")
    st.write("Example: FCX for Freeport-McMoRan Inc.")
    st.write("Example: NEM for Newmont Corporation")
