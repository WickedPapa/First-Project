def stampa_nome_cognome(nome : str, cognome : str) -> None:
    print("sono nella funzione")
    def stampa(valore : str) -> None:
        print(valore)
    stampa(nome)
    stampa(cognome)

stampa_nome_cognome("Mario", "Rossi")
#stampa("Mario") errore, la funzione è incapsulata e annidata in un'altra funzione