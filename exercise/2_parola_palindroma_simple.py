while True:
    parola : str = input("Parola palindroma: ").lower().strip()
    inverted_parola = parola[::-1]
    print(parola == inverted_parola)