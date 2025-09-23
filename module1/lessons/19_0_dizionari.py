#formato come json
#non ordinati (ma ordinabili)?
#chiavi uniche e immutabili

#2 modi per dichiarare un dizionario
studente : dict = {
    "nome" : "Paolo",
    "cognome" : "Montano",
    "eta" : 33
}

studente_2 : dict = dict(
    nome = "Paolo",
    cognome = "Montano",
    eta = 33)

print(studente)
print(studente_2)

#2 modi per accedere un dizionario
print(studente_2["nome"])
print(studente_2.get("nome"))
#print(studente_2["colore_occhi"]) produce errore KeyError
print(studente_2.get("colore_occhi")) #None
print(studente_2.get("occhiali", False)) #se la chiave non è presente posso dare un default

#modificare valori
studente["eta"] = studente["eta"]+1

print(studente)
print(studente_2)

#default per un campo
studente_3 : dict = dict(
    nome = "Paolo",
    cognome = "Montano",
    eta = 33)

print(studente_3)
studente_3.setdefault("segni_particolari", "Nessuno")
print(studente_3)
print(studente_3.get("segni_particolari"))

#nested dict
utente : dict = {
    "id": 123,
    "nome": "Mario Rossi",
    "ruoli": ["admin", "editor"],
    "profilo": {
        "email": "mario.rossi@example.com",
        "indirizzi": [
            {"tipo": "casa", "via": "Via Roma 10", "città": "Palermo"},
            {"tipo": "lavoro", "via": "Corso Italia 25", "città": "Milano"}
        ],
        "preferenze": {
            "notifiche": True,
            "tema": "scuro"
        }
    }
}

print(utente)
print(utente.get("id"))
print(utente.get("profilo").get("indirizzi")[0]["via"])
print(utente.get("profilo").get("preferenze").get("notifiche"))

