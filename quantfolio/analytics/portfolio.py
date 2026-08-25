from quantfolio.models import portfolio
import numpy as np


def calculate_portfolio_value(portfolio, current_prices):
    total_value = 0

    for asset in portfolio.assets:
        if asset.ticker not in current_prices:
            raise ValueError(f"Current price for {asset.ticker} not found.")

        total_value += asset.shares * current_prices[asset.ticker]

    return total_value



def calculate_portfolio_weights(portfolio, current_prices):
    total_value = calculate_portfolio_value(portfolio, current_prices)
    weights = {}

    for asset in portfolio.assets:
        if total_value == 0:
            weights[asset.ticker] = 0
        else:
            weights[asset.ticker] = (asset.shares * current_prices[asset.ticker]) / total_value

    return weights



def calculate_portfolio_return(portfolio, current_prices, returns):
    weights = calculate_portfolio_weights(portfolio, current_prices)
    portfolio_return = 0.0

    for asset in portfolio.assets:
        if asset.ticker not in returns:
            raise ValueError(f"Return for {asset.ticker} not found.")

        portfolio_return += weights[asset.ticker] * returns[asset.ticker]

    return portfolio_return



def calculate_covariance_matrix(returns):
    if len(returns) == 0:
        raise ValueError("Returns cannot be empty.")

    return_series = list(returns.values())

    first_length = len(return_series[0])

    if first_length < 2:
        raise ValueError("Each return series must contain at least two observations.")

    for series in return_series:
        if len(series) != first_length:
            raise ValueError("All return series must have the same length.")

    returns_array = np.array(return_series)

    covariance_matrix = np.cov(returns_array)

    return covariance_matrix



def calculate_portfolio_variance(weights, covariance_matrix):
    if len(weights) == 0:
        raise ValueError("Weights cannot be empty.")

    if len(weights) != covariance_matrix.shape[0]:
        raise ValueError("Number of weights must match the number of assets in the covariance matrix.")
    
    weights_array = np.array(list(weights.values()))

    portfolio_variance = weights_array.T @ covariance_matrix @ weights_array

    return portfolio_variance


def calculate_portfolio_volatility(weights, covariance_matrix):
    portfolio_variance = calculate_portfolio_variance(weights, covariance_matrix)
    portfolio_volatility = np.sqrt(portfolio_variance)

    return portfolio_volatility