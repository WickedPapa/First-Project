dict_translations = {
    "ciao" : "hello",
    "case" : "home"
}

while True:
    word = input("Inserisci la parola e la tradurrò in inglese (Enter per uscire): ").strip().lower()
    # controlli vari tipo spazi, caratteri speciali, numeri ecc...
    if not word:
        print("Arrivederci!")
        break
    if word in dict_translations:
        print(word, "in inglese si dice", dict_translations[word])
    else:
        new_word_translation = input("Mi dispiace, la traduzione non è presente nel dizionario, inseriscila tu: ").strip()
        # controlli vari tipo spazi, caratteri speciali, numeri ecc...
        dict_translations.update({word: new_word_translation.lower()})
        print("Traduzione aggiunta!", word, "in inglese si dice", dict_translations[word])