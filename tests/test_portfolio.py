from quantfolio.models.asset import Asset
from quantfolio.models.portfolio import Portfolio

def test_empty_portfolio():
    portfolio = Portfolio()

    assert len(portfolio.asset) == 0


def test_add_asset(): 
    portfolio = Portfolio()

    asset = Asset("NVDA", 10, 150)

    portfolio.add_asset(asset)

    assert len(portfolio.asset) == 1
    assert portfolio.assets[0] == asset


def test_total_cost_basis(): 
    portfolio = Portfolio()

    nvda  = Asset('NVDA', 10, 150)
    vfv = Asset('VFV', 20, 120)

    portfolio.add_asset(nvda,vfv)

    assert portfolio.total_cost_basis() == 3900 

