# 05_polymorphism.py
# Demonstrates polymorphism and method overriding in Python.

class Animal:
    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Robot:
    def speak(self):
        return "Beep boop."


animals = [Dog(), Cat(), Robot()]
for creature in animals:
    print(f"{creature.__class__.__name__} says: {creature.speak()}")

# Polymorphism allows code to work with any object that implements the same interface.
