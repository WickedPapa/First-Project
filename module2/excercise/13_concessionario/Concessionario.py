from typing import List, Optional

from Auto import Auto

class Concessionario:

    tipo_concessionario : str = "Vendita Auto"

    def __init__(self, lista_auto : List[Auto]):
        self.lista_auto = lista_auto

    def aggiungi_auto(self, auto : Auto) :
        self.lista_auto.append(auto)

    def mostra_auto(self):
        for auto in self.lista_auto:
            auto.show_info()

    def cerca_auto(self, marca: Optional[str] = None, modello: Optional[str] = None):
        match marca, modello:
            case None, None:
                return self.lista_auto
            case _, None:
                return [auto for auto in self.lista_auto if auto.marca == marca]
            case None, _:
                return [auto for auto in self.lista_auto if auto.modello == modello]
            case _:
                return [auto for auto in self.lista_auto if auto.marca == marca and auto.modello == modello]

    def vendi_auto(self, marca: str, modello: str):
        trovate = self.cerca_auto(marca, modello)
        if trovate:
            self.lista_auto.remove(trovate[0])
            print("Auto Rimossa")
        else:
            print("Auto non trovata")

    def descrizione_servizio(self):
        print("Benvenuti al concessionario. Servizi offerti:", self.tipo_concessionario)