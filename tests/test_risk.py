import pytest
import numpy as np

from quantfolio.analytics.risk import (
    calculate_annualized_volatility,
    calculate_volatility,
    calculate_max_drawdown,
    calculate_sharpe_ratio)


# ==============================================================================
# calculate_volatility() TESTS
# ==============================================================================

def test_calculate_volatility_with_positive_returns():
    returns = [0.1, 0.2, 0.15, 0.05]

    actual = calculate_volatility(returns)
    expected = 0.06454972243679029

    assert actual == pytest.approx(expected)


def test_calculate_volatility_with_negative_returns():
    returns = [-0.1, -0.2, -0.15, -0.05]

    actual = calculate_volatility(returns)
    expected = 0.06454972243679029

    assert actual == pytest.approx(expected)


def test_calculate_volatility_with_no_variation():
    returns = [0.1, 0.1, 0.1, 0.1]

    actual = calculate_volatility(returns)
    expected = 0.0

    assert actual == pytest.approx(expected)


def test_calculate_volatility_with_single_return():
    returns = [0.1]

    with pytest.raises(ValueError):
        calculate_volatility(returns)


def test_calculate_volatility_with_empty_returns():
    returns = []

    with pytest.raises(ValueError):
        calculate_volatility(returns)


# ==============================================================================
# calculate_annualized_volatility() TESTS
# ==============================================================================

def test_calculate_annualized_volatility_with_default_periods():
    returns = [0.1, 0.2, 0.15, 0.05]

    actual = calculate_annualized_volatility(returns)
    expected = 0.06454972243679029 * np.sqrt(252)

    assert actual == pytest.approx(expected)


def test_calculate_annualized_volatility_with_custom_periods():
    returns = [0.1, 0.2, 0.15, 0.05]
    periods_per_year = 12

    actual = calculate_annualized_volatility(
        returns,
        periods_per_year
    )

    expected = 0.06454972243679029 * np.sqrt(12)

    assert actual == pytest.approx(expected)


def test_calculate_annualized_volatility_with_no_variation():
    returns = [0.1, 0.1, 0.1, 0.1]

    actual = calculate_annualized_volatility(returns)
    expected = 0.0

    assert actual == pytest.approx(expected)


def test_calculate_annualized_volatility_with_insufficient_returns():
    returns = [0.1]

    with pytest.raises(ValueError):
        calculate_annualized_volatility(returns)


def test_calculate_annualized_volatility_with_invalid_periods_per_year():
    returns = [0.1, 0.2, 0.15]

    with pytest.raises(ValueError):
        calculate_annualized_volatility(returns, 0)

    with pytest.raises(ValueError):
        calculate_annualized_volatility(returns, -1)


# ==============================================================================
# calculate_max_drawdown() TESTS
# ==============================================================================

def test_calculate_max_drawdown_with_decline():
    prices = [100, 120, 90, 110]

    actual = calculate_max_drawdown(prices)
    expected = -0.25

    assert actual == pytest.approx(expected)


def test_calculate_max_drawdown_with_multiple_declines():
    prices = [100, 120, 90, 130, 100]

    actual = calculate_max_drawdown(prices)
    expected = -0.25

    assert actual == pytest.approx(expected)


def test_calculate_max_drawdown_with_no_decline():
    prices = [100, 110, 120, 130]

    actual = calculate_max_drawdown(prices)
    expected = 0.0

    assert actual == pytest.approx(expected)


def test_calculate_max_drawdown_with_constant_prices():
    prices = [100, 100, 100, 100]

    actual = calculate_max_drawdown(prices)
    expected = 0.0

    assert actual == pytest.approx(expected)


def test_calculate_max_drawdown_with_single_price():
    prices = [100]

    actual = calculate_max_drawdown(prices)
    expected = 0.0

    assert actual == pytest.approx(expected)


def test_calculate_max_drawdown_with_empty_prices():
    prices = []

    with pytest.raises(ValueError):
        calculate_max_drawdown(prices)


def test_calculate_max_drawdown_with_recovery():
    prices = [100, 120, 90, 120]

    actual = calculate_max_drawdown(prices)
    expected = -0.25

    assert actual == pytest.approx(expected)


    # ==============================================================================
# calculate_sharpe_ratio() TESTS
# ==============================================================================

def test_calculate_sharpe_ratio_with_positive_returns():
    returns = [0.10, 0.20, 0.15, 0.05]

    actual = calculate_sharpe_ratio(
        returns,
        risk_free_rate=0.0,
        periods_per_year=252
    )

    mean_return = np.mean(returns)
    volatility = 0.06454972243679029

    expected = (
        mean_return / volatility
    ) * np.sqrt(252)

    assert actual == pytest.approx(expected)


def test_calculate_sharpe_ratio_with_risk_free_rate():
    returns = [0.10, 0.20, 0.15, 0.05]
    risk_free_rate = 0.03

    actual = calculate_sharpe_ratio(
        returns,
        risk_free_rate=risk_free_rate,
        periods_per_year=252
    )

    mean_excess_return = np.mean(returns) - risk_free_rate
    volatility = 0.06454972243679029

    expected = (
        mean_excess_return / volatility
    ) * np.sqrt(252)

    assert actual == pytest.approx(expected)


def test_calculate_sharpe_ratio_with_negative_returns():
    returns = [-0.10, -0.20, -0.15, -0.05]

    actual = calculate_sharpe_ratio(
        returns,
        risk_free_rate=0.0,
        periods_per_year=252
    )

    mean_return = np.mean(returns)
    volatility = 0.06454972243679029

    expected = (
        mean_return / volatility
    ) * np.sqrt(252)

    assert actual == pytest.approx(expected)


def test_calculate_sharpe_ratio_with_insufficient_returns():
    returns = [0.10]

    with pytest.raises(ValueError):
        calculate_sharpe_ratio(returns)


def test_calculate_sharpe_ratio_with_invalid_periods_per_year():
    returns = [0.10, 0.20, 0.15]

    with pytest.raises(ValueError):
        calculate_sharpe_ratio(
            returns,
            periods_per_year=0
        )

    with pytest.raises(ValueError):
        calculate_sharpe_ratio(
            returns,
            periods_per_year=-1
        )


def test_calculate_sharpe_ratio_with_zero_volatility():
    returns = [0.10, 0.10, 0.10, 0.10]

    with pytest.raises(ValueError):
        calculate_sharpe_ratio(returns)