from unittest.mock import patch

import pandas as pd

from quantfolio.data.market_data import MarketDataProvider

def test_market_data_provider_creation():
    provider = MarketDataProvider()

    assert provider is not None

@patch("quantfolio.data.market_data.yf.download")
def test_get_historical_prices(mock_download):
    test_data = pd.DataFrame({"Close": [100, 105, 110]})

    mock_download.return_value = test_data

    provider = MarketDataProvider()

    data = provider.get_historical_prices("NVDA")

    assert data.equals(test_data)
    mock_download.assert_called_once_with("NVDA")