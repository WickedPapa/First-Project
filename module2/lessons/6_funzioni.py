def greetings():
    print("ciao")

def repeat(word):
    print(word)

def is_int(num):
    try:
        int(num)
        return True
    except Exception:
        return False

#tipizzazione
def say_hi() -> None:
    print("hi")

def is_short_word(word : str) -> bool:
    return len(word) <= 4

#parametri obbligatori e opzionali
#obbligatori sono sempre indicati prima
#opzionali si mettono dopo e va indicato un default

def print_inf(full_name: str, age: int, is_admin : bool = False) -> None:
    print(full_name + ",", age, "anni.", "Utente", "amministratore." if is_admin else "standard.")

if __name__ == '__main__':
    print_inf("Paolo Montano", 32, True)
    print_inf("Marta Chiofalo", 33, False)
    print_inf("Simona Montano", 9)
    print_inf(age=9, full_name="Ellen Montano") #in python posso passare i parametri in qualunque ordine se specifico il nome