# args -> numero variabile di argomenti (lista o tupla)
# kwargs (keyword args) -> numero variabile di argomenti (dict)

def saluta_persone(*argomenti : str):
    for person in argomenti:
        print("Ciao", person)

def saluta_persone_kwargs(**argomenti_dict):
    for k, v in argomenti_dict.items():
        print(f"{k}: {v}")

if __name__ == '__main__':
    saluta_persone("Paolo", "Marta", "Ellen", "Simona")
    saluta_persone_kwargs(nome="Paolo", cognome= "Montano")


#args e kwargs possono essere usati con parametri obbligatori e opzionali.
#la gerarchia è:
#obbligatori, opzionali, args e kwargs
#in realtà esistono anche i parametri obbligatori e opzionali "nominali" cioè che vanno passati per forza per nome.
#la gerarchia completa è
#obbligatori, opzionali, args, obbligatori nominali, obbligatori opzionali e kwargs
