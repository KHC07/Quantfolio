# Quantfolio Architecture Overview

## Purpose

Quantfolio is organized around a small set of domain models and stateless analytics functions. The current architecture separates portfolio state from external data access and numerical calculations.

## Package boundaries

```text
quantfolio/
├── models/
│   ├── asset.py       # Asset state and cost basis
│   └── portfolio.py   # Collection of assets and portfolio totals
├── data/
│   └── market_data.py # External market-data provider
└── analytics/
    ├── returns.py    # Return calculations
    └── risk.py       # Volatility and risk metrics
```

## Data flow

The intended flow is:

1. `MarketDataProvider` retrieves historical market data from `yfinance`.
2. A caller extracts an ordered price series from the provider result.
3. Functions in `analytics.returns` convert prices into periodic, cumulative, total, annualized, or logarithmic returns.
4. Functions in `analytics.risk` consume returns or prices to calculate volatility, drawdown, and Sharpe ratio.
5. `Asset` and `Portfolio` hold investment information and calculate cost basis independently of the analytics pipeline.

The current code does not yet connect these steps through a service or application layer. Callers are responsible for selecting columns, preserving chronological order, and passing compatible values between packages.

## Architectural principles

- **Models own portfolio state.** `Asset` stores one holding, while `Portfolio` stores a list of assets and aggregates cost basis.
- **Data access is isolated.** External-provider behavior is concentrated in `MarketDataProvider` instead of being embedded in analytics functions.
- **Analytics functions are stateless.** Return and risk calculations receive values as arguments and return calculated values or raise `ValueError` for invalid inputs.
- **Numerical conventions are explicit.** Prices must be positive for return calculations, sample standard deviation is used for volatility, and annualization requires a positive periods-per-year value.
- **Dependencies remain replaceable.** The analytics modules use the Python standard library and NumPy; market-data retrieval uses `yfinance`. No analytics function calls the provider directly.

## Current limitations

- The models have no type validation, persistence, valuation, or market-price integration.
- The market-data provider exposes the raw `yfinance` result and has no caching, retries, authentication, or normalized result type.
- Analytics functions operate on sequence-like inputs and do not manage dates, missing values, dividends, fees, or portfolio weights.
- There is no application layer coordinating data retrieval, portfolio valuation, or reporting.

## Related documents

- [Asset Domain Model](asset-model.md)
- [Portfolio Domain Model](portfolio-model.md)
- [Portfolio Analytics](portfolio-analytics.md)
- [Market Data](market-data.md)
- [Return Calculations](return-calculations.md)
- [Risk Analysis](risk-analysis.md)
