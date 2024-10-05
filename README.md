# Stock Price Prediction with LSTM

## Overview

This project implements a stock price prediction model using Long Short-Term Memory (LSTM) networks, a type of recurrent neural network (RNN) well-suited for time series forecasting. The primary goal is to predict stock prices based on historical data, specifically focusing on Google’s stock (GOOG). Users can input a date range and stock symbol to visualize and predict future prices.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Trial and Error](#trial-and-error)
- [Improvements](#improvements)
- [Technologies Used](#technologies-used)

## Features
- Interactive user interface built with Streamlit for seamless data input and visualization.
- Utilizes the Yahoo Finance API to fetch historical stock data.
- Preprocessing steps include scaling and sequence creation for LSTM input.
- LSTM model architecture with dropout layers to prevent overfitting.
- Visualizations comparing predicted stock prices with actual prices.

## Installation
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

## Trial and Error
During the development of this project, several challenges were encountered:

- **Data Availability**: Initially, insufficient historical data led to errors when creating sequences for training the LSTM model. This was resolved by ensuring the user selects a longer date range.
- **Model Overfitting**: The first iterations of the LSTM model exhibited signs of overfitting due to a lack of dropout layers. This was mitigated by adding dropout layers between LSTM layers.
- **Predictive Performance**: Early predictions were inaccurate, prompting experimentation with different window sizes for sequence creation and adjustments in the model architecture.

## Improvements
Throughout the project development, the following improvements were implemented:

- Enhanced User Guidance: Added informative messages in the UI to help users select appropriate date ranges for predictions.
- Model Optimization: Adjusted the LSTM architecture and hyperparameters, including the number of epochs and batch size, to enhance prediction accuracy.
- Visualization Enhancements: Improved the graphical representation of actual vs. predicted stock prices, making it easier to interpret results.

## Technologies Used
- Python
- Streamlit
- TensorFlow/Keras
- NumPy
- Pandas
- Matplotlib
- Yahoo Finance API
