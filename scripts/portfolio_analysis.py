from quantfolio.models.asset import Asset
from quantfolio.models.portfolio import Portfolio

from quantfolio.analytics.portfolio import (
    calculate_portfolio_value,
    calculate_portfolio_weights,
    calculate_portfolio_return,
    calculate_covariance_matrix,
    calculate_portfolio_variance,
    calculate_portfolio_volatility,
    calculate_historical_portfolio_returns,
)

from quantfolio.analytics.risk import calculate_sharpe_ratio


def main():

    # Create assets
    vfv = Asset("VFV", 20, 120)
    nvda = Asset("NVDA", 10, 180)

    # Create portfolio
    portfolio = Portfolio()

    portfolio.add_asset(vfv)
    portfolio.add_asset(nvda)

    # Current market prices
    current_prices = {
        "VFV": 135,
        "NVDA": 200,
    }

    # Calculate portfolio value
    portfolio_value = calculate_portfolio_value(
        portfolio,
        current_prices
    )

    # Calculate portfolio weights
    portfolio_weights = calculate_portfolio_weights(
        portfolio,
        current_prices
    )

    # Current asset returns
    returns = {
        "VFV": 0.10,
        "NVDA": 0.20
    }

    # Calculate current portfolio return
    portfolio_return = calculate_portfolio_return(
        portfolio,
        current_prices,
        returns
    )

    # Historical returns for each asset
    historical_returns = {
        "VFV": [0.02, -0.01, 0.015, 0.01],
        "NVDA": [0.03, -0.02, 0.025, 0.04]
    }

    # Calculate covariance matrix
    covariance_matrix = calculate_covariance_matrix(
        historical_returns
    )

    # Calculate portfolio variance
    portfolio_variance = calculate_portfolio_variance(
        portfolio_weights,
        covariance_matrix
    )

    # Calculate portfolio volatility
    portfolio_volatility = calculate_portfolio_volatility(
        portfolio_weights,
        covariance_matrix
    )

    # Calculate historical portfolio returns
    historical_portfolio_returns = calculate_historical_portfolio_returns(
        portfolio_weights,
        historical_returns
    )

    # Calculate Sharpe ratio
    sharpe_ratio = calculate_sharpe_ratio(
        historical_portfolio_returns
    )

    # Display portfolio report
    print()
    print("=" * 45)
    print("        QUANTFOLIO PORTFOLIO ANALYSIS")
    print("=" * 45)

    print()
    print(f"Portfolio Value: ${portfolio_value:,.2f}")

    print()
    print("Portfolio Allocation:")

    for ticker, weight in portfolio_weights.items():
        print(f"  {ticker}: {weight:.2%}")

    print()
    print("Performance:")
    print(f"  Portfolio Return:     {portfolio_return:.2%}")

    print()
    print("Risk:")
    print(f"  Portfolio Variance:   {portfolio_variance:.6f}")
    print(f"  Portfolio Volatility: {portfolio_volatility:.2%}")
    print(f"  Sharpe Ratio:         {sharpe_ratio:.2f}")

    print()
    print("=" * 45)


if __name__ == "__main__":
    main()