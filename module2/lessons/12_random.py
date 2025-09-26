import random

lista_estratti = random.sample(range(1,100_000), 100) #prendi 100 num casuali da 1 a 100k
print(lista_estratti)

print("IL VINCITORE E' :", random.choice(lista_estratti))