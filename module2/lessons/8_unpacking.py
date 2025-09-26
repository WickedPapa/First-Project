print("lista", [1, 2, 3])
print("lista spacchettata",*[1, 2, 3])

print("tupla",(1, 2, 3))
print("tupla spacchettata",*(1, 2, 3))


lista = [1, 2, 3]
tupla = (1, 2, 3)
dizionario = {"x": 1, "y": 2, "z": 3}

print(*lista)
print(*tupla)
print(*dizionario)

#definisco un metodo
def f(x, y, z=0, k=0):
    print(x, y, z, k)

#il dizionario deve avere i nomi delle chiavi uguali a quelli del metodo
d = {"x": 1, "y": 2, "z": 3}
f(**dizionario)
#oppure
f(**{"x": 1, "y": 2})  # f(x=1, y=2)
f(*[9, 9, 9])

#usando kwargs posso usare anche nomi delle chiavi a piacere
dizionario_2 = {"Paolo": 1, "Marta": 2, "Ellen": 3, "Simona": 4}

def f_2(**dizionario):
    for k, v in dizionario.items():
        print(k, v)

f_2(**dizionario_2)


#IMPORTANTE
# *seq → spacchetta in posizionali.
f(*[8, 9, 10])
# **dict → spacchetta in keyword args.
f(**{"z":5, "y": 1, "x": 2})  # f(x=1, y=2)


#POSSO COMBINARLI!

print("COMBINAZIONE UNPACKING ARGS E KWARGS")
def funzione(a, b, c, d, e):
    print(a, b, c, d, e)

arguments = [1, 2, 3]
keyword_arguments = {"d": 4, "e": 5}
funzione(*arguments, **keyword_arguments)