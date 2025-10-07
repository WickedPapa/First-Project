#E' una pratica sconsigliata. E' di gran lunga preferibile usare la composizione

class Mamma:
    def __init__(self, occhi_mamma, capelli_mamma):
        self.occhi_mamma = occhi_mamma
        self.capelli_mamma = capelli_mamma

class Papa:
    def __init__(self, occhi_papa, capelli_papa):
        self.occhi_papa = occhi_papa
        self.capelli_papa = capelli_papa

class Figlio:
    def __init__(self, papa, mamma):
        self.occhi = mamma.occhi_mamma
        self.capelli = papa.capelli_papa

    def show_info(self):
        return f"Occhi: {self.occhi}, Capelli: {self.capelli}"

if __name__ == '__main__':
    papa = Papa("Castani", "Biondi")
    mamma = Mamma("Azzurri", "Castani")
    roberto = Figlio(papa, mamma)
    print(roberto.show_info())