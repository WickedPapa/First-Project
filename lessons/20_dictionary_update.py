#stessa chiave sovrascrive, chiavi diverse aggiunge

d1 = {
    "id": 123,
    "nome": "Paolo",
}

d2 = {
    "id": 124,
    "nome": "Marco",
}

d1.update(d2)
print(d1)
print(d2)

d3 = {
    "id": 123,
    "nome": "Paolo",
}

d4 = {
    "id2": 123,
    "nome2": "Marco",
}

d3.update(d4)
print(d3)
print(d4)

#pop
d5 = {
    "id": 123,
    "nome": "Paolo"
}
print(d5)
nome = d5.pop("nome")
print(nome)
print(d5)