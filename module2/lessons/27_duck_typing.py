class Animal:
    def speak(self):
        raise NotImplementedError("Method not implemented")

class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

class Bird:
    def speak(self):
        return "Cip"

if __name__ == '__main__':
    animals = [Dog(), Cat(), Bird()] #funziona per il duck typing...ogni classe ha "casualmente" il metodo speak()
    for animal in animals:
        print(animal.speak())
