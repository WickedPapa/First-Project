from Veicolo import Veicolo


class Auto(Veicolo):
    def __init__(self, marca, modello, anno, prezzo, numero_porte):
        super().__init__(marca, modello, anno, prezzo)
        self.numero_porte = numero_porte
