class Portfolio: 
    def __init__(self):
        self.assets = []
    ## creates the list for the assets to get stored

    def add_asset(self, asset): 
        self.assets.append(asset)
    ## adds the assets into a list

    def total_cost_basis(self): 
        total = 0

        for asset in self.assets: 
            total += asset.calculate_cost_basis()

        return total
    ## adds all the total cost of each asset