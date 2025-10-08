from Veicolo import Veicolo
class Camion(Veicolo):

    def __init__(self, marca, modello, anno, prezzo, capacita_carico):
        super().marca = marca
        super().modello = modello
        super().anno = anno
        super().prezzo = prezzo
        self.capacita_carico = capacita_carico