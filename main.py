from pay import Pay


def read():
    earn = float(input("Введіть оклад: "))
    worked_days = int(input("Введіть відпрацьовані дні:"))
    get = Pay()
    get.set_first(earn)
    get.set_second(worked_days)
    return get.summa()


def display():
    print(read())


display()
