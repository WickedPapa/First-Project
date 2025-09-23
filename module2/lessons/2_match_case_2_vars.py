eta, premium = 15, False

match eta, premium:
    case e, True if e >= 18:
        print("Accesso a tutto il catalogo")
    case e, False if e >= 18:
        print("Accesso a tutto il catalogo NON premium")
    case _, True:
        print("Accesso al catalogo minorenni")
    case _:
        print("Accesso al catalogo minorenni  NON premium")

#spesso quando il match case è complesso è meglio usare if-elif-else