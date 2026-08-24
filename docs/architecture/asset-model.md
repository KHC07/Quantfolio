# Asset Domain Model

## Responsibility

`Asset` represents one investment holding. It stores the security identifier, number of shares, and purchase price used to calculate the holding's cost basis.

## Implementation

```text
quantfolio/models/asset.py
```

The current class is a small stateful model:

```python
asset = Asset(ticker="NVDA", shares=10, purchase_price=150)
asset.calculate_cost_basis()  # 1500
```

## Data contract

| Field | Meaning | Current behavior |
| --- | --- | --- |
| `ticker` | Security identifier | Stored unchanged; no format validation |
| `shares` | Quantity held | Stored unchanged; expected to be numeric for cost calculations |
| `purchase_price` | Price paid per share | Stored unchanged; expected to be numeric for cost calculations |

## Behavior

`calculate_cost_basis()` returns:

$$
\text{cost basis} = \text{shares} \times \text{purchase price}
$$

The method does not include commissions, taxes, dividends, currency conversion, partial-lot rules, or multiple purchase lots.

## Relationships

- A `Portfolio` contains zero or more `Asset` instances.
- `Portfolio.total_cost_basis()` delegates each holding's calculation to `Asset.calculate_cost_basis()`.
- `Asset` has no dependency on market-data retrieval or analytics modules.

## Invariants and validation

The class currently does not enforce a non-empty ticker, positive share count, positive purchase price, or a numeric type. Those rules are therefore caller responsibilities. Adding validation would be a domain-model change and should be accompanied by explicit tests for the accepted input policy.

## Future extension points

Potential future responsibilities include immutable identifiers, currency, acquisition date, current valuation, and support for multiple tax lots. These should be added only when the surrounding portfolio and reporting workflows require them; they are not part of the current contract.
