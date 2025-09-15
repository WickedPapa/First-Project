def ask_the_word():
    word : str = input("Inserisci una parola e ti dirò se è palindroma: ")
    while not word.isalpha():
        word = input("Per favore inserisci una parola che contenga solo lettere: ")
    return word.lower()

def palindrome_checker(word):
    size : int = len(word)
    for i in range(size//2):
        if word[i] != word[size-i-1]:
            return False
    return True


def is_palindrome():
    inserted_word : str = ask_the_word()
    variable_string_part : str = ""
    if palindrome_checker(inserted_word):
        variable_string_part = "è"
    else:
        variable_string_part = "non è"
    print(f"La parola {inserted_word} {variable_string_part} palindroma")

if __name__ == '__main__':
    is_palindrome()