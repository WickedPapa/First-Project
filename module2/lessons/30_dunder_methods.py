#dunder sta per double-underscore
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account di {self.name} con saldo {self.balance} euro"


    #descrizione dettagliata per debug
    def __repr__(self):
        return f"Account('{self.name}', '{self.balance}')"

    def __add__(self, other): #definisce il comportamento dell'operatore +
        if isinstance(other, Account):
            return Account(self.name, self.balance + other.balance)
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Account):
            return self.name == other.name and self.balance == other.balance
        return False

    def __lt__(self, other): #definisce il comportamento dell'operatore <
        if isinstance(other, Account):
            return self.balance < other.balance
        raise TypeError

    def __gt__(self, other): #definisce il comportamento dell'operatore >
        if isinstance(other, Account):
            return self.balance > other.balance
        raise TypeError

    def __le__(self, other): #definisce il comportamento dell'operatore <=
        if isinstance(other, Account):
            return self.balance <= other.balance
        raise TypeError

    def __ge__(self, other): #definisce il comportamento dell'operatore >=
        if isinstance(other, Account):
            return self.balance >= other.balance
        raise TypeError

if __name__ == '__main__':

    account = Account("Paolo", 100)
    account_2 = Account("Marta", 200)

    print(account)
    print(str(account_2))
    print(repr(account_2))

    account_3 = account + account_2
    print(account_3)

    print(account == account_2)
    print(account_2 <= account_3)