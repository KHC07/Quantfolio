# Portfolio Domain Model

## Responsibility

`Portfolio` is the aggregate root for a collection of investment assets. It owns the collection and provides portfolio-level cost-basis aggregation.

## Implementation

```text
quantfolio/models/portfolio.py
```

## State and operations

- `assets` is initialized as an empty list for every portfolio instance.
- `add_asset(asset)` appends the supplied object to the collection.
- `total_cost_basis()` sums `calculate_cost_basis()` for every stored asset.

```python
portfolio = Portfolio()
portfolio.add_asset(Asset("NVDA", 10, 150))
portfolio.total_cost_basis()  # 1500
```

## Aggregation contract

The portfolio total is calculated as:

$$
	ext{portfolio cost basis} = \sum_{i=1}^{n} \text{asset}_i.\text{cost basis}
$$

An empty portfolio returns `0`. The portfolio does not calculate market value, performance, allocation, or risk.

## Relationships

- The portfolio depends on the behavior of its stored assets, specifically their `calculate_cost_basis()` method.
- It does not retrieve market data and has no dependency on `quantfolio.data` or `quantfolio.analytics`.
- The current implementation accepts any object with a compatible cost-basis method; it does not enforce an `Asset` type.

## Invariants and validation

The class currently does not validate asset types, duplicate tickers, share quantities, purchase prices, or mutation of the public `assets` list. Callers can therefore change the collection directly. These are intentional descriptions of the current implementation, not guarantees that invalid input is rejected.

## Future extension points

Valuation, portfolio weights, transactions, and performance attribution would require additional domain rules. They should be introduced with a defined relationship to `Asset` and with a decision about whether the portfolio remains mutable and list-backed.