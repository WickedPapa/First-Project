def quadrato(x):
    return x ** 2

quadrato_lambda = lambda x : x ** 2

print("quadrato da funzione", quadrato(5))
print("quadrato da lambda", quadrato_lambda(5))

def multiply(x, y):
    return x * y

multiply_lambda = lambda x, y: x * y

print("multiply da funzione", multiply(4, 5))
print("multiply da lambda", multiply_lambda(4, 5))

##############################################
persone = [("Paolo", 32), ("marta", 33), ("Gianni", 50)]
persone.sort(key=lambda x: x[0].upper())
print("persone orinate per nome upper: ", persone)
print("persone orinate per eta: ", sorted(persone, key=lambda x: x[1]))
print("persone orinate per per la terza lettera: ", sorted(persone, key=lambda x: x[0][2].upper()))

numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeri_len = len(numeri)
numeri.sort(key=lambda x: x if x%2!=0 else x+len(numeri))
print("numeri ordinati, prima i dispari e poi i pari: ", numeri)