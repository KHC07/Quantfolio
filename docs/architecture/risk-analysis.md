# Risk Analysis

## Responsibility

This module provides stateless risk and risk-adjusted performance calculations. It accepts price or return sequences and returns scalar metrics. It does not retrieve market data or manage portfolio holdings.

## Implementation

```text
quantfolio/analytics/risk.py
```

## Functions and contracts

| Function | Input | Result |
| --- | --- | --- |
| `calculate_volatility(returns)` | At least two periodic returns | Sample standard deviation |
| `calculate_annualized_volatility(returns, periods_per_year=252)` | Returns and positive frequency | Period volatility scaled by square root of frequency |
| `calculate_max_drawdown(prices)` | Non-empty price sequence | Most negative peak-to-trough decline |
| `calculate_sharpe_ratio(returns, risk_free_rate=0.0, periods_per_year=252)` | Returns and scalar risk-free rate | Annualized Sharpe ratio |

## Formulas and conventions

Volatility uses sample standard deviation (`ddof=1`):

$$
\sigma_{annual} = \sigma_{period} \sqrt{N}
$$

For each price $P_t$, the drawdown is measured from the highest price observed through that point:

$$
D_t = \frac{P_t - \max(P_0, \ldots, P_t)}{\max(P_0, \ldots, P_t)}
$$

`calculate_max_drawdown` returns the minimum $D_t$, so declines are negative and a never-declining series returns `0.0`.

The Sharpe ratio subtracts the scalar risk-free rate from each return, divides the mean excess return by sample volatility, and annualizes the result:

$$
S_{annual} = \frac{\operatorname{mean}(r - r_f)}{\operatorname{std}(r - r_f)}\sqrt{N}
$$

## Validation rules

- Volatility, annualized volatility, and Sharpe ratio require at least two returns.
- Annualization frequencies must be positive.
- Sharpe ratio raises `ValueError` when excess-return volatility is zero.
- Max drawdown requires at least one price, but the current implementation does not reject zero or negative prices.
- Inputs are expected to be ordered chronologically; dates and missing values are not handled by this module.

## Boundary and dependencies

```text
caller -> risk functions -> NumPy scalar result
```

The module depends on NumPy for standard deviation, mean, array arithmetic, and square root. It is independent of the market-data provider and portfolio models. Callers must ensure the return frequency matches `periods_per_year`; the default `252` represents typical daily market observations, not a universal convention.

## Limitations

The current API does not model time-varying risk-free rates, irregular observations, benchmark-relative risk, portfolio covariance, or confidence intervals. These concerns should be specified before adding them to the sequence-based functions.