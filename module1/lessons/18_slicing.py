#sintassi lista[start:stop:step]
numeri = [1, 2, 3, 4, 5]
print(numeri)
print(numeri[0:5]) #ometto step
print(numeri[2:]) #ometto stop e step
print(numeri[:2]) #ometto start e step
print(numeri[2:5])
print(numeri[0::2])
print(numeri[0::3])
print(numeri[::-1]) #lista reverse
print(numeri[::-2]) #lista reverse a step di 2
print(numeri[::-8]) #lista reverse a ste di 8 (non va in out of bound/range)
print(numeri[:]) #copia lista
print(numeri[:8]) #stop maggiore della lista non va in out of range ma restituisce fino all'ultimo elemento
print(numeri[8:]) #start maggiore della lista non va in out of range ma restituisce lista vuota
#print(numeri[8]) questo va in out of range

numeri2 = numeri[:]
numeri2.reverse()
print(numeri2) #non posso fare print(numeri2.reverse()) perchè reverse ritorna None (tipo void....)