caratteri_speciali: str = "!£$%&/()=?^><,.-_:;"
parola : str = "<,.<aiuhf.<n.kahgòo8<g37<9&(/&(/%)(3"
parola_pulita = ""
for lettera in parola:
    if lettera not in caratteri_speciali:
        parola_pulita += lettera
print(parola_pulita)
