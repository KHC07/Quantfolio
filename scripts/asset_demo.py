from quantfolio.models.asset import Asset


nvda = Asset(
    ticker="NVDA",
    shares=10,
    purchase_price=150
)


print(nvda.ticker)
print(nvda.shares)
print(nvda.purchase_price)