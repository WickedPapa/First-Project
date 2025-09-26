lista_numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def numero_pari(numero):
    return numero % 2 == 0

lambda_numero_pari = lambda numero: numero % 2 == 0

lambda_numero_pari_chiamando_function = lambda numero: numero_pari(numero)

lambda_numero_pari_chiamando_lambda = lambda numero: lambda_numero_pari(numero)

numeri_estratti = list(filter(lambda x: x % 2 == 0, lista_numeri))
print(numeri_estratti)

numeri_estratti = list(filter(numero_pari, lista_numeri))
print(numeri_estratti)

numeri_estratti = list(filter(lambda_numero_pari, lista_numeri))
print(numeri_estratti)

numeri_estratti = list(filter(lambda_numero_pari_chiamando_function, lista_numeri))
print(numeri_estratti)

numeri_estratti = list(filter(lambda_numero_pari_chiamando_lambda, lista_numeri))
print(numeri_estratti)