class Pay:

    def __init__(self, first, second, days):
        self.first = int(first)
        self.second = float(second)
        self.days = int(days)

    def summa(self):
        return self.first / self.days * self.second

