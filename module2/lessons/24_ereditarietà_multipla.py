#E' una pratica sconsigliata. E' di gran lunga preferibile usare la composizione

class Mamma:
    def __init__(self, occhi_mamma, capelli_mamma):
        self.occhi_mamma = occhi_mamma
        self.capelli_mamma = capelli_mamma

class Papa:
    def __init__(self, occhi_papa, capelli_papa):
        self.occhi_papa = occhi_papa
        self.capelli_papa = capelli_papa

class Figlio(Papa, Mamma):
    def __init__(self, occhi_mamma, capelli_papa):
        Papa.__init__(self, None, capelli_papa)
        Mamma.__init__(self, occhi_mamma, None)

    def show_info(self):
        return f"Occhi: {self.occhi_mamma}, Capelli: {self.capelli_papa}"

if __name__ == '__main__':
    papa = Papa("Castani", "Biondi")
    mamma = Mamma("Azzurri", "Castani")
    roberto = Figlio(mamma.occhi_mamma, papa.capelli_papa)
    print(roberto.show_info())