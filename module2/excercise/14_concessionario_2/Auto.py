from Veicolo import Veicolo
class Auto(Veicolo):

    def __init__(self, marca, modello, anno, prezzo, numero_porte):
        super().marca = marca
        super().modello = modello
        super().anno = anno
        super().prezzo = prezzo
        self.numero_porte = numero_porte