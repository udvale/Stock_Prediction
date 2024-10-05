import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Function to load stock data
def load_data(stock, start, end):
    data = yf.download(stock, start=start, end=end)
    data = data[['Close']]
    return data

# Function to create sequences
def create_sequences(data, window_size):
    if len(data) < window_size:
        return np.array([]), np.array([])
    X, y = [], []
    for i in range(window_size, len(data)):
        X.append(data[i-window_size:i, 0])
        y.append(data[i, 0])
    return np.array(X), np.array(y)

# Function to build and train the LSTM model
def build_and_train_model(X_train, y_train, X_test):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=20, batch_size=32)
    return model

# Streamlit App
st.title("Google Stock Price Prediction")

# Sidebar for user input
st.sidebar.subheader("Stock Input Parameters")
stock = st.sidebar.text_input("Stock Symbol", "GOOG")

# Add an informative message about the date range
st.sidebar.markdown("""
    **Please select a date range that provides sufficient data for predictions.** 
    For best results, select a start date earlier than 2015 to ensure enough historical data.
""")

start = st.sidebar.date_input("Start Date", pd.to_datetime("2010-01-01"))
end = st.sidebar.date_input("End Date", pd.to_datetime("2022-01-01"))

# Load and display stock data
if st.sidebar.button("Load Data"):
    data = load_data(stock, start, end)

    # Check if there's enough data
    if len(data) < 60:
        st.warning("Not enough data to create sequences. Please adjust the date range.")
    else:
        st.write(f"### {stock} Stock Data from {start} to {end}")
        st.line_chart(data['Close'])

        # Preprocess the data
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(data.values)

        # Train-test split
        train_size = int(len(scaled_data) * 0.8)
        train_data, test_data = scaled_data[:train_size], scaled_data[train_size:]

        # Prepare sequences
        window_size = 60
        X_train, y_train = create_sequences(train_data, window_size)
        X_test, y_test = create_sequences(test_data, window_size)

        # Reshape for LSTM input
        if X_train.size == 0 or X_test.size == 0:
            st.warning("Not enough data to create sequences. Please adjust the date range.")
        else:
            X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
            X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

            # Train the LSTM model
            model = build_and_train_model(X_train, y_train, X_test)

            # Predict stock prices
            predicted_stock_price = model.predict(X_test)
            predicted_stock_price = scaler.inverse_transform(predicted_stock_price)

            # Actual stock prices
            actual_stock_price = scaler.inverse_transform(test_data[window_size:])

            # Plot results
            st.write(f"### {stock} Stock Price Prediction vs. Actual")
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(data.index[train_size + window_size:], actual_stock_price, color='blue', label='Actual Stock Price')
            ax.plot(data.index[train_size + window_size:], predicted_stock_price, color='red', label='Predicted Stock Price')
            ax.set_xlabel('Date')
            ax.set_ylabel('Stock Price')
            ax.legend()
            st.pyplot(fig)

            st.write(f"### Stock Summary Statistics")
            st.write(data.describe())