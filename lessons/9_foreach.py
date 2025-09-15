#foreach
parola = "ciao"

#posso iterare una stringa (ovviamente anche liste e tuple)
for lettera in parola:
    print(lettera)

print("prova enumerate che crea tuple indice-lettera")
for tupla in enumerate(parola):
    print(tupla)

#se uso enumerate posso indicare 2 varibili perchè la tupla ha indice e lettera
print("prova con 2 variabili")
for  indice, lettera in enumerate(parola):
    print(indice, lettera)

print("prova lista e stringhe")
parola = "ciao"
lista = ["ciao", 1, True]

print("\nSTRINGA:")
for lettera in parola:
    print(lettera)

print("\nLISTA:")
for elemento in lista:
    print(elemento)

print("\nMISTO:")
for elemento in lista:
    if type(elemento) == str: #instanceOf
        for lettera in elemento:
            print(lettera)
    else:
        print(elemento)

print("\nTEST CON TUPLE, LISTE E STRINGHE:")
persone = [("Paolo","Montano", 32), ("Marta", "CHIOFALO", 33), ("Mario", "Rossi", 50)]
print("Tra le seguenti persone:")
perosone_interessate = []
for persona in persone:
    print(persona)
    if type(persona[1]) == str and persona[1][-1].lower() == "o":
        perosone_interessate.append(persona)

print("Solo le seguenti hanno un cognome che finisce per O:")
for persona in perosone_interessate:
    print(persona)