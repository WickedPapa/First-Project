from functools import reduce

print("MAP")
lista_nomi = ["Paolo", "marta", "simona", "Ellen"]
print(lista_nomi)
lista_nomi = list(map(lambda x : x.upper(), lista_nomi))
print(lista_nomi)

print("")
print("FILTER")
lista_nomi = ["Paolo", "marta", "simona", "Ellen"]
print(lista_nomi)
lista_nomi = list(filter(lambda x : len(x) == 5, lista_nomi))
print(lista_nomi)

print("")
print("MAP + FILTER")
lista_nomi = ["1", "marta", "5", "Ellen"]
print(lista_nomi)
lista_int_in_lista_nomi = list(map(lambda x : int(x), filter(lambda x : x.isdigit(), lista_nomi)))
print(lista_int_in_lista_nomi)

print("")
print("ZIP")
lista_nomi = ["Paolo", "Marta", "Simona", "Ellen"]
lista_eta = [32, 33, 9, 5]
print(lista_nomi)
print(lista_eta)
tuple_generate_tramite_zip = list(zip(lista_nomi, lista_eta))
print("tuple_generate_tramite_zip:\n")
print(tuple_generate_tramite_zip)
print(tuple_generate_tramite_zip[0][1])

print("")
print("RANGE")
#range(start, stop, step)
print(list(range(0, 10 , 2))) #range ritorna un operatore. start e step sono opzionali

print("")
print("ENUMERATE")
#enumerate(iterabile, start)
for index, nome in enumerate(["Paolo", "Marta"], 10): #range ritorna un operatore. start è opzionale
    print(index, nome)

print("")
print("ALL")
#verifica che tutti gli elementi rispettino la condizione
numeri = [1, 2, 3]
print(numeri)
print(all([True, False, True]))
print(all(n % 2 == 0 for n in numeri)) #generatori, li vedremo dopo

print("")
print("ANY")
#verifica che almeno un elemento rispetti la condizione
numeri = [1, 2, 3]
print(numeri)
print(any([True, False, True]))
print(any(n % 2 == 0 for n in numeri)) #generatori, li vedremo dopo

print("")
print("SUM")
numeri = [1, 2, 3]
print(sum(numeri))

print("")
print("MAX")
numeri = [1, 2, 3]
print(max(numeri))

print("")
print("MIN")
numeri = [1, 2, 3]
print(min(numeri))