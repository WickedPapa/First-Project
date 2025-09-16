MAIN_MENU_VOICES : list[str] = [
    "Go to shopping",
    "Go to cart",
    "Quit"
]

CART_MENU_VOICES : list[str] = [
    "Show cart",
    "Complete order",
    "Clear cart",
    "Go back"
]

def print_menu(voices : list[str]):
    for index, voice in enumerate(voices):
        print(index, " - ", voice)

def exec_menu(voices : list[str]):
    choice: int = -1
    while choice != len(voices) - 1:
        print_menu(voices)
        try:
            choice = int(input("\nInserisci il numero corrispondente del menu: "))
        except ValueError:
            print("\nInserisci un numero valido")
            continue
        # rendere la lista di voci una mappa di voci -> funzioni così da poter eseguire la funzione corretta

if __name__ == '__main__':
    exec_menu(MAIN_MENU_VOICES)
