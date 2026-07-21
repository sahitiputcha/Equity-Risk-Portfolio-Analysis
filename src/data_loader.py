import yfinance as yf
import pandas as pd 

def download_market_data(tickers, start_date, end_date):
    """
    Download historical market data from Yahoo Finance.

    Parameters
    ----------
    tickers : list
        List of ticker symbols.
    start_date : str
        Start date in YYYY-MM-DD format.
    end_date : str
        End date in YYYY-MM-DD format.

    Returns
    -------
    pandas.DataFrame
        Historical market data.
    """
    data = yf.download(
        tickers=tickers,
        start = start_date,
        end= end_date,
        auto_adjust=True,
        progress = False,
        group_by="ticker"

    )
    return data
