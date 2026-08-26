import numpy as np

from quantfolio.models.asset import Asset
from quantfolio.models.portfolio import Portfolio

from quantfolio.analytics.portfolio import (
    calculate_portfolio_value,
    calculate_portfolio_weights,
    calculate_portfolio_return,
    calculate_covariance_matrix,
    calculate_portfolio_variance,
    calculate_portfolio_volatility,
)

from quantfolio.analytics.returns import calculate_returns
from quantfolio.analytics.risk import calculate_sharpe_ratio


def test_portfolio_analysis_pipeline():
    vfv = Asset("VFV", 20, 120)
    nvda = Asset("NVDA", 10, 180)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)
    portfolio.add_asset(nvda)

    current_prices = {
        "VFV": 135,
        "NVDA": 200,
    }

    value = calculate_portfolio_value(
        portfolio,
        current_prices,
    )

    weights = calculate_portfolio_weights(
        portfolio,
        current_prices,
    )

    returns = {
        "VFV": 0.10,
        "NVDA": 0.20,
    }

    portfolio_return = calculate_portfolio_return(
        portfolio,
        current_prices,
        returns,
    )

    historical_prices = {
        "VFV": [100, 102, 101, 103, 104],
        "NVDA": [180, 185, 181, 186, 190],
    }

    historical_returns = {
        ticker: calculate_returns(prices)
        for ticker, prices in historical_prices.items()
    }

    covariance_matrix = calculate_covariance_matrix(
        historical_returns
    )

    portfolio_variance = calculate_portfolio_variance(
        weights,
        covariance_matrix,
    )

    portfolio_volatility = calculate_portfolio_volatility(
        weights,
        covariance_matrix,
    )

    historical_portfolio_returns = [weights["VFV"] * vfv_return + weights["NVDA"] * nvda_return
        for vfv_return, nvda_return in zip(
            historical_returns["VFV"],
            historical_returns["NVDA"],
        )
    ]

    sharpe_ratio = calculate_sharpe_ratio(
        historical_portfolio_returns
    )

    assert value == 4700

    assert np.isclose(
        sum(weights.values()),
        1.0,
    )

    assert np.isclose(
        portfolio_return,
        0.1425531914893617,
    )

    assert covariance_matrix.shape == (2, 2)

    assert portfolio_variance >= 0

    assert portfolio_volatility >= 0

    assert np.isfinite(sharpe_ratio)