from typing import List
from dataclasses import dataclass

@dataclass
class Indirizzo:
    tipo: str
    via: str
    città: str

@dataclass
class Preferenze:
    notifiche: bool
    tema: str

@dataclass
class Profilo:
    email: str
    indirizzi: List[Indirizzo]
    #preferenze: dict[str, bool | str]  # notifiche: bool, tema: str
    preferenze: Preferenze

@dataclass
class Utente:
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