import numpy as np


def calculate_volatility(returns):
    if len(returns) < 2:
        raise ValueError("Returns list must contain at least two elements to calculate volatility.")

    return np.std(returns, ddof=1)



def calculate_annualized_volatility(returns, periods_per_year = 252):
    if len(returns) < 2: 
        raise ValueError("Returns list must contain at least two elements to calculate annualized volatility.")

    if periods_per_year <= 0:
        raise ValueError("Periods per year must be a positiive integer.")

    period_volatility = calculate_volatility(returns)
    annualized_volatility = period_volatility * np.sqrt(periods_per_year)

    return annualized_volatility



def calculate_max_drawdown(prices):
    if len(prices) == 0:
        raise ValueError("Prices list cannot be empty.")

    peak = prices[0]
    max_drawdown = 0.0

    for price in prices:
        if price > peak:
            peak = price

        drawdown = (price - peak) / peak

        if drawdown < max_drawdown:
            max_drawdown = drawdown

    return max_drawdown


def calculate_sharpe_ratio(returns, risk_free_rate=0.0, periods_per_year=252):
    if len(returns) < 2: 
        raise ValueError("Returns list must contain at least two elements to calculate Sharpe ratio.")

    if periods_per_year <= 0:
        raise ValueError("Periods per year must be a positive nnumber.")

    excess_returns = np.array(returns) - risk_free_rate
    mean_excess_return = np.mean(excess_returns)
    volatility = calculate_volatility(excess_returns)

    if volatility == 0:
        raise ValueError("Volatility is zero, cannot calculate Sharpe ratio.")

    sharpe_ratio = (mean_excess_return / volatility) * np.sqrt(periods_per_year)


    return sharpe_ratio