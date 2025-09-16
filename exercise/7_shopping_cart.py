from __future__ import annotations

from collections.abc import Callable, Sequence

MenuAction = Callable[[], bool]
MenuItem = tuple[str, MenuAction]

shopping_cart: list[str] = []


def go_to_shopping() -> bool:
    while True:
        item = input("\nInserisci il prodotto da aggiungere (ENTER per tornare al menu principale): ").strip()
        if not item:
            return True
        shopping_cart.append(item)
        print(f"{item} aggiunto al carrello.")


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
        print("\nProdotti nel carrello:")
        for index, item in enumerate(shopping_cart, start=1):
            print(f"{index}. {item}")
    return True


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
