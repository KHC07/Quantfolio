import pytest
import math
from quantfolio.analytics.returns import (
    calculate_annualized_return,
    calculate_log_returns,
    calculate_returns,
    calculate_total_return,
    calculate_cumulative_returns,
)


# ==============================================================================
# calculate_returns() TESTS
# ==============================================================================

def test_calculate_returns_with_positive_returns():
    prices = [100, 110, 120, 130]

    actual = calculate_returns(prices)
    expected = [0.1, 0.09090909090909091, 0.08333333333333333]

    assert actual == pytest.approx(expected)


def test_calculate_returns_with_negative_returns():
    prices = [100, 90, 80, 70]

    actual = calculate_returns(prices)
    expected = [-0.1, -0.1111111111111111, -0.125]

    assert actual == pytest.approx(expected)


def test_calculate_returns_with_single_price():
    prices = [100]

    actual = calculate_returns(prices)
    expected = []

    assert actual == pytest.approx(expected)


def test_calculate_returns_with_empty_prices():
    prices = []

    actual = calculate_returns(prices)
    expected = []

    assert actual == pytest.approx(expected)


def test_calculate_returns_with_no_change_in_prices():
    prices = [100, 100, 100]

    actual = calculate_returns(prices)
    expected = [0.0, 0.0]

    assert actual == pytest.approx(expected)


def test_calculate_returns_with_zero_price():
    prices = [100, 0, 50]

    with pytest.raises(ValueError):
        calculate_returns(prices)


def test_calculate_returns_with_negative_price():
    prices = [100, -50, 75]

    with pytest.raises(ValueError):
        calculate_returns(prices)


# ==============================================================================
# calculate_cumulative_returns() TESTS
# ==============================================================================

def test_calculate_cumulative_returns_with_positive_returns():
    returns = [0.1, 0.2, 0.15]

    actual = calculate_cumulative_returns(returns)
    expected = [0.1, 0.32, 0.518]

    assert actual == pytest.approx(expected)


def test_calculate_cumulative_returns_with_positive_and_negative_returns():
    returns = [0.1, -0.2, 0.15]

    actual = calculate_cumulative_returns(returns)
    expected = [0.1, -0.12, 0.012]

    assert actual == pytest.approx(expected)

def test_calculate_cumulative_returns_with_no_change():
    returns = [0.0, 0.0, 0.0]

    actual = calculate_cumulative_returns(returns)
    expected = [0.0, 0.0, 0.0]

    assert actual == pytest.approx(expected)

def test_calculate_cumulative_returns_with_empty_returns():
    returns = []

    actual = calculate_cumulative_returns(returns)
    expected = []

    assert actual == pytest.approx(expected)


# ==============================================================================
# calculate_total_returns() TESTS
# ==============================================================================

def test_calculate_total_return_with_positive_returns():
    prices = [100, 110, 120, 130]

    actual = calculate_total_return(prices)
    expected = 0.3

    assert actual == pytest.approx(expected)

def test_calculate_total_return_with_negative_returns():
    prices = [100, 90, 80, 70]

    actual = calculate_total_return(prices)
    expected = -0.3

    assert actual == pytest.approx(expected)

def test_calculate_total_return_with_no_change():
    prices = [100, 100, 100]

    actual = calculate_total_return(prices)
    expected = 0.0

    assert actual == expected

def test_calculate_total_return_with_single_price():
    prices = [100]

    actual = calculate_total_return(prices)
    expected = 0.0

    assert actual == expected

def test_calculate_total_return_with_empty_prices():
    prices = []

    actual = calculate_total_return(prices)
    expected = 0.0

    assert actual == expected

def test_calculate_total_return_with_invalid_prices():
    prices = [100, 0, 50]

    with pytest.raises(ValueError):
        calculate_total_return(prices)

def test_calculate_total_return_with_negative_prices():
    prices = [100, -50, 75]

    with pytest.raises(ValueError):
        calculate_total_return(prices)


# ==============================================================================
# calculate_annualized_returns() TESTS
# ==============================================================================

def test_calculate_annualized_returns_with_one_year(): 
    prices = [100, 130]
    periods_per_year = 1

    actual = calculate_annualized_return(prices, periods_per_year)
    expected = 0.3
    
    assert actual == pytest.approx(expected)

def test_calculate_annualized_returns_with_multiple_years():
    prices = [100, 110, 120, 130]
    periods_per_year = 4

    actual = calculate_annualized_return(prices, periods_per_year)
    expected = (1 + 0.3) ** (4 / 3) - 1 

    assert actual == pytest.approx(expected)

def test_calculate_annualized_returns_with_negative_returns():
    prices = [100, 70]
    periods_per_year = 1

    actual = calculate_annualized_return(prices, periods_per_year)
    expected = -0.3

    assert actual == pytest.approx(expected)

def test_calculate_annualized_returns_with_single_price():
    prices = [100]
    periods_per_year = 12

    actual = calculate_annualized_return(prices, periods_per_year)
    expected = 0.0

    assert actual == pytest.approx(expected)

def test_calculate_annualized_returns_with_zero_periods_per_year():
    prices = [100, 110, 120, 130]
    periods_per_year = 0

    with pytest.raises(ValueError):
        calculate_annualized_return(prices, periods_per_year)

def test_calculate_annualized_returns_with_negative_periods_per_year():
    prices = [100, 110, 120, 130]
    periods_per_year = -1

    with pytest.raises(ValueError):
        calculate_annualized_return(prices, periods_per_year)

def test_calculate_annualized_returns_with_empty_prices():
    prices = []
    periods_per_year = 12

    actual = calculate_annualized_return(prices, periods_per_year)
    expected = 0.0

    assert actual == pytest.approx(expected)


# ==============================================================================
# calculate_log_returns() TESTS
# ==============================================================================

def test_calculate_log_returns_with_positive_returns():
    prices = [100, 110, 120, 130]

    actual = calculate_log_returns(prices)
    expected = [math.log(110 / 100), math.log(120 / 110), math.log(130 / 120)]

    assert actual == pytest.approx(expected)

def test_calculate_log_returns_with_negative_returns():
    prices = [100, 90, 80, 70]

    actual = calculate_log_returns(prices)
    expected = [math.log(90 / 100), math.log(80 / 90), math.log(70 / 80)]

    assert actual == pytest.approx(expected)

def test_calculate_log_returns_with_no_change():
    prices = [100, 100, 100]

    actual = calculate_log_returns(prices)
    expected = [0.0, 0.0]

    assert actual == pytest.approx(expected)

def test_calculate_log_returns_with_empty_prices():
    prices = []

    actual = calculate_log_returns(prices)
    expected = []

    assert actual == expected

def test_calculate_log_returns_with_invalid_prices():
    prices = [100, 0, 50]

    with pytest.raises(ValueError):
        calculate_log_returns(prices)

def test_calculate_log_returns_with_negative_prices():
    prices = [100, -50, 75]

    with pytest.raises(ValueError):
        calculate_log_returns(prices)