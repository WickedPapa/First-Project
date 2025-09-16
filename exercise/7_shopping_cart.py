from __future__ import annotations

from collections.abc import Callable, Sequence

products : dict = {
    "Mela" : 1.0,
    "Banana" : 0.8,
    "Arancia" : 1.2,
    "Pera" : 1.5,
    "Uva" : 2.0,
}

MenuAction = Callable[[], bool]
MenuItem = tuple[str, MenuAction]

shopping_cart: list[tuple[str, float]] = []


def go_to_shopping() -> bool:
    print("\nScegli il prodotto da acquistare")
    products_list = list(products.items())
    while True:
        for i, (k, v) in enumerate(products_list):
            print(i, "-", k + ":", v, "euro")
        try:
            str_choice = input("\nInserisci il numero corrispondente del menu (ENTER per tornare al menu principale): ").strip()
            if not str_choice:
                return True
            choice = int(str_choice)
        except ValueError:
            print("Inserisci un numero valido\n")
            continue
        if choice < 0 or choice >= len(products.items()):
            print("Scelta non valida, riprova.\n")
            continue
        shopping_cart.append(products_list[choice])
        print(f"\n{products_list[choice][0]} aggiunto al carrello.\n")


def open_cart_menu() -> bool:
    exec_menu(CART_MENU)
    return True


def quit_program() -> bool:
    print("\nArrivederci!")
    return False


def show_cart() -> bool:
    if not shopping_cart:
        print("Il carrello è vuoto.\n")
    else:
        tot : float = 0
        print("\nProdotti nel carrello:")
        for index, (item, price) in enumerate(shopping_cart):
            print(f"{index}. {item}: {price}")
            tot += price
        print("Total:", tot, end="\n\n")
    return True

def remove_product() -> bool:
    show_cart()
    if not shopping_cart:
        return True
    while True:
        try:
            str_choice = input("Inserisci il numero corrispondente del prodotto da rimuovere (ENTER per tornare al menu principale): ").strip()
            if not str_choice:
                return True
            choice = int(str_choice)
        except ValueError:
            print("Inserisci un numero valido\n")
            continue
        if choice < 0 or choice >= len(shopping_cart):
            print("Scelta non valida, riprova.\n")
            continue
        product_removed = shopping_cart.pop(choice)
        print(f"\n{product_removed[0]} correttamente rimosso.\n")

def complete_order() -> bool:
    if not shopping_cart:
        print("\nNon ci sono prodotti da acquistare.")
    else:
        show_cart()
        if not shopping_cart:
            return True
        tot : float = 0
        for item in shopping_cart:
            tot += item[1]
        while True:
            try:
                cash = float(input("Inserisci importo per pagare: "))
            except ValueError:
                print("Inserisci un importo valido (e.g. 23.30, 10, 0.50, ecc...)\n")
                continue
            if cash < tot:
                print("Purtroppo non hai abbastanza soldi per pagare. Prova a rimuovere qualcosa dal carello.\n")
                return True
            print("\nOrdine completato! Grazie per l'acquisto.")
            print(f"Resto: {cash - tot}")
            print("Hai acquistato:")
            for item in shopping_cart:
                print(item[0])
            shopping_cart.clear()
            print("")
            break
    return True


def clear_cart() -> bool:
    shopping_cart.clear()
    print("\nCarrello svuotato.\n")
    return True


def go_back() -> bool:
    return False


MAIN_MENU: list[MenuItem] = [
    ("Go to shopping", go_to_shopping),
    ("Go to cart", open_cart_menu),
    ("Quit", quit_program),
]

CART_MENU: list[MenuItem] = [
    ("Show cart", show_cart),
    ("Complete order", complete_order),
    ("Clear cart", clear_cart),
    ("Remove product", remove_product),
    ("Go back", go_back),
]


def print_menu(items: Sequence[MenuItem]) -> None:
    for index, (label, _) in enumerate(items):
        print(index, " - ", label)

def exec_menu(items: Sequence[MenuItem]) -> None:
    while True:
        print_menu(items)
        try:
            choice = int(input("\nInserisci il numero corrispondente del menu: "))
        except ValueError:
            print("Inserisci un numero valido\n")
            continue
        if choice < 0 or choice >= len(items):
            print("Scelta non valida, riprova.\n")
            continue
        _, action = items[choice]
        if not action():
            break

if __name__ == "__main__":
    exec_menu(MAIN_MENU)
