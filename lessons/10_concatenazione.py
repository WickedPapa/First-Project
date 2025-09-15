a = 5
b = 7

print("benvenuti nella classe " + str(a if a > b else b) + " liceo")

#f string -> codice dentro le stringhe senza concatenazione
print(f"benvenuti nella classe {str(a if a > b else b)} liceo")

#la concatenazione funziona con stringhe, liste e tuple

lista = [1, 2]
lista2 = ["ciao", True]
lista3 = lista + lista2
print(lista3)

tupla = (1, 2)
tupla2 = ("ciao", True)
tupla3 = tupla + tupla2
print(tupla3)