#WHILE
number = 0
while number < 10:
    number = number + 1
    print(number)
print("FINE")

#CONTINUE skippa il ciclo
print("\nCONTINUE")
number2 = 0
while number2 < 10:
    number2 = number2 + 1
    if number2 == 2:
        continue #non stamperà il 2 ma andrà al 3
    print(number2)
print("FINE")

#BREAK termina il ciclo
print("\nBREAK")
number3 = 0
while number3 < 10:
    number3 = number3 + 1
    if number3 == 5:
        break #esco dal while
    print(number3)
print("FINE")