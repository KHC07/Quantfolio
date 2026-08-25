# Portfolio Analytics

## Responsibility

`quantfolio.analytics.portfolio` provides stateless calculations for valuing a
`Portfolio`, deriving current-value weights, combining asset returns, and
estimating portfolio risk. It performs calculations only; it does not store
portfolio state, retrieve prices, or fetch historical data.

## Implementation

```text
quantfolio/analytics/portfolio.py
```

## Functions and contracts

| Function | Inputs | Result |
| --- | --- | --- |
| `calculate_portfolio_value(portfolio, current_prices)` | Portfolio and ticker-to-price mapping | Total current market value |
| `calculate_portfolio_weights(portfolio, current_prices)` | Portfolio and ticker-to-price mapping | Ticker-to-weight mapping |
| `calculate_portfolio_return(portfolio, current_prices, returns)` | Portfolio, current prices, and ticker-to-return mapping | Weighted portfolio return |
| `calculate_covariance_matrix(returns)` | Ticker-to-return-series mapping | NumPy covariance matrix |
| `calculate_portfolio_variance(weights, covariance_matrix)` | Ticker-to-weight mapping and covariance matrix | Portfolio variance |
| `calculate_portfolio_volatility(weights, covariance_matrix)` | Ticker-to-weight mapping and covariance matrix | Portfolio volatility |

## Valuation and return flow

The valuation functions use current market values, calculated as shares held
multiplied by the supplied current price:

$$
V_p = \sum_{i=1}^{n} q_i P_i
$$

Weights are each asset's current value divided by the portfolio value:

$$
w_i = \frac{q_i P_i}{V_p}
$$

The portfolio return is the weighted sum of the supplied asset returns:

$$
R_p = \sum_{i=1}^{n} w_i R_i
$$

`current_prices` and `returns` are caller-provided mappings keyed by the
assets' tickers. The module does not retrieve, normalize, or timestamp these
values.

## Risk flow

`calculate_covariance_matrix()` converts the mapping's return series into a
NumPy array and delegates covariance estimation to `numpy.cov`. The series are
treated as aligned observations in mapping order. The resulting matrix and
the weights mapping must use the same asset order when passed to the
portfolio risk functions.

Portfolio variance follows the standard quadratic form:

$$
\sigma_p^2 = w^T \Sigma w
$$

Portfolio volatility is the square root of portfolio variance:

$$
\sigma_p = \sqrt{\sigma_p^2}
$$

## Validation and edge cases

- Missing current prices raise `ValueError` and identify the missing ticker.
- Missing asset returns raise `ValueError` and identify the missing ticker.
- An empty portfolio has value `0` and produces an empty weight mapping.
- A zero-value portfolio assigns zero to each weight rather than dividing by zero.
- Covariance input cannot be empty; every return series must contain at least two observations; and all series must have equal lengths.
- Variance and volatility reject empty weights or a weight count that does not match the covariance matrix dimension.
- The module does not validate price signs, return ranges, ticker uniqueness, weight sums, covariance symmetry, or covariance-matrix shape beyond the indexed dimension check.

## Boundary and dependencies

```text
Portfolio + caller-supplied prices -> valuation and weights
Portfolio + caller-supplied returns -> weighted portfolio return
Return series -> covariance matrix -> weights + covariance -> variance -> volatility
```

The module depends on the `Portfolio`/`Asset` object shape (`assets`, `ticker`,
and `shares`) and on NumPy for covariance, arrays, and square roots. It has no
dependency on `quantfolio.data`; callers are responsible for obtaining current
prices and aligned historical returns.

## Limitations and extension points

The current API does not model transaction costs, dividends, short positions,
cash, currency conversion, time-varying weights, rebalancing, dates, or
missing observations. Adding those concerns should begin with an explicit
time-series and portfolio-position contract rather than changing the meaning
of these mapping-based functions implicitly.