import pandas as pd
import pytest
from unittest.mock import patch

from quantfolio.data.market_data import MarketDataProvider


@patch("quantfolio.data.market_data.yf.download")
def test_get_historical_prices(mock_download):
    test_data = pd.DataFrame({"Close": [100, 105, 110]})

    mock_download.return_value = test_data

    provider = MarketDataProvider()

    data = provider.get_historical_prices("NVDA")

    mock_download.assert_called_once_with(
        "NVDA",
        period="1y",
        auto_adjust=False,
    )

    pd.testing.assert_frame_equal(data, test_data)


def test_empty_ticker():
    provider = MarketDataProvider()

    with pytest.raises(ValueError, match="Ticker must not be empty"):
        provider.get_historical_prices("")


@patch("quantfolio.data.market_data.yf.download")
def test_no_historical_data(mock_download):
    mock_download.return_value = pd.DataFrame()

    provider = MarketDataProvider()

    with pytest.raises(
        ValueError,
        match="No historical data found for ticker 'INVALID'",
    ):
        provider.get_historical_prices("INVALID")


def test_invalid_period():
    provider = MarketDataProvider()

    with pytest.raises(
        ValueError,
        match="Invalid period 'banana'",
    ):
        provider.get_historical_prices("NVDA", period="banana")


@patch("quantfolio.data.market_data.yf.download")
def test_missing_values(mock_download):
    test_data = pd.DataFrame({
        "Close": [100, 105, None],
    })

    mock_download.return_value = test_data

    provider = MarketDataProvider()

    with pytest.raises(
        ValueError,
        match="Historical data for ticker 'NVDA' contains missing values",
    ):
        provider.get_historical_prices("NVDA")


@patch("quantfolio.data.market_data.yf.download")
def test_invalid_prices(mock_download):
    test_data = pd.DataFrame({
        "Open": [100, 105, 110],
        "High": [102, 107, 112],
        "Low": [99, 103, 109],
        "Close": [101, 106, 0],
        "Volume": [1000, 1200, 1100],
    })

    mock_download.return_value = test_data

    provider = MarketDataProvider()

    with pytest.raises(
        ValueError,
        match="Historical data for ticker 'NVDA' contains invalid prices",
    ):
        provider.get_historical_prices("NVDA")


@patch("quantfolio.data.market_data.yf.download")
def test_invalid_ohlc_data(mock_download):
    test_data = pd.DataFrame({
        "Open": [100, 105, 110],
        "High": [102, 107, 108],
        "Low": [99, 103, 109],
        "Close": [101, 106, 110],
        "Volume": [1000, 1200, 1100],
    })

    mock_download.return_value = test_data

    provider = MarketDataProvider()

    with pytest.raises(
        ValueError,
        match="Historical data for ticker 'NVDA' contains invalid OHLC data",
    ):
        provider.get_historical_prices("NVDA")