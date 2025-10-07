class Persona:
    def __init__(self, nome):
        self.nome = nome

if __name__ == '__main__':

    p = Persona("Paolo")

    print(p.nome) #accesso diretto, se non esiste il campo si spacca...perciò usiamo getter
    print(getattr(p,"nome")) #ma così si spaccherebbe comunque se il campo non esistesse
    print(getattr(p,"eta",32)) #così invece definiamo un default se il campo non esiste