from typing import List


class Animal:
    def speak(self):
        raise NotImplementedError("Method not implemented")

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Bird(Animal):
    def speak(self):
        return "Cip"

if __name__ == '__main__':
    # animals = [Dog(), Cat(), Bird()]
    animals : List[Animal] = [Dog(), Cat(), Bird()]
    for animal in animals:
        print(animal.speak())
