print("OPERATORE IS")
a = [1, 2]
b = [1, 2]
c = a

print(a is c) #vero perchè stesso indirizzo di memoria
print(a is b) #falso perchè valori uguali ma diverso indirizzo di memoria
print(a is not b) #vero perchè negato

print("OPERATORE IN")
stringa = "Ciao Mondo"
lista = ["Ciao", 1]
tupla = (1, True)


print("C" in stringa)
print('C' in stringa)
print(True in tupla)
print(True not in lista)
print(1 not in lista)

#l'in si usa anche per le iterazioni
for lettera in stringa:
    print(lettera)
