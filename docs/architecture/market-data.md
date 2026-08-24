# Market Data

## Responsibility

The market-data layer isolates retrieval of historical prices from the rest of the application. Its current public boundary is `MarketDataProvider.get_historical_prices(ticker)`.

## Implementation

```text
quantfolio/data/market_data.py
```

## Provider contract

```python
provider = MarketDataProvider()
data = provider.get_historical_prices("NVDA")
```

The method passes the ticker directly to `yfinance.download()` and returns the provider's result unchanged. In the current implementation, this is normally a pandas `DataFrame`, but Quantfolio does not normalize or wrap that result.

## Boundary and data flow

```text
caller -> MarketDataProvider -> yfinance -> external market-data service
caller <- raw provider result
```

Analytics functions do not call `MarketDataProvider` directly. A caller must extract an ordered price sequence, such as a close-price column, before passing it to return or risk calculations.

## Current behavior

- The ticker is a required positional argument.
- Provider options such as date range, interval, auto-adjustment, and timeout are not exposed.
- Network errors, empty results, missing values, and provider-specific schemas are not translated into Quantfolio-specific errors.
- There is no caching, retry policy, rate-limit handling, persistence, or offline source.

## Design constraints

Code using this layer should treat the external result as untrusted input. It should verify that the required price column exists, values are ordered by date, and missing or invalid prices are handled before analytics are called.

## Future extension points

A normalized market-data interface could make the analytics pipeline independent of `yfinance`. Such an interface should define date/index behavior, price fields, missing-data policy, provider errors, and request parameters before additional providers are added.