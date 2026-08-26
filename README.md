# Quantfolio

Quantfolio is a lightweight portfolio analytics library for modeling investment holdings, calculating return and risk metrics, and working with historical market data.

It is designed as a practical engineering and data science project for building, testing, and extending portfolio analysis workflows in Python.

## Overview

Quantfolio currently provides:

* Asset and portfolio domain models
* Historical market data through Yahoo Finance
* Simple, cumulative, total, annualized, and log return calculations
* Volatility and annualized volatility
* Maximum drawdown
* Sharpe ratio
* Portfolio value and portfolio weights
* Portfolio returns
* Covariance, variance, and portfolio volatility
* Historical portfolio return calculations
* Input validation and error handling
* Automated unit and integration testing

The project is intentionally modular so that the analytical foundation can be extended with more advanced quantitative finance, data science, and machine learning functionality in future versions.

---

## Version 1

Version 1 establishes the core analytical foundation of Quantfolio.

### Included

* Asset modeling
* Portfolio modeling
* Historical market-data retrieval
* Market-data validation
* Return analytics
* Risk analytics
* Portfolio analytics
* Integration testing
* Example analysis scripts
* Architecture documentation

### Not yet included

* Portfolio optimization
* Factor models
* Machine learning
* AI-assisted data analysis
* Automated trading
* Live portfolio monitoring
* Database persistence
* Web application
* REST API

These capabilities are planned for future versions.

---

## Project Structure

```text
Quantfolio/
│
├── quantfolio/
│   ├── analytics/
│   │   ├── portfolio.py
│   │   ├── returns.py
│   │   └── risk.py
│   │
│   ├── data/
│   │   └── market_data.py
│   │
│   ├── models/
│   │   ├── asset.py
│   │   └── portfolio.py
│   │
│   └── __init__.py
│
├── scripts/
│   ├── asset_demo.py
│   ├── explore_market_data.py
│   └── portfolio_analysis.py
│
├── tests/
│   ├── test_asset.py
│   ├── test_integration.py
│   ├── test_market_data.py
│   ├── test_portfolio.py
│   ├── test_portfolio_analytics.py
│   ├── test_returns.py
│   └── test_risk.py
│
├── docs/
│   └── architecture/
│       ├── asset-model.md
│       ├── market-data.md
│       ├── overview.md
│       ├── portfolio-analytics.md
│       ├── portfolio-model.md
│       ├── return-calculations.md
│       └── risk-analysis.md
│
├── .gitignore
├── pytest.ini
├── README.md
├── requirements.txt
└── pyproject.toml
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-user>/Quantfolio.git
cd Quantfolio
```

Create and activate a virtual environment:

### Windows

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Install Quantfolio in editable mode:

```bash
pip install -e .
```

---

## Requirements

Quantfolio currently targets **Python 3.11+**.

Core dependencies include:

* NumPy
* Pandas
* Matplotlib
* yfinance
* pytest

See `requirements.txt` for the complete dependency list.

---

## Quick Start

### Build a Portfolio

```python
from quantfolio.models.asset import Asset
from quantfolio.models.portfolio import Portfolio

vfv = Asset("VFV", 20, 120)
nvda = Asset("NVDA", 10, 180)

portfolio = Portfolio()

portfolio.add_asset(vfv)
portfolio.add_asset(nvda)

print(portfolio.total_cost_basis())
```

### Calculate Portfolio Value and Weights

```python
from quantfolio.models.asset import Asset
from quantfolio.models.portfolio import Portfolio
from quantfolio.analytics.portfolio import (
    calculate_portfolio_value,
    calculate_portfolio_weights,
)

vfv = Asset("VFV", 20, 120)
nvda = Asset("NVDA", 10, 180)

portfolio = Portfolio()

portfolio.add_asset(vfv)
portfolio.add_asset(nvda)

current_prices = {
    "VFV": 135,
    "NVDA": 200,
}

portfolio_value = calculate_portfolio_value(
    portfolio,
    current_prices,
)

weights = calculate_portfolio_weights(
    portfolio,
    current_prices,
)

print(portfolio_value)
print(weights)
```

### Calculate Returns

```python
from quantfolio.analytics.returns import (
    calculate_returns,
    calculate_total_return,
    calculate_annualized_return,
)

prices = [100, 110, 120, 130]

returns = calculate_returns(prices)

print(returns)
print(calculate_total_return(prices))
print(calculate_annualized_return(prices, periods_per_year=4))
```

### Calculate Risk Metrics

```python
from quantfolio.analytics.risk import (
    calculate_volatility,
    calculate_annualized_volatility,
    calculate_sharpe_ratio,
)

returns = [0.10, 0.20, 0.15, 0.05]

print(calculate_volatility(returns))

print(
    calculate_annualized_volatility(
        returns,
        periods_per_year=252,
    )
)

print(
    calculate_sharpe_ratio(
        returns,
        risk_free_rate=0.02,
        periods_per_year=252,
    )
)
```

### Fetch Historical Market Data

```python
from quantfolio.data.market_data import MarketDataProvider

provider = MarketDataProvider()

prices = provider.get_historical_prices(
    "VFV",
    period="1y",
)

print(prices.head())
```

---

## Analytics

### Returns

Quantfolio provides:

* `calculate_returns(prices)`
* `calculate_cumulative_returns(returns)`
* `calculate_total_return(prices)`
* `calculate_annualized_return(prices, periods_per_year)`
* `calculate_log_returns(prices)`

### Risk

Quantfolio provides:

* `calculate_volatility(returns)`
* `calculate_annualized_volatility(returns, periods_per_year=252)`
* `calculate_max_drawdown(prices)`
* `calculate_sharpe_ratio(returns, risk_free_rate=0.0, periods_per_year=252)`

### Portfolio Analytics

Quantfolio provides:

* `calculate_portfolio_value(portfolio, current_prices)`
* `calculate_portfolio_weights(portfolio, current_prices)`
* `calculate_portfolio_return(portfolio, current_prices, returns)`
* `calculate_covariance_matrix(returns)`
* `calculate_portfolio_variance(weights, covariance_matrix)`
* `calculate_portfolio_volatility(weights, covariance_matrix)`
* `calculate_historical_portfolio_returns(weights, historical_returns)`

---

## Example Scripts

Quantfolio includes scripts demonstrating how the library can be used.

Run the asset demonstration:

```bash
python -m scripts.asset_demo
```

Explore historical market data:

```bash
python -m scripts.explore_market_data
```

Run the portfolio analysis:

```bash
python -m scripts.portfolio_analysis
```

---

## Testing

Quantfolio uses `pytest` for automated testing.

Run the complete test suite:

```bash
pytest
```

The Version 1 test suite currently contains **100 tests** covering:

* Asset models
* Portfolio models
* Market-data retrieval and validation
* Portfolio analytics
* Return calculations
* Risk calculations
* Integration workflows

Current Version 1 status:

```text
100 passed
```

The goal is to maintain a reliable analytical foundation as new functionality is introduced.

---

## Architecture

Quantfolio follows a separation-of-concerns architecture:

```text
                    Market Data
                        │
                        ▼
                ┌───────────────┐
                │ Data Provider │
                └───────┬───────┘
                        │
                        ▼
              ┌───────────────────┐
              │ Asset / Portfolio │
              │      Models       │
              └─────────┬─────────┘
                        │
                        ▼
                 ┌─────────────┐
                 │  Analytics  │
                 └──────┬──────┘
                        │
             ┌──────────┼──────────┐
             ▼          ▼          ▼
          Returns      Risk     Portfolio
                                  Analytics
```

The main responsibilities are:

* `models` — represent portfolio and asset state
* `data` — retrieve and validate external market data
* `analytics` — perform quantitative calculations
* `scripts` — demonstrate and exercise the library
* `tests` — verify individual components and integration workflows
* `docs` — document architecture and analytical methods

Additional architecture documentation is available in `docs/architecture/`.

---

## Roadmap

### Version 1 — Core Analytics

* [x] Asset model
* [x] Portfolio model
* [x] Market-data provider
* [x] Market-data validation
* [x] Return analytics
* [x] Risk analytics
* [x] Portfolio analytics
* [x] Integration testing
* [x] Architecture documentation

### Version 2 — Advanced Analytics

Planned areas include:

* [ ] Benchmark comparison
* [ ] Performance attribution
* [ ] Additional risk metrics
* [ ] Portfolio visualization
* [ ] Improved data handling
* [ ] More comprehensive portfolio analysis

### Future Versions

Potential future development includes:

* [ ] Portfolio optimization
* [ ] Factor analysis
* [ ] Machine learning models
* [ ] AI-assisted data-quality analysis
* [ ] Database persistence
* [ ] API layer
* [ ] Web application
* [ ] Advanced portfolio monitoring

The roadmap is intentionally flexible and will evolve as the project develops.

---

## Status

Quantfolio Version 1 is a **functional analytical prototype** focused on building a reliable foundation for portfolio analysis.

It is currently best suited for:

* Learning quantitative finance concepts
* Practicing Python software engineering
* Experimenting with portfolio analytics
* Building a foundation for future data science and machine learning work

It is **not currently intended to be a production-grade trading or investment platform**.

---

## License

This project does not currently include a license file.

If the repository will be made public or distributed to others, an appropriate open-source license should be added.
