def genera_numeri_e_lettere():
    lista_numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista_lettere = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    for numero, lettera in zip(lista_numeri, lista_lettere):
        yield str(numero) + str(lettera)

for el in genera_numeri_e_lettere():
    print(el)