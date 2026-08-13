from quantfolio.models.asset import Asset


def test_asset_creation():
    asset = Asset(ticker="NVDA", shares=10, purchase_price=150)

    assert asset.ticker == "NVDA"
    assert asset.shares == 10
    assert asset.purchase_price == 150
    ## checks that the information is true 

def test_cost_basis():
    asset = Asset(ticker="NVDA", shares=10, purchase_price=150)

    assert asset.calculate_cost_basis() == 1500