import statistics

lista_valori = [1,1,1,3,4,5,5,5,5,5,5,5,6,9]

# MEDIA: somma valori divisi per numero totale
media = statistics.mean(lista_valori)
print("media", media)

# MEDIANA: valore centrale di un insieme di dati ordinati. Se i dati sono in numero pari,
# la mediana e la media dei 2 valori centrali.
mediana = statistics.median(lista_valori)
print("mediana", mediana)

# MODA: il valore che appare più frequentemente in un insieme di dati
moda = statistics.mode(lista_valori)
print("moda", moda)
