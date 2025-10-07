class Auto:
    def __init__(self, marca : str, modello : str, anno : int, prezzo : float, sconto : int):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.prezzo = prezzo
        self._sconto = sconto

    def prezzo_scontato(self) :
        return self.prezzo - ((self.prezzo * self._sconto)/100)

    def show_info(self):
        print("Marca:", self.marca)
        print("Modello:", self.modello)
        print("Anno:", self.anno)
        print("Prezzo:", self.prezzo)
        print("Prezzo scontato:", self.prezzo_scontato())