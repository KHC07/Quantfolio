import pandas as pd

from quantfolio.models.asset import Asset
from quantfolio.models.portfolio import Portfolio

from quantfolio.data.market_data import MarketDataProvider

from quantfolio.analytics.returns import calculate_returns

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
    # Define the portfolio holdings.
    vfv = Asset("VFV", 20, 120)
    nvda = Asset("NVDA", 10, 180)

    portfolio = Portfolio()
    portfolio.add_asset(vfv)
    portfolio.add_asset(nvda)

    provider = MarketDataProvider()

    # Download historical prices and align observations by trading date.
    vfv_data = provider.get_historical_prices("VFV")
    nvda_data = provider.get_historical_prices("NVDA")

    vfv_close_prices = vfv_data["Close"].squeeze()
    nvda_close_prices = nvda_data["Close"].squeeze()

    prices = pd.DataFrame({"VFV": vfv_close_prices, "NVDA": nvda_close_prices}).dropna()

    vfv_close_prices = prices["VFV"].tolist()
    nvda_close_prices = prices["NVDA"].tolist()

    # Calculate asset returns from the aligned price series.
    vfv_returns = calculate_returns(vfv_close_prices)
    nvda_returns = calculate_returns(nvda_close_prices)

    historical_returns = {
        "VFV": vfv_returns,
        "NVDA": nvda_returns,
    }

    # Use the latest closing prices for portfolio valuation.
    current_prices = {
        "VFV": vfv_close_prices[-1],
        "NVDA": nvda_close_prices[-1],
    }

    returns = {
        "VFV": vfv_returns[-1],
        "NVDA": nvda_returns[-1],
    }

    portfolio_value = calculate_portfolio_value(
        portfolio,
        current_prices,
    )

    portfolio_weights = calculate_portfolio_weights(
        portfolio,
        current_prices,
    )

    portfolio_return = calculate_portfolio_return(
        portfolio,
        current_prices,
        returns,
    )

    covariance_matrix = calculate_covariance_matrix(
        historical_returns,
    )

    portfolio_variance = calculate_portfolio_variance(
        portfolio_weights,
        covariance_matrix,
    )

    portfolio_volatility = calculate_portfolio_volatility(
        portfolio_weights,
        covariance_matrix,
    )

    historical_portfolio_returns = calculate_historical_portfolio_returns(
        portfolio_weights,
        historical_returns,
    )

    sharpe_ratio = calculate_sharpe_ratio(
        historical_portfolio_returns,
    )

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
    print(f"  Latest Portfolio Return: {portfolio_return:.2%}")

    print()
    print("Risk:")
    print(f"  Portfolio Variance:      {portfolio_variance:.6f}")
    print(f"  Portfolio Volatility:    {portfolio_volatility:.2%}")
    print(f"  Sharpe Ratio:             {sharpe_ratio:.2f}")

    print()
    print("=" * 45)


if __name__ == "__main__":
    main()