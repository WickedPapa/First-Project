from __future__ import annotations

from collections.abc import Callable, Sequence

products : dict = {
    "apple" : 1.0,
    "banana" : 0.8,
    "orange" : 1.2,
    "pear" : 1.5,
    "grapes" : 2.0,
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
            print("\nInserisci un numero valido")
            continue
        if choice < 0 or choice > len(products.items()):
            print("\nScelta non valida, riprova.")
            continue
        shopping_cart.append(products_list[choice])
        print(f"{products_list[choice][0]} aggiunto al carrello.")


def open_cart_menu() -> bool:
    exec_menu(CART_MENU)
    return True


def quit_program() -> bool:
    print("\nArrivederci!")
    return False


def show_cart() -> bool:
    if not shopping_cart:
        print("\nIl carrello è vuoto.")
    else:
        tot : float = 0
        print("\nProdotti nel carrello:")
        for index, (item, price) in enumerate(shopping_cart, start=1):
            print(f"{index}. {item}: {price}")
            tot += price
        print("Total:", tot, end="\n\n")
    return True

def remove_product() -> bool:
    show_cart()
    while True:
        try:
            str_choice = input("\nInserisci il numero corrispondente del menu (ENTER per tornare al menu principale): ").strip()
            if not str_choice:
                return True
            choice = int(str_choice)
        except ValueError:
            print("\nInserisci un numero valido")
            continue
        if choice < 0 or choice > len(products.items()):
            print("\nScelta non valida, riprova.")
            continue
        product_removed = shopping_cart.pop(choice)
        print(f"{product_removed[0]} correttamente rimosso.")

def complete_order() -> bool:
    if not shopping_cart:
        print("\nNon ci sono prodotti da acquistare.")
    else:
        print("\nOrdine completato! Grazie per l'acquisto.")
        shopping_cart.clear()
    return True


def clear_cart() -> bool:
    shopping_cart.clear()
    print("\nCarrello svuotato.")
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
            print("\nInserisci un numero valido")
            continue
        if choice < 0 or choice >= len(items):
            print("\nScelta non valida, riprova.")
            continue
        _, action = items[choice]
        if not action():
            break

if __name__ == "__main__":
    exec_menu(MAIN_MENU)
