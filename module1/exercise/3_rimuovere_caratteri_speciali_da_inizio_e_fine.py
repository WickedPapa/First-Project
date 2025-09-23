while True:
    parola: str = input("Parola con caratteri speciali: ").lower().strip()
    print(parola.strip("\"!.-&$%"))