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
    
