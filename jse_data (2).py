"""
This module provides functionality to fetch historical stock data for a list of symbols and save it to individual CSV files.

It uses the `yahooquery` package to fetch the data, and `pandas` for data manipulation. The data is saved in the CSV format
using the standard library `os` module for file operations.

Functions:
    get_data(symbols, start, end, output_folder): Fetches historical stock data for a list of symbols and saves it to individual CSV files.
"""

from yahooquery import Ticker
import pandas as pd
import os

def get_data(symbols, start, end, output_folder):
    """
    Fetches historical stock data for a list of symbols and saves it to individual CSV files.

    Args:
        symbols (list): List of stock symbols (e.g., ['AAPL', 'MSFT', 'GOOGL']).
        start (str): Start date in 'YYYY-MM-DD' format.
        end (str): End date in 'YYYY-MM-DD' format.
        output_folder (str): Path to the folder where CSV files will be saved.

    Example:
        >>> get_data(['AAPL', 'MSFT', 'GOOGL'], '2020-01-01', '2020-12-31', './stock_data')
        This will fetch the stock data for Apple, Microsoft, and Google from the year 2020 and save it to the 'stock_data' folder.
    """
    tickers = Ticker(symbols, asynchronous=True)
    data = tickers.history(start=start, end=end, interval='1d')
    data = data.drop(['adjclose', 'dividends', 'splits'], axis=1)
    data.reset_index(inplace=True)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for symbol, group in data.groupby('symbol'):
        output_file = os.path.join(output_folder, f'{symbol}.csv')
        group.to_csv(output_file, header=True, index_label=False)

