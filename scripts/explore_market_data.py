from quantfolio.data.market_data import MarketDataProvider

provider = MarketDataProvider()

data = provider.get_historical_prices("NVDA")

print(data)