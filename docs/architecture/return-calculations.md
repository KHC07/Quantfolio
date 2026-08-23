# Return Calculations

## Purpose

Adds the return analytics layer to Quantfolio.

The purpose of this module is to calculate different types of investment returns from historical price data.

Implementation:

```text
quantfolio/
└── analytics/
    └── returns.py
```

Tests:

```text
tests/
└── test_returns.py
```

---

## Implemented Calculations

### Period Returns

Calculates the return between each consecutive price.

Formula:

```text
R = (current_price - previous_price) / previous_price
```

Implemented with:

```python
calculate_returns(prices)
```

---

### Cumulative Returns

Calculates compounded returns over multiple periods.

Formula:

```text
Cumulative Return = product(1 + period_return) - 1
```

Implemented with:

```python
calculate_cumulative_returns(returns)
```

---

### Total Return

Calculates the overall return from the starting price to the final price.

Formula:

```text
Total Return = (final_price - starting_price) / starting_price
```

Implemented with:

```python
calculate_total_return(prices)
```

---

### Annualized Return

Converts a total return into an annualized return based on the number of periods per year.

Formula:

```text
Annualized Return = (1 + total_return)^(periods_per_year / number_of_periods) - 1
```

Implemented with:

```python
calculate_annualized_return(prices, periods_per_year)
```

The function validates that `periods_per_year` is greater than zero.

---

### Log Returns

Calculates continuously compounded returns.

Formula:

```text
Log Return = ln(current_price / previous_price)
```

Implemented with:

```python
calculate_log_returns(prices)
```

Prices must be greater than zero.

---

## Validation

The return functions include validation for invalid inputs, including:

- Zero prices where they would cause division by zero
- Negative prices
- Invalid `periods_per_year`
- Insufficient price data

---

## Testing

All return calculations are tested in:

```text
tests/test_returns.py
```

The tests cover:

- Positive returns
- Negative returns
- No price change
- Empty inputs
- Single-price inputs
- Invalid prices
- Cumulative compounding
- Annualized returns
- Invalid annualization parameters
- Log returns


---

## Design

Return calculations are kept in the `analytics` layer rather than inside the `Asset` or `Portfolio` models.

```text
Market Data
     │
     ▼
Return Calculations
     │
     ├── Period Returns
     ├── Cumulative Returns
     ├── Total Return
     ├── Annualized Return
     └── Log Returns
```

This keeps the financial models responsible for representing assets and portfolios while the analytics layer handles quantitative calculations.

---

