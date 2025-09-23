from typing import TypedDict, List

class Indirizzo(TypedDict):
    tipo: str
    via: str
    città: str

class Preferenze(TypedDict):
    notifiche: bool
    tema: str

class Profilo(TypedDict):
    email: str
    indirizzi: List[Indirizzo]
    #preferenze: dict[str, bool | str]  # notifiche: bool, tema: str
    preferenze: Preferenze

class Utente(TypedDict):
    id: int
    nome: str
    ruoli: List[str]
    profilo: Profilo

utente = Utente(
    id=123,
    nome="Mario Rossi",
    ruoli=["admin", "editor"],
    profilo=Profilo(
        email="mario.rossi@example.com",
        indirizzi=[
            Indirizzo(tipo="casa", via="Via Roma 10", città="Palermo"),
            Indirizzo(tipo="lavoro", via="Corso Italia 25", città="Milano")
        ],
        preferenze=Preferenze(
            notifiche=True,
            tema="scuro"
        )
    )
)

print(utente)
print(type(utente))