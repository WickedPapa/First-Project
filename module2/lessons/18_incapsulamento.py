#l'incapsulamento è convenzionale in python...

#con un underscore _ davanti al nome dell'attributo diciamo che quell'attributo non dovrebbe essere modificato direttamente
#con 2 underscore __ davanti al nome dell'attributo quell'attributo utilizza il name mangling che rende l'attributo meno accessibile

class Account:
    def __init__(self, nome : str, balance : int, password : str):
        self.nome = nome
        self._balance = balance #indica che l'attributo è privato
        self.__password = password #qui usiamo il name mangling

account1 = Account("Paolo", 500, "MyPsw")
print(account1.nome)
print(account1._balance) #pycharm segnala il warning ma nulla mi impedisce di accedere comunque

#print(account1.__password) questo causa un errore AttributeError: 'Account' object has no attribute '__password'
#perchè python rinomina il campo quando usiamo il name mangling in _Nomeclasse__campo

#esiste comunque un modo sconsigliato per accedere:
print(account1._Account__password)
