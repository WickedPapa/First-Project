#esistono di 4 tipi: list, dict, set, generator
#servono per creare una nuova struttura dati da qualsiasi oggetto iterabile.

#List Comprehension
print("LIST COMPREHENSION")
lista = ["ciao", 3, 4, True, [], None]
lista_solo_int = []
for el in lista:
    if type(el) is int:
        lista_solo_int.append(el)

lista_solo_int_comprehension = [el for el in lista if type(el) is int]
print(lista_solo_int)
print(lista_solo_int_comprehension)

#esempio list comprehension complessa
lista = ["ciao", "casa", "ciaone", 3, 4, True, [], None]
lista_vocali_nelle_parole_di_quattro_lettere = [elem.replace(letter, letter.upper()) #l'output aggiunto alla lista
                                                    for elem in lista if type(elem) is str and len(elem) == 4
                                                        for letter in elem if letter in ["a", "e", "i", "o", "u"]]

print(lista_vocali_nelle_parole_di_quattro_lettere)

#Dict Comprehension
print("DICT COMPREHENSION")
lista_chiavi = [1, 2, 3, 4, 5]
lista_valori = ["valore1", "valore2", "valore3", "valore4", "valore5"]
lista_valori_2 = ["valore1_2", "valore2_2", "valore3_2", "valore4_2", "valore5_2"]
dict_generato = {(k if k%2 == 0 else 10+k):v+"#"+v2 for k, v, v2 in zip(lista_chiavi, lista_valori, lista_valori_2)} #zip funziona solo con liste della stessa lunghezza
#print(dict_generato)
for k, v in dict_generato.items():
    print(k, v)
#Set Comprehension
print("SET COMPREHENSION")
lista_2 = ["ciao", "casa", "ciaone", 3, 4, True, [], None, "ciao"]
set_parole_di_4_lettere = {elem.upper() for elem in lista_2 if type(elem) is str and len(elem) == 4}
print(set_parole_di_4_lettere)

#Generator Comprehension
print("GENERATOR COMPREHENSION")