# zaquity

This package provides utility functions for working with stock price series data of 350 securities trading on the Johannesburg Stock Exchange (XJSE) , including processing stock tickers, fetching historical data, cleaning outliers, and saving the price data in ohlcv format as a dataset in csv files to a folder on your local disc drive.

## Modules

`jse_tickers`: Retrieves stock tickers from the MarketStack API.

`jse_data`: Fetches historical stock data using the YahooQuery library.

`jse_process_data`: Processes stock CSV files to remove outliers.

## Implementation

### 1. Import the desired module(s) from the package.

```css
import zaquity
from zaquity import jse_tickers
from zaquity import jse_data
from zaquity import jse_process_data
```
   
### 2. Use the provided functions to perform specific tasks related to stock data.

`.get.tickers` function:
```css
tickers = jse_tickers.get_tickers("your_api_key_here")
```

`.get.data` function:
```css
jse_data.get_data(['AAPL', 'MSFT'], '2022-01-01', '2022-12-31', '/path/to/output_folder')
```

`.clean` function:
```css
jse_process_data.clean('/path/to/csv_folder')
```

## Example usage

```css
#Import functions
import zaquity
from zaquity import jse_tickers as jt
from zaquity import jse_data as jd
from zaquity import process_data as jpd

# Set variables
my_access_key = '<your_Marketstack_API_Key>'

symbols = tickers

start = '2000-01-27'
end = '2024-06-29'

output_folder_path = '/content/jsestocks'

#Call functions

tickers = jt.get_tickers(my_access_key)

jd.get_data(symbols, start, end, output_folder_path)

jpd.clean('/content/jsestocks')
```

version:"0.1.0"
author:"Helmie Analytics"
email:"francoishemie@outlook.com"
