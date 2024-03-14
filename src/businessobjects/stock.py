class stock:
    def __init__(self, stock_id:int, name:str, price:float):
        self.stock_id = stock_id
        self.stock_name = name
        self.current_price = price

    def get_stock_current_price(self):
        return self.current_price

    def update_stock_current_price(self, price:float):
        self.current_price = price

