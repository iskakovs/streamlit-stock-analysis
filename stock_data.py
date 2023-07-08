import logging #package is responsible for collecting all the logs (see the file)
import yfinance as yf #package is responsible for collecting stock real market data from Yahoo!Finance

logger = logging.getLogger()

# Define a function to collect the data from Yahoo!Finance, it uses tickers(symbols), defines the stock value start date and end date
def fetch_stock_data(symbol, start_date, end_date):
    """
    fetch stock data from yahoo finance
    :param symbol: ticker
    :type symbol: string
    :param start_date: start date
    :type start_date: date
    :param end_date: End date
    :type end_date: date
    :return: data
    :rtype: Dataframe
    """
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        if data is not None:
            data_with_indices = calculate_indices(data)
            return data_with_indices
        else:
            return None
    except Exception as e:
        logger.error(f'yf_download | Error: {str(e)}')
        return None

# Based on the 'data' variable defined above we define the function 'calculate_indices' to calculate SMA and RSI
def calculate_indices(data):
    """
    calculate SMA and RSI
    :param data: data
    :type data: Dataframe
    :return: data with indices
    :rtype: Dataframe
    """
  # Calculation of the SMA (Simple Moving Average) index
    data['SMA'] = data['Close'].rolling(window=20).mean()
    
    # Calculation of the RSI index (Relative Strength Index)
    delta = data['Close'].diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    avg_gain = up.rolling(window=14).mean()
    avg_loss = down.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    data['RSI'] = rsi
    return data   
