try:
    numero = int(input("Inserisci un numero: "))
    print(10/numero)
except ValueError:
    print("Devi inserire un numero intero")
#except ZeroDivisionError:
#    print("Errore non puoi dividere per zero")
except Exception as ex:
    print("ERRORE: ", ex)
    raise ex
else:
    print("Divisione effettuata con successo!")
finally:
    print("Esecuzione terminata")