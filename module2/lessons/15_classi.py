#in Python anche stringhe, numeri e liste sono oggetti

class SenzaParam:
    pass

senzaParam = SenzaParam()
senzaParam.marca = "Fiat"
senzaParam.modello = "Panda"

print(senzaParam, senzaParam.marca, senzaParam.modello)

#questo funziona ma ovviamente non si fa

class Auto:
    
    def __init__(self, marca, modello, colore, anno):
        self.marca = marca
        self.modello = modello
        self.colore = colore
        self.anno = anno


auto1 = Auto("Fiat", "Panda", "Verde", 1995)
auto2 = Auto("Toyota", "Yaris", "Rossa", 2022)

print(auto1, auto1.marca, auto1.modello, auto1.colore, auto1.anno)
print(auto2, auto2.marca, auto2.modello, auto2.colore, auto2.anno)
