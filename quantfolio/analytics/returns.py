import math



def calculate_returns(prices):
    if len(prices) < 2:
        return []

    returns = []

    for i in range(1, len(prices)):
        previous_price = prices[i - 1]
        current_price = prices[i]

        if previous_price <= 0:
            raise ValueError("Previous price cannot be zero or negative")

        if current_price <= 0:
            raise ValueError("Current price cannot be zero or negative")

        period_return = (current_price - previous_price) / previous_price
        returns.append(period_return)
        
    return returns



def calculate_cumulative_returns(returns):
    cumulative_returns = []
    cumulative_return = 1.0

    for period_return in returns:
        cumulative_return *= (1 + period_return)
        cumulative_returns.append(cumulative_return - 1)

    return cumulative_returns



def calculate_total_return(prices):
    if len(prices) < 2:
        return 0.0

    for price in prices:
        if price <= 0:
            raise ValueError("Prices must be greater than zero")

    starting_price = prices[0]
    final_price = prices[-1]

    total_return = (final_price - starting_price) / starting_price

    return total_return



def calculate_annualized_return(prices, periods_per_year):
    if periods_per_year <= 0:
        raise ValueError("Periods per year must be greater than zero")

    if len(prices) < 2:
        return 0.0

    total_return = calculate_total_return(prices)
    num_periods = len(prices) - 1
    annualized_return = (1 + total_return) ** (periods_per_year / num_periods) - 1

    return annualized_return



def calculate_log_returns(prices):
    if len(prices) < 2:
        return []

    log_returns = []

    for i in range(1, len(prices)):
        previous_price = prices[i - 1]
        current_price = prices[i]

        if previous_price <= 0:
            raise ValueError("Previous price must be greater than zero for log returns")

        if current_price <= 0:
            raise ValueError("Current price must be greater than zero for log returns")

        period_log_return = math.log(current_price / previous_price)
        log_returns.append(period_log_return)

    return log_returns