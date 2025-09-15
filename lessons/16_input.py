while True:
    try:
        numero : int = int(input("Ciao pirla, inserisci un numero: "))
        print(f"hai inserito il numero: {numero}")
        break
    except:
        print("Ti ho detto un numero (non scritto a lettere)")
        continue
