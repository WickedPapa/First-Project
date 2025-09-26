def stampa_ordine(cognome_cliente : str, asporto : bool = False, *pizze, **note) -> None:
    print("ORDINE", cognome_cliente.capitalize())
    if asporto:
        print("Il cliente porta via le seguenti pizze:")
    else:
        print("Le seguenti pizze vanno servite al tavolo:")
    for pizza in pizze:
        print("-"+pizza.lower())
    if note:
        print("NOTE:")
        for k,v in note.items():
            print(f"{k}: {v}")

if __name__ == '__main__':
    print("1")
    stampa_ordine("Montano", True, "Margherita", "Diavola", allergie = "Il cliente è allergico alla frutta secca.", aggiunzioni = "diavola con cipolla rossa")

    print("\n2")
    stampa_ordine("Chiofalo", False, "Margherita", "Diavola", allergie = "Il cliente è allergico alla frutta secca.", aggiunzioni = "diavola con cipolla rossa")

