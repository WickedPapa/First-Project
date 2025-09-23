variabile_globale : int = 10
variabile_globale_2 : int = 10

def printa_variabili():
    variabile_locale = 20
    print(variabile_locale)
    print(variabile_globale)
    variabile_globale_2 = 30
    print(variabile_globale_2)

if __name__ == '__main__':
    printa_variabili()
    print(variabile_globale_2)