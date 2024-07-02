"""
This module provides functionality to clean stock data by removing outliers.

It uses the `pandas` package for data manipulation, `numpy` for numerical operations, `scipy` for statistical functions, and `pathlib` for file path operations.

Functions:
    clean(csv_folder_path): Processes stock CSV files in the specified folder to remove outliers.
"""

import pandas as pd
import numpy as np
from scipy import stats
from pathlib import Path

def clean(csv_folder_path):
    """
    Processes stock CSV files in the specified folder to remove outliers.

    This function reads each CSV file in the specified folder, removes outliers in the price and volume columns using the Z-score method, and saves the cleaned data back to the CSV file.

    Args:
        csv_folder_path (str): Path to the folder containing CSV files.

    Returns:
        None

    Example:
        >>> clean('./stock_data')
        This will process all '.JO.csv' files in the 'stock_data' folder and remove outliers in the price and volume data.
    """
    csv_folder = Path(csv_folder_path)

    for file in csv_folder.glob('*.JO.csv'):
        mydata = pd.read_csv(file)
        df_new = mydata.iloc[:, [1, 2, 3, 4, 5, 6, 0]]

        df_new['date'] = pd.to_datetime(df_new['date']).dt.strftime('%Y-%m-%d')
        df_new.set_index('date', inplace=True)

        df = df_new[["open", "high", "low", "close", "volume"]]

        no_outlier_prices = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]

        new_file_name = file.parent.joinpath(f"{file.stem}.csv")
        no_outlier_prices.to_csv(new_file_name)
