def conta_parola(testo : str):
    parole = testo.split()
    def conta(parola):
        return parole.count(parola)
    return conta

testo_prova = "Ciao come stai ? Tutto bene ? Io bene ? Ciao"
testo_prova_2 = "Altro testo"
a = conta_parola(testo_prova)
b = conta_parola(testo_prova_2)
print(a("bene")) #2
print(a("Ciao")) #2
print(a("come")) #1
print(a("rosso")) #0

print(b("bene")) #0
print(b("Ciao")) #0
print(b("come")) #0
print(b("rosso")) #0
print(b("Altro")) #1