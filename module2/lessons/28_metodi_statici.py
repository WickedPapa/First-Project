class Calcolatrice:

    @staticmethod #decoratore
    def somma(a, b):
        return a + b

if __name__ == '__main__':
    print(Calcolatrice.somma(1, 2))