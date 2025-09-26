import time
import datetime
from functools import reduce

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

print(duration)
print(f"\nLa generazione della lista ha impiegato {duration:.8f} secondi")

print("\nREDUCE")
start = time.time()
somma = reduce(sum_lambda, nuova_lista)
end = time.time()
duration = end - start
print(f"La somma dei {numbers_in_list} numeri nella lista fa = {somma}.") #.8f serve per stampare con 8 cifre dopo la virgola
print(f"Calcolo tramite REDUCE effettuato in {duration:.8f} seconds")
print("FINE REDUCE")