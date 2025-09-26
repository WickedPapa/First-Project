from functools import reduce

print("")
print("MAP + FILTER + REDUCE")
lista_nomi = ["1", "marta", "5", "Ellen"]
print(lista_nomi)
somma = reduce(lambda x, y : x + y, map(lambda x : int(x), filter(lambda x : x.isdigit(), lista_nomi)))
print(somma)