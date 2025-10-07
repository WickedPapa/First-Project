#closure ci permette di mantere delle info relative all'esecuzione precedente (vedi secondo esempio)

def moltiplicatore(fattore):
    def moltiplica(numero):
        return numero * fattore
    return moltiplica

doppio = moltiplicatore(2)
triplo = moltiplicatore(3)

print(doppio(5)) #10
print(triplo(5)) #15

#posso anche farlo inline
print(moltiplicatore(4)(5)) #20

def contatore():
    conta = 0
    def incremento():
        nonlocal conta #mi permette di accedere in scrittura alla variabile della funzione esterna
        conta += 1
        return conta
    return incremento

counter = contatore()
print(counter())
print(counter())
print(counter())