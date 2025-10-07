from typing import List

from Auto import Auto
from Concessionario import Concessionario

def stampa_trovate(trovate : List[Auto]):
    for auto in trovate:
        auto.show_info()

if __name__ == '__main__':
    panda = Auto("FIAT", "PANDA", 2020, 11999, 10)
    punto = Auto("FIAT", "PUNTO", 2019, 10000, 0)
    concessionario = Concessionario([panda])
    concessionario.descrizione_servizio()
    print("")
    concessionario.aggiungi_auto(punto)
    concessionario.mostra_auto()
    print("")
    stampa_trovate(concessionario.cerca_auto(marca="FIAT"))
    print("")
    stampa_trovate(concessionario.cerca_auto(modello="PUNTO"))
    print("")
    stampa_trovate(concessionario.cerca_auto())
    print("")
    stampa_trovate(concessionario.cerca_auto(marca="FIAT", modello="PUNTO"))
    print("")
    concessionario.vendi_auto(marca="FIAT", modello="PUNTO")
    print("")
    stampa_trovate(concessionario.cerca_auto(marca="FIAT", modello="PUNTO"))
    print("")
    concessionario.mostra_auto()