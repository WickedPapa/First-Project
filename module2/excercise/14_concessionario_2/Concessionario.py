from typing import List

from Veicolo import Veicolo
class Concessionario:
    def __init__(self, nome : str, lista_auto : List[Veicolo]):
        self.nome = nome
        self.lista_auto = lista_auto

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nome : str):
        self.nome = nome

    @property
    def lista_auto(self):
        return self.lista_auto

    @lista_auto.setter
    def lista_auto(self, lista_auto : List[Veicolo]):
        self.lista_auto = lista_auto