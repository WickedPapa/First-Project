from Veicolo import Veicolo


class Camion(Veicolo):
    def __init__(self, marca, modello, anno, prezzo, capacita_carico):
        super().__init__(marca, modello, anno, prezzo)
        self.capacita_carico = capacita_carico
