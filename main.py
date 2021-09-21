class Pay:

    def __init__(self, first, second, days):
        self.first = int(first)
        self.second = float(second)
        self.days = int(days)

    def summa(self):
        return self.first / self.days * self.second
while True:
    try:
        oklad = input("Введіть оклад: ")
        worked_days = input("Введіть відпрацьовані дні:")
        days_in = input("Введіть дні у місяці: ")

        working = Pay(oklad, worked_days, days_in)

        print(working.summa())
    except:
        print("Введіть інші числа")