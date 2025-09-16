print("ESERCIZIO 1")
dizionario = {
    'a': 10,
    'b': "casa",
    'c': True,
    'd': None
}

for k, v in dizionario.items():
    print(k, v)
############################################
print("\nESERCIZIO 2")
dizionario = {
    'a': 10,
    'a': "casa"
}

print(dizionario.get('a'))
############################################
print("\nESERCIZIO 3")

nested_dict = {
    "a": {
        "b": "casa",
        "c": {
            "d": True
        }
    }
}
print(nested_dict["a"]["b"])
print(nested_dict["a"].get("c")["d"])
############################################
print("\nESERCIZIO 4")
dizionario_2 = {
    'a': 10,
    'b': "casa",
    'c': 12,
    'd': None,
    'e': True
}
print("dizionario: ", dizionario_2)
lista_keys = list(dizionario_2.keys())
print("lista chiavi: ", lista_keys)
for k in lista_keys:
    a = dizionario_2.pop(k)
    print(a)
    print(dizionario_2)
############################################
print("\nESERCIZIO 5")


def _parse_numeric_input(prompt: str) -> list[int]:
    """Return a list of integers parsed from a comma separated input string."""

    raw_values = input(prompt)
    cleaned_values: list[int] = []
    for raw_value in raw_values.replace(" ", "").split(","):
        if not raw_value:
            continue
        try:
            cleaned_values.append(int(raw_value))
        except ValueError as exc:
            raise ValueError(
                f"Il valore '{raw_value}' non è un numero intero valido."
            ) from exc
    return cleaned_values


original_list = _parse_numeric_input(
    "inserisci una lista di num separati da virgole: "
)
cleaned_set = set(original_list)
print("original list: ", sorted(original_list))
print("cleaned set: ", sorted(cleaned_set))
############################################
print("\nESERCIZIO 6")
list_1 = _parse_numeric_input(
    "inserisci una lista di num separati da virgole: "
)
list_2 = _parse_numeric_input(
    "inseriscine un'altra e ti dirò intersezione, unione e differenze tra le 2: "
)
cleaned_set_1 = set(list_1)
cleaned_set_2 = set(list_2)
print("union: ", cleaned_set_1 | cleaned_set_2)
print("intersection: ", cleaned_set_1 & cleaned_set_2)
print("difference lista 1 - lista 2: ", cleaned_set_1 - cleaned_set_2)
print("difference lista 2 - lista 1: ", cleaned_set_2 - cleaned_set_1)
print("symmetric difference: ", cleaned_set_1 ^ cleaned_set_2)
############################################
print("\nESERCIZIO 7")
frase_1 = set(input("inserisci una frase: ").lower()
              .replace(",","")
              .replace(".","")
              .split(" "))
frase_2 = set(input("inserisci un'altra frase e troverò le parole in comune: ").lower()
              .replace(",","")
              .replace(".","")
              .split(" "))
print("Parole in comune: ", frase_1 & frase_2)
############################################
print("\nESERCIZIO 8")
frase = set((input("Inserisci una frase e ordinerò le parole in ordine alfabetico: ")
         .replace(",", "")
         .replace(".", "")
         .replace("!", "")
         .replace("?", "")
         .lower()
         .split(" ")))
print("Parole in ordine: ", sorted(frase, reverse=True))