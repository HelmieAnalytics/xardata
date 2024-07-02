# zaquity
"""
zaquity_data package

This package provides utility functions for working with stock data, including fetching historical data, cleaning outliers, and processing stock tickers.

Modules:
    - `marketstack_tickers`: Retrieves stock tickers from the MarketStack API.
    - `stock_data_fetcher`: Fetches historical stock data using the YahooQuery library.
    - `stock_data_cleaner`: Processes stock CSV files to remove outliers.

Usage:
    1. Import the desired module(s) from the package.
    2. Use the provided functions to perform specific tasks related to stock data.

Example:
    >>> from zaquity_data import marketstack_tickers, stock_data_fetcher, stock_data_cleaner
    >>> tickers = marketstack_tickers.get_tickers("your_api_key_here")
    >>> stock_data_fetcher.get_data(['AAPL', 'MSFT'], '2022-01-01', '2022-12-31', '/path/to/output_folder')
    >>> stock_data_cleaner.clean('/path/to/csv_folder')

"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your@email.com"
