import yfinance as yf


class MarketDataProvider:
    YAHOO_TICKERS = {
        "VFV": "VFV.TO",
    }

    VALID_PERIODS = {
        "1d",
        "5d",
        "1mo",
        "3mo",
        "6mo",
        "1y",
        "2y",
        "5y",
        "10y",
        "ytd",
        "max",
    }

    def get_historical_prices(self, ticker, period="1y"):
        if not ticker:
            raise ValueError("Ticker must not be empty.")

        if period not in self.VALID_PERIODS:
            raise ValueError(
                f"Invalid period '{period}'. "
                f"Supported periods: {sorted(self.VALID_PERIODS)}"
            )

        yahoo_ticker = self.YAHOO_TICKERS.get(ticker, ticker)

        data = yf.download(
            yahoo_ticker,
            period=period,
            auto_adjust=False,
        )

        if data.empty:
            raise ValueError(
                f"No historical data found for ticker '{ticker}'."
            )

        if data.isna().any().any():
            raise ValueError(
                f"Historical data for ticker '{ticker}' contains missing values."
            )

        price_columns = ["Open", "High", "Low", "Close"]

        for column in price_columns:
            if column not in data.columns:
                continue

            values = data[column]

            if hasattr(values, "columns"):
                values = values.iloc[:, 0]

            if (values <= 0).any():
                raise ValueError(
                    f"Historical data for ticker '{ticker}' "
                    "contains invalid prices."
                )

        if all(column in data.columns for column in price_columns):
            open_prices = data["Open"]
            high_prices = data["High"]
            low_prices = data["Low"]
            close_prices = data["Close"]

            if hasattr(open_prices, "columns"):
                open_prices = open_prices.iloc[:, 0]
                high_prices = high_prices.iloc[:, 0]
                low_prices = low_prices.iloc[:, 0]
                close_prices = close_prices.iloc[:, 0]

            invalid_ohlc = (
                (low_prices > open_prices)
                | (low_prices > close_prices)
                | (high_prices < open_prices)
                | (high_prices < close_prices)
            )

            if invalid_ohlc.any():
                raise ValueError(
                    f"Historical data for ticker '{ticker}' "
                    "contains invalid OHLC data."
                )

        return data