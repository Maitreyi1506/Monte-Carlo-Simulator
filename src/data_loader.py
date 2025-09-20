import yfinance as yf
import pandas as pd

def get_ohlc(ticker, start="2020-01-01", end="2025-01-01"):
    df = yf.download(ticker, start=start, end=end, progress=False)
    return df[["Open", "High", "Low", "Close"]]
