class Auto:

    #variabili di classe
    varibile_di_classe = "VEICOLO"

    #metodo init o costruttore
    def __init__(self, marca, modello, colore, anno):
        # variabili di classe o di istanza
        self.marca = marca
        self.modello = modello
        self.colore = colore
        self.anno = anno


auto1 = Auto("Fiat", "Panda", "Verde", 1995)
auto2 = Auto("Toyota", "Yaris", "Rossa", 2022)

print(auto1, auto1.marca, auto1.modello, auto1.colore, auto1.anno)
print(auto2, auto2.marca, auto2.modello, auto2.colore, auto2.anno)

print(auto1.varibile_di_classe, auto2.varibile_di_classe)
Auto.varibile_di_classe = "MOTORE"
print(auto1.varibile_di_classe, auto2.varibile_di_classe)

del auto1.marca
#print(auto1.marca) darebbe errore perche abbiamo cancellato l'attributo marca per l'istanza auto1