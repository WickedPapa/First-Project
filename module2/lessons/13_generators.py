# I GENERATORI SONO UN TIPO SPECIALE DI ITERATORI
# UN GENERATORE PRODUCE DEI VALORI ATTRAVERSO LA PAROLA CHIAVE yield

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

generatore_numeri_pari = (num for num in numeri if num % 2 == 0)
for i in generatore_numeri_pari:
    print(i)

print("////////////////////////////////////////////////////////////////////////////")
def genera_numeri_pari(numeri):
    for num in numeri:
        if num % 2 == 0:
            yield num #ogni volta che si arriva qui l'esecuzione si ferma finchè il valore non viene consumato.

generatore_numeri_pari_definito_tramite_funzione = genera_numeri_pari(numeri)

print(next(generatore_numeri_pari_definito_tramite_funzione))

for i in generatore_numeri_pari_definito_tramite_funzione:
    print(i)