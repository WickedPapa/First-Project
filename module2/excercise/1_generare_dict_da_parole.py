#dato un array di parole generare tramite comprehension un dic avente come chiavi le parole e come valori la lunghezza delle stesse

input_str = ["aasfua", "paolo", "nome", "ciccionello", "brigido"]

dict_gen = { k:len(k) for k in input_str }

print(dict_gen)