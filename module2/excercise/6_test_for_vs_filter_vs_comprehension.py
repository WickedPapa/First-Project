import time
import datetime
from collections import Counter

lista_numeri = [1, 2, 3, 4, 5]
nuova_lista = []
sum_lambda = lambda x, y : x + y
numbers_in_list = 10_000_000

start = time.time()
print("Inizio generazione lista =", datetime.datetime.fromtimestamp(start).time())

for index in range(numbers_in_list):
    if index % 100_000 == 0:
        print("Ciclo numero", index)
    nuova_lista.extend(lista_numeri)
end = time.time()

print("Fine generazione lista =", datetime.datetime.fromtimestamp(end).time())
duration = end - start

print("\nTEST VELOCITA' FOR VS FILTER VS COMPREHENSION")
print("Dalla lista generata estrarremo solo i numeri pari maggiori di 500")

podio = []

print("\nFOR")
start = time.time()
lista_for = []
for element in nuova_lista:
    if element > 500 and element % 2 == 0:
        lista_for.append(element)
end = time.time()
duration = end - start
print(f"Calcolo tramite FOR effettuato in {duration:.8f} seconds")
podio.append(("FOR", duration))
print("FINE FOR")

print("\nFILTER")
start = time.time()
lista_filter = list(filter(lambda x : x > 500 and x % 2 == 0, nuova_lista))
end = time.time()
duration = end - start
print(f"Calcolo tramite FILTER effettuato in {duration:.8f} seconds")
podio.append(("FILTER", duration))
print("FINE FILTER")

print("\nCOMPREHENSION")
start = time.time()
lista_comprehension = [x for x in nuova_lista if x > 500 and x % 2 == 0]
end = time.time()
duration = end - start
print(f"Calcolo tramite COMPREHENSION effettuato in {duration:.8f} seconds")
podio.append(("COMPREHENSION", duration))
print("FINE COMPREHENSION")

if Counter(lista_for) == Counter(lista_filter) == Counter(lista_comprehension):
    print("\nLe 3 liste generate sono uguali")
else:
    print("\nERRORE: Le 3 liste generate NON sono uguali")

podio.sort(key=lambda x : x[1])
print("\nPODIO RISULTATI")
for position,element in enumerate(podio):
    print(f"{position + 1} posto: {element[0]} con {element[1]:.3f} secondi")
