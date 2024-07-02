"""
This module provides functionality to fetch ticker data from the MarketStack API and process it.

It uses the `requests` package to make HTTP requests, `json` for parsing the API response, and `pandas` for data manipulation.

Functions:
    get_tickers(access_key): Fetches ticker data from the MarketStack API and processes it.
"""

import pandas as pd
import json
import requests

def get_tickers(access_key):
    """
    Fetches ticker data from the MarketStack API and processes it.

    Args:
        access_key (str): Your MarketStack API access key.

    Returns:
        list: A list of tickers.

    Example:
        >>> get_tickers('your_marketstack_access_key')
        This will fetch the ticker data from the MarketStack API using your access key and return a list of tickers.

    """
    # Set your MarketStack API access key
    params = {'access_key': access_key, 'limit': 350}
    api_result = requests.get('http://api.marketstack.com/v1/exchanges/XJSE/tickers', params)
    api_response = api_result.json()

    # Serializing json
    json_object = json.dumps(api_response, indent=4)
    # Writing to sample.json
    with open("jse.json", "w") as outfile:
        outfile.write(json_object)

    # Extract tickers from the API response
    df1 = pd.json_normalize(api_response["data"]["tickers"])
    new = df1["symbol"].str.split(".", n=1, expand=True)
    df1["ticker"] = new[0]
    df1.drop(columns=["has_intraday", "has_eod"], inplace=True)

    # Combine ticker components and replace exchange code
    new.columns = new.columns.astype(str)
    new.columns.values[1] = "tickers"
    new['0'] + '.' + new['tickers']
    new.replace("XJSE", "JO", inplace=True)

    result = pd.concat([df1, new], axis=1, join='inner')
    df2 = result['0'] + '.' + result['tickers']
    final = pd.concat([df1, df2], axis=1, join='inner')
    final.columns.values[3] = "tickers"

    # Convert tickers to a list
    xjse = final["tickers"].tolist()
    return xjse
