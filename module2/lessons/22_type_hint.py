#Il codice funziona comunque ma abbiamo suggerimenti sui tipi

from typing import Union, Optional, List, Literal

def funzione_esempio(
        numero : Union[int, float],
        lista_numeri : List[int],
        operazione : Literal["addizione", "sottrazione", "moltiplicazione", "divisione", "potenza"],
        fattore : Optional[int] = None):
    match operazione :
        case "addizione":
            print(numero + sum(lista_numeri))
        case "sottrazione":
            print(numero - sum(lista_numeri))
        case "moltiplicazione":
            print(numero * sum(lista_numeri))
        case "divisione":
            print(numero / sum(lista_numeri))
        case "potenza":
            print(numero ** fattore if fattore else 1)
        case _:
            print("ERRORE")

funzione_esempio(numero=2, lista_numeri=[], operazione="potenza", fattore=3)
funzione_esempio(numero=2.4, lista_numeri=[2, 4], operazione="divisione")
funzione_esempio(numero=2.4, lista_numeri=[], operazione="asvsvasv", fattore=3)