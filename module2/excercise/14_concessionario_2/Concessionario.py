from typing import List, Optional

from Veicolo import Veicolo
class Concessionario:
    def __init__(self, nome: str, lista_auto: List[Veicolo]):
        self._nome: Optional[str] = None
        self._lista_auto: List[Veicolo] = []
        self.nome = nome
        self.lista_auto = lista_auto

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if not isinstance(nome, str):
            raise TypeError("Il nome del concessionario deve essere una stringa")
        if not nome:
            raise ValueError("Il nome del concessionario non può essere vuoto")
        self._nome = nome

    @property
    def lista_auto(self) -> List[Veicolo]:
        return list(self._lista_auto)

    @lista_auto.setter
    def lista_auto(self, lista_auto: List[Veicolo]) -> None:
        if lista_auto is None:
            raise TypeError("La lista delle auto non può essere None")
        if not isinstance(lista_auto, list):
            raise TypeError("La lista delle auto deve essere una lista")
        for veicolo in lista_auto:
            if not isinstance(veicolo, Veicolo):
                raise TypeError("Tutti gli elementi devono essere istanze di Veicolo")
        self._lista_auto = list(lista_auto)
