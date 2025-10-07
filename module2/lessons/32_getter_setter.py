class Account:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance must be positive")
        self._balance = value

    @balance.deleter
    def balance(self):
        del self._balance

if __name__ == '__main__':

    a = Account("Paolo", 243)
    print(a.balance)
    a.balance = 200
    print(a.balance)
    # a.balance = -200 Errore
    del a.balance
    print(a.balance)