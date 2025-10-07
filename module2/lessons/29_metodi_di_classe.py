class Persona:
    def __init__(self, nome, cognome, eta, residenza):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.residenza = residenza

    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.eta}
        Residenza: {self.residenza}\n"""
        return scheda

    def modifica_scheda(self):
        print("""Modifica scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza""")
        scelta = input("Cosa desideri modificare?")
        if scelta == "1":
            self.nome = input("Nome: ")
        elif scelta == "2":
            self.cognome = input("Cognome: ")
        elif scelta == "3":
            self.eta = input("Eta: ")
        elif scelta == "4":
            self.residenza = input("Residenza: ")

    @classmethod
    def from_string(cls, string, *args):
        nome, cognome, eta, residenza = string.split("-")
        return cls(nome, cognome, eta, residenza, *args)

##################################################################################

class Studente(Persona):
    profilo = "Studente"

    def __init__(self, nome, cognome, eta, residenza, corso_di_studi):
        super().__init__(nome, cognome, eta, residenza)
        self.corso_di_studi = corso_di_studi

    def scheda_personale(self):
        scheda = f"""
        Profilo: {Studente.profilo}
        Corso di Studi: {self.corso_di_studi}
        """
        return super().scheda_personale() + scheda

    def cambio_corso(self, corso):
        self.corso_di_studi = corso
        print("Corso Aggiornato")

##################################################################################

class Insegnante(Persona):
    profilo = "Insegnante"
    def __init__(self, nome, cognome, eta, residenza, materie=None):
        super().__init__(nome, cognome, eta, residenza)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie

    def scheda_personale(self):
        scheda = f"""
        Profilo: {Insegnante.profilo}
        Materie insegnate: {self.materie}
        """
        return super().scheda_personale() + scheda

##################################################################################

if __name__ == '__main__':
    iron_man_string = "Tony-Stark-40-Torre Stark"

    iron_man = Persona.from_string(iron_man_string)
    print(iron_man.scheda_personale())

    insegnante = Insegnante.from_string(iron_man_string) #avrebbe funzionato anche senza *args perchè materie ha default None
    print(insegnante.scheda_personale())

    studente = Studente.from_string(iron_man_string, "Informatica") #funziona solo perchè ho args
    print(studente.scheda_personale())