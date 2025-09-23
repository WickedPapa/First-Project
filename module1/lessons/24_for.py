#FOR
print("FOR SEMPLICE")
for letter in "programming":
    print(letter)

#CONTINUE skippa il ciclo
print("\nCONTINUE")
number2 = 0
for letter in "programming":
    if letter == "p":
        continue #skippo il giro
    print(letter)

#BREAK termina il ciclo
print("\nBREAK")
for letter in "programming":
    if letter == "m":
        break
    print(letter)

#FOR CON RANGE
print("\nFOR CON RANGE")
for number in range (10):
    print(number, end=" ") #print stampa con , invece di andare a capo

print("\nFOR CON IN")
lista_esempio = ["a", "b", "c", "d", "e", "f"]
for item in lista_esempio:
    print(item, end=" ")

print("\nFOR CON ENUMERATE")
for index, item in enumerate(lista_esempio):
    print(index, item)

print("\nFOR CON RANGE LEN")
for index in range(len(lista_esempio)):
    print(index, lista_esempio[index])