class Studente:

    ore_settimanali = 36
    ore_presenza = 0

    def __init__(self, nome, cognome, corso_di_studi):
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi
        Studente.ore_presenza += 1

    #metodo di istanza
    def scheda_personale(self):
        return f"Nome: {self.nome} Cognome: {self.cognome} Corso: {self.corso_di_studi}"

    def studia(self):
        print(f"Lo studente {self.nome} sta studiando")

studente1 = Studente("Paolo", "Montano", "Corso Python")
studente2 = Studente("Mario", "Rossi", "Corso Cucina")

print(studente1.scheda_personale())
print(studente2.scheda_personale())

print(studente1.ore_presenza) #stampa 2 perchè quella variabile di classe viene aumentata di uno ogni volta che uno studente viene creato

studente1.studia()