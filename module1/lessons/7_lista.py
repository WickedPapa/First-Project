from os import remove

lista : list = [1, 2, 3]
lista_2 : list = [1, "ciao", True]

print(lista)
print(lista_2)

print(lista[1])

#lunghezza lista
print(len(lista))

#posso riassegnarla
lista = [4, 5]
print(lista)

#o modificarne il contenuto
lista[1] = 12
print(lista)

#aggiungere
lista.append(4)

#aggiugere in un determinato posto
lista.insert(2, 7)
print(lista)

lista.remove(7)
print(lista)

#lista.remove(40) errore 40 not in list quindi potrei fare:
if 40 in lista:
    lista.remove(40)

#rimuove ultimo elemento
lista.pop()
print(lista)

#rimuove elemento all'indice dato
lista.pop(1)
print(lista)

#ordinamento
lista_da_ordinare = [2, 4, 3, 2, 5]
lista_da_ordinare_2 = [2, 4, 3, 2, 5]
lista_da_ordinare.sort() #ritorna None
lista_da_ordinare_2.sort(reverse=True)
print("lista ordinata: ", lista_da_ordinare)
print("lista ordinata reverse: ", lista_da_ordinare_2)

lista_da_ordinare_3 = [2, 4, 3, 2, 5]
#sorted invece restituisce la lista
lista_ordinata_3 = sorted(lista_da_ordinare_3)
lista_ordinata_4_reversed = sorted(lista_ordinata_3, reverse=True)
print("lista ordinata con sorted: ", lista_ordinata_3)
print("lista ordinata con sorted reversed: ", lista_ordinata_4_reversed)