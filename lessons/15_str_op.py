testo : str = "Buongiorno e benvenuti al corso"

print(testo)
print(testo.upper())
print(testo.lower())
print(testo.count("o")) #conta occorrenze
print(testo.find("o")) #prima occorrenza
print(testo.rfind("o")) #ultima occorrenza
print(testo.capitalize()) #maiusc solo prima lettera
print(testo.title()) #maiusc la prima lettera di ogni parola
print(testo.startswith("corso"))
print(testo.endswith("corso"))
# print(testo.strip()) #tipo trim
print(testo.removesuffix("rso"))
print(testo.strip("rso")) #come trim ma con caratteri specifici a inizio o fine stringa ATTENZIONE "rso" è l'insieme di
# caratteri, quindi continuerà a rimuovere l'ultimo carattere finchè sarà una r, una s o una o
print(testo.split(" "))
print(testo.split(" ", 2)) #splitta solo per le prime 2 occorrenze al massimo
print(testo.replace(" ", "-"))
print(", ".join(["ciao", "mondo", "cosa"]))
print(", ".join("prova"))

alpha = "Ciao"
digit = "1241"
float = "21412.214"
alphanumeric : str = "Ciao1234"
alphanumericWithSymbol : str = "Ciao1234"

print(alphanumeric.isalpha())
print(alphanumeric.isdigit())
print(alphanumeric.isalnum())
print(alphanumericWithSymbol.isalnum())
print(digit.isdigit())
print(digit.isnumeric())
print(float.isdigit())
print(float.isnumeric())

stringa_da_formattare = "Ciao sono {nome} {cognome} e ho {anni} anni"
print(stringa_da_formattare.format(nome = "Paolo", cognome = "Montano", anni = 32))

#Opppure
nome = "Paolo"
cognome = "Montano"
anni = 32
print(f"Ciao sono {nome} {cognome} e ho {anni} anni")