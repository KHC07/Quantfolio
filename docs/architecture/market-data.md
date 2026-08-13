# Market Data Architecture

## Purpose

The market data layer is responsible for retrieving historical financial market data for Quantfolio.

## Data Provider

Quantfolio currently uses the `yfinance` Python library to retrieve historical market data from Yahoo Finance.

## MarketDataProvider

The `MarketDataProvider` class acts as an abstraction between Quantfolio and the external market data source.

Its main responsibility is retrieving historical price data for a given ticker.

Example:

```python
provider = MarketDataProvider()

data = provider.get_historical_prices("NVDA")