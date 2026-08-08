class Asset:

    def __init__(self, ticker, shares, purchase_price):
        self.ticker = ticker
        self.shares = shares
        self.purchase_price = purchase_price

    def calculate_cost_basis(self): 
        return self.shares * self.purchase_price