from sys import exit


class Pay:
    def __init__(self):
        self.__second = 1
        self.__first = 1

    def set_first(self, first):
        if first > 0:
            self.__first = first
        else:
            exit("Введіть додатнє число")

    def set_second(self, second):
        if second > 0:
            self.__second = second
        else:
            exit("Введіть додатнє число")

    def get_first(self):
        return self.__first

    def get_second(self):
        return self.__second

    def summa(self):
        get_paid = (float(self.__first) / 30)
        get_paid2 = get_paid * int(self.__second)
        return get_paid2
