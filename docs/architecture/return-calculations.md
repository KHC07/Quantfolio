# Return Calculations

## Responsibility

This module provides stateless functions for deriving investment returns from an ordered sequence of positive prices. It does not retrieve data, store time series, or know about portfolios.

## Implementation

```text
quantfolio/analytics/returns.py
```

## Functions and contracts

| Function | Result |
| --- | --- |
| `calculate_returns(prices)` | Period-to-period simple returns |
| `calculate_cumulative_returns(returns)` | Cumulative compounded return after each period |
| `calculate_total_return(prices)` | Return from the first price to the last price |
| `calculate_annualized_return(prices, periods_per_year)` | Annualized total return |
| `calculate_log_returns(prices)` | Period-to-period logarithmic returns |

For prices $P_{t-1}$ and $P_t$, a simple return is:

$$
r_t = \frac{P_t - P_{t-1}}{P_{t-1}}
$$

The cumulative return compounds periodic returns:

$$
R_t = \prod_{i=1}^{t}(1+r_i) - 1
$$

Annualized return uses the number of observed periods:

$$
R_{annual} = (1 + R_{total})^{\frac{\text{periods per year}}{\text{number of periods}}} - 1
$$

## Input and validation rules

- Prices must be greater than zero for simple, total, annualized, and logarithmic return calculations.
- A price sequence with fewer than two values produces `[]` for periodic or log returns and `0.0` for total or annualized return.
- `periods_per_year` must be positive for annualized return.
- Inputs are expected to be ordered chronologically. The module does not inspect dates or reorder values.
- The functions return ordinary Python lists or floats and do not preserve date indexes.

## Boundary

```text
market-data result -> caller extracts ordered prices -> return functions -> numeric results
```

The caller is responsible for dividends, splits, fees, currency conversion, missing values, and choosing adjusted versus unadjusted prices. Those choices can materially change the meaning of the returned metrics.

## Limitations

The current API does not accept timestamps, return metadata, portfolio weights, or a risk-free-rate schedule. Supporting those concerns would require an explicit time-series or portfolio analytics contract rather than silently extending these sequence-based functions.