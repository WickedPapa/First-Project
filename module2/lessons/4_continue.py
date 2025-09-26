lista_numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for num in lista_numeri:
    if num == 10:
        continue #mi permette di saltare un giro, si usa solo in particolari casi
    if num % 2 == 0:
        print(num)