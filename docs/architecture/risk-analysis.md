# Risk Analytics Architecture

## Purpose

The risk analytics layer measures the risk and risk-adjusted performance of assets and portfolios.

## Risk Calculations

The module currently provides:

- Volatility
- Annualized Volatility
- Maximum Drawdown
- Sharpe Ratio

## Data Flow

Risk calculations use returns or historical prices depending on the metric.

```text
Historical Prices
       │
       ├──────────────→ Maximum Drawdown
       │
       ↓
    Returns
       │
       ├──────────────→ Volatility
       │
       ├──────────────→ Annualized Volatility
       │
       └──────────────→ Sharpe Ratio