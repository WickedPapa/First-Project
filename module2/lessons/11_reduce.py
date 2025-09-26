from functools import reduce

lista_numeri = [1, 2, 3, 4, 5]
somma = reduce(lambda x, y : x + y, lista_numeri)
print(somma)