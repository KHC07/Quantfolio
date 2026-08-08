# Quantfolio Domain Model

## Asset

An Asset represents a single investment holding in a portfolio.

### Responsibilities

- Store the investment ticker
- Store the number of shares
- Store the purchase price
- Calculate the cost basis

### Attributes

| Attribute | Description |
|---|---|
| ticker | Stock or ETF ticker symbol |
| shares | Number of shares owned |
| purchase_price | Price paid per share |

### Methods

| Method | Description |
|---|---|
| calculate_cost_basis() | Calculates shares × purchase price |

## Design Decision

The Asset class is responsible for representing investment information.

Market data retrieval will not be handled by Asset. A separate data component will be responsible for retrieving market prices. This separation keeps the domain model independent from external data sources.