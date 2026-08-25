import pytest
import numpy as np

from quantfolio.models.asset import Asset
from quantfolio.models.portfolio import Portfolio
from quantfolio.analytics.portfolio import (
    calculate_portfolio_value,
    calculate_portfolio_weights,
    calculate_portfolio_return,
    calculate_covariance_matrix,
    calculate_portfolio_variance,
    calculate_portfolio_volatility
)

# ==============================================================================
# calculate_portfolio_value() TESTS
# ==============================================================================

def test_calculate_portfolio_value_with_multiple_assets():
    vfv = Asset("VFV", 5, 100)
    nvda = Asset("NVDA", 10, 100)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)
    portfolio.add_asset(nvda)

    current_prices = {
        "VFV": 120,
        "NVDA": 180
    }

    actual = calculate_portfolio_value(portfolio, current_prices)
    expected = 2400.0

    assert actual == expected


def test_calculate_portfolio_value_with_single_asset():
    vfv = Asset("VFV", 5, 100)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)

    current_prices = {
        "VFV": 120
    }

    actual = calculate_portfolio_value(portfolio, current_prices)
    expected = 600.0

    assert actual == expected


def test_calculate_portfolio_value_with_empty_portfolio():
    portfolio = Portfolio()

    current_prices = {}

    actual = calculate_portfolio_value(portfolio, current_prices)
    expected = 0.0

    assert actual == expected


def test_calculate_portfolio_value_with_missing_price():
    vfv = Asset("VFV", 5, 100)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)

    current_prices = {}

    with pytest.raises(ValueError):
        calculate_portfolio_value(portfolio, current_prices)


def test_calculate_portfolio_value_with_zero_shares():
    vfv = Asset("VFV", 0, 100)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)

    current_prices = {
        "VFV": 120
    }

    actual = calculate_portfolio_value(portfolio, current_prices)
    expected = 0.0

    assert actual == expected


# ==============================================================================
# calculate_portfolio_weights() TESTS
# ==============================================================================

def test_calculate_portfolio_weights_with_multiple_assets():
    vfv = Asset("VFV", 5, 100)
    nvda = Asset("NVDA", 10, 100)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)
    portfolio.add_asset(nvda)

    current_prices = {
        "VFV": 120,
        "NVDA": 180
    }

    actual = calculate_portfolio_weights(portfolio, current_prices)

    expected = {
        "VFV": 0.25,
        "NVDA": 0.75
    }

    assert actual == expected


def test_calculate_portfolio_weights_with_single_asset():
    vfv = Asset("VFV", 5, 100)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)

    current_prices = {
        "VFV": 120
    }

    actual = calculate_portfolio_weights(portfolio, current_prices)

    expected = {
        "VFV": 1.0
    }

    assert actual == expected


def test_calculate_portfolio_weights_with_equal_values():
    vfv = Asset("VFV", 5, 100)
    nvda = Asset("NVDA", 5, 100)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)
    portfolio.add_asset(nvda)

    current_prices = {
        "VFV": 100,
        "NVDA": 100
    }

    actual = calculate_portfolio_weights(portfolio, current_prices)

    expected = {
        "VFV": 0.5,
        "NVDA": 0.5
    }

    assert actual == expected


def test_calculate_portfolio_weights_with_zero_value():
    portfolio = Portfolio()

    current_prices = {}

    actual = calculate_portfolio_weights(portfolio, current_prices)

    expected = {}

    assert actual == expected


def test_calculate_portfolio_weights_sum_to_one():
    vfv = Asset("VFV", 5, 100)
    nvda = Asset("NVDA", 10, 100)
    xiu = Asset("XIU", 10, 100)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)
    portfolio.add_asset(nvda)
    portfolio.add_asset(xiu)

    current_prices = {
        "VFV": 120,
        "NVDA": 180,
        "XIU": 60
    }

    actual = calculate_portfolio_weights(portfolio, current_prices)

    total_weight = sum(actual.values())

    assert total_weight == pytest.approx(1.0)



# ==============================================================================
# calculate_portfolio_return() TESTS
# ==============================================================================

def test_calculate_portfolio_return_with_multiple_assets():
    vfv = Asset("VFV", 5, 100)
    nvda = Asset("NVDA", 10, 100)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)
    portfolio.add_asset(nvda)

    current_prices = {
        "VFV": 120,
        "NVDA": 180
    }

    returns = {
        "VFV": 0.10,
        "NVDA": 0.20
    }

    actual = calculate_portfolio_return(portfolio, current_prices, returns)

    expected = (0.25 * 0.10) + (0.75 * 0.20)

    assert actual == pytest.approx(expected)


def test_calculate_portfolio_return_with_single_asset():
    vfv = Asset("VFV", 5, 100)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)

    current_prices = {
        "VFV": 120
    }

    returns = {
        "VFV": 0.10
    }

    actual = calculate_portfolio_return(portfolio, current_prices, returns)
 

    expected = 0.10

    assert actual == pytest.approx(expected)


def test_calculate_portfolio_return_with_negative_returns():
    vfv = Asset("VFV", 5, 100)
    nvda = Asset("NVDA", 5, 100)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)
    portfolio.add_asset(nvda)

    current_prices = {
        "VFV": 100,
        "NVDA": 100
    }

    returns = {
        "VFV": -0.10,
        "NVDA": -0.20
    }

    actual = calculate_portfolio_return(portfolio, current_prices, returns)

    expected = (0.50 * -0.10) + (0.50 * -0.20)

    assert actual == pytest.approx(expected)


def test_calculate_portfolio_return_with_zero_returns():
    vfv = Asset("VFV", 5, 100)
    nvda = Asset("NVDA", 5, 100)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)
    portfolio.add_asset(nvda)

    current_prices = {
        "VFV": 100,
        "NVDA": 100
    }

    returns = {
        "VFV": 0.0,
        "NVDA": 0.0
    }

    actual = calculate_portfolio_return(portfolio, current_prices, returns)

    expected = 0.0

    assert actual == pytest.approx(expected)


def test_calculate_portfolio_return_with_missing_return():
    vfv = Asset("VFV", 5, 100)
    nvda = Asset("NVDA", 10, 100)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)
    portfolio.add_asset(nvda)

    current_prices = {
        "VFV": 120,
        "NVDA": 180
    }

    returns = {
        "VFV": 0.10
    }

    with pytest.raises(ValueError):
        calculate_portfolio_return(portfolio, current_prices, returns)


# ==============================================================================
# calculate_covariance_matrix() TESTS
# ==============================================================================

def test_calculate_covariance_matrix_with_multiple_assets():
    returns = {
        "VFV": [0.02, -0.01, 0.03, 0.01],
        "NVDA": [0.04, -0.03, 0.06, 0.02]
    }

    actual = calculate_covariance_matrix(returns)

    expected = np.cov([
        [0.02, -0.01, 0.03, 0.01],
        [0.04, -0.03, 0.06, 0.02]
    ])

    np.testing.assert_allclose(actual, expected)


def test_calculate_covariance_matrix_with_single_asset():
    returns = {
        "VFV": [0.02, -0.01, 0.03, 0.01]
    }

    actual = calculate_covariance_matrix(returns)

    expected = np.cov([
        [0.02, -0.01, 0.03, 0.01]
    ])

    np.testing.assert_allclose(actual, expected)


def test_calculate_covariance_matrix_with_empty_returns():
    returns = {}

    with pytest.raises(ValueError):
        calculate_covariance_matrix(returns)


def test_calculate_covariance_matrix_with_single_observation():
    returns = {
        "VFV": [0.02],
        "NVDA": [0.04]
    }

    with pytest.raises(ValueError):
        calculate_covariance_matrix(returns)


def test_calculate_covariance_matrix_with_different_lengths():
    returns = {
        "VFV": [0.02, -0.01, 0.03],
        "NVDA": [0.04, -0.03]
    }

    with pytest.raises(ValueError):
        calculate_covariance_matrix(returns)


# ==============================================================================
# calculate_portfolio_variance() TESTS
# ==============================================================================

def test_calculate_portfolio_variance_with_multiple_assets():
    weights = {
        "VFV": 0.25,
        "NVDA": 0.75
    }

    covariance_matrix = np.array([
        [0.01, 0.002],
        [0.002, 0.04]
    ])

    actual = calculate_portfolio_variance(weights, covariance_matrix)

    expected = (
        0.25**2 * 0.01
        + 2 * 0.25 * 0.75 * 0.002
        + 0.75**2 * 0.04
    )

    assert actual == pytest.approx(expected)


def test_calculate_portfolio_variance_with_equal_weights():
    weights = {
        "VFV": 0.5,
        "NVDA": 0.5
    }

    covariance_matrix = np.array([
        [0.01, 0.0],
        [0.0, 0.01]
    ])

    actual = calculate_portfolio_variance(weights, covariance_matrix)

    expected = 0.005

    assert actual == pytest.approx(expected)


def test_calculate_portfolio_variance_with_single_asset():
    weights = {
        "VFV": 1.0
    }

    covariance_matrix = np.array([
        [0.04]
    ])

    actual = calculate_portfolio_variance(weights, covariance_matrix)

    expected = 0.04

    assert actual == pytest.approx(expected)


def test_calculate_portfolio_variance_with_empty_weights():
    weights = {}

    covariance_matrix = np.array([
        [0.01, 0.002],
        [0.002, 0.04]
    ])

    with pytest.raises(ValueError):
        calculate_portfolio_variance(weights, covariance_matrix)


def test_calculate_portfolio_variance_with_mismatched_dimensions():
    weights = {
        "VFV": 0.5,
        "NVDA": 0.5
    }

    covariance_matrix = np.array([
        [0.01, 0.002, 0.001],
        [0.002, 0.04, 0.003],
        [0.001, 0.003, 0.02]
    ])

    with pytest.raises(ValueError):
        calculate_portfolio_variance(weights, covariance_matrix)



# ==============================================================================
# calculate_portfolio_volatility() TESTS
# ==============================================================================

def test_calculate_portfolio_volatility():
    weights = {
        "VFV": 0.25,
        "NVDA": 0.75
    }

    covariance_matrix = np.array([
        [0.01, 0.002],
        [0.002, 0.04]
    ])

    actual = calculate_portfolio_volatility(weights, covariance_matrix)
    variance = (
        0.25**2 * 0.01
        + 2 * 0.25 * 0.75 * 0.002
        + 0.75**2 * 0.04
    )

    expected = np.sqrt(variance)

    assert actual == pytest.approx(expected)


def test_calculate_portfolio_volatility_with_single_asset():
    weights = {
        "VFV": 1.0
    }

    covariance_matrix = np.array([
        [0.04]
    ])

    actual = calculate_portfolio_volatility(weights, covariance_matrix)

    expected = 0.20

    assert actual == pytest.approx(expected)


def test_calculate_portfolio_volatility_with_zero_variance():
    weights = {
        "VFV": 0.5,
        "NVDA": 0.5
    }

    covariance_matrix = np.array([
        [0.0, 0.0],
        [0.0, 0.0]
    ])

    actual = calculate_portfolio_volatility(weights, covariance_matrix)

    expected = 0.0

    assert actual == pytest.approx(expected)


def test_calculate_portfolio_volatility_with_mismatched_dimensions():
    weights = {
        "VFV": 0.5,
        "NVDA": 0.5
    }

    covariance_matrix = np.array([
        [0.01, 0.002, 0.001],
        [0.002, 0.04, 0.003],
        [0.001, 0.003, 0.02]
    ])

    with pytest.raises(ValueError):
        calculate_portfolio_volatility(weights, covariance_matrix)