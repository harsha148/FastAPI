from src.businessobjects.stock import stock


class stock_repository:
    def __init__(self,all_stocks):
        self.all_stocks = [stock(1,'Reddit',123)]

    def get_all_stocks(self) -> list[stock]:
        return self.all_stocks
