#struttura immutabile
#PIU' VELOCE DELLE LISTE
#SI PUO' USARE COME CHIAVE DEI DIZIONARI

tupla1 : tuple = (1, 2, 3)
tupla2 : tuple = (1, "ciao", True)

print(tupla1)
print(tupla2)

print(tupla1[1])

#posso riassegnarla
tupla1 = (9, 12)
print(tupla1)

#ma non posso modificarne il contenuto
#tupla1[1] = 12 -> errore!!

#posso creare tuple sia con le tonde che senza
tupla_3 = (9, 4, 5)
tupla_4 = 9, 4, 5
print(tupla_3)
print(tupla_4)

#sulle tuple posso fare: slice, concatenazioni, moltiplicazioni, in, len, iterazioni
print(tupla_3*2)

tupla_a = "Paolo", "Montano", 32
tupla_b = "Marta", "Chiofalo", 33

print(tupla_a)
print(tupla_b)

lista_tuple = [tupla_a*5, tupla_b*4]

tuplone = ()

for el in lista_tuple:
    tuplone += el

lisa_cognomi = tuplone[1::3]
print(lisa_cognomi)