# Stock Price Prediction using ML

## Overview
Stock prices are highly volatile and can be influenced by various factors such as news events, market sentiment, and economic data. The goal of this project is to predict Google stock prices using historical data and compare the performance of a simple Linear Regression model with a more advanced LSTM model.

**Models Used**:
- Linear Regression: A simple model that assumes a linear relationship between input (past stock prices) and output (future prices).
- LSTM (Long Short-Term Memory): A type of Recurrent Neural Network (RNN) that is capable of learning from sequential data, making it ideal for time-series prediction tasks like stock price forecasting.

## Dataset
The dataset for this project consists of historical Google stock prices, sourced from [Yahoo Finance](https://finance.yahoo.com/quote/GOOG/history/). The dataset includes:
- Open, High, Low, and Close prices
- Volume data
For the purpose of prediction, I focused on the ```closing prices```, which are often considered the most accurate reflection of a stock's value at the end of the trading day. The data is preprocessed by normalizing the closing prices and splitting them into training and test sets. 

  <img src="https://github.com/user-attachments/assets/4c122907-f1cb-4e0b-81c4-5b0cdb10a87f" alt="Screenshot 2024-07-30 180759"  style="border: 2px solid rgba(0, 0, 0, 0.2); border-radius: 15px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); display: block;" />

## Deployment

You can view the deployed version of the stock prediction web app - https://prediction-goog-yf.streamlit.app/.

This application is hosted on Streamlit Cloud, which allows users to easily access and interact with the model's predictions. 
The app fetches stock data using the Yahoo Finance API and visualizes the predicted stock prices against actual prices.

## Installation and Setup
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/udvale/stock-price-prediction.git
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

4. Install required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
1. Running Steamlit app:
   ```bash
   streamlit run stock_prediction.py
2. Open your web browser and navigate to the URL displayed in the terminal (usually http://localhost:8501).
3. Input the desired stock symbol (default is "GOOG") and select a date range.
4. Click "Load Data" to fetch and visualize the stock prices, and view the predictions.

