import yfinance as yf


class MarketDataProvider:
    def get_historical_prices(self, ticker):
        data = yf.download(ticker)
        return data