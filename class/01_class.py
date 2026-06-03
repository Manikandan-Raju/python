# 01_class.py
# Basic object-oriented programming example with constructor, method, and inheritance.

class Parent:
    def __init__(self, name):
        # Public attribute
        self.name = name

    def greet(self):
        # Instance method: works with the specific object instance.
        print(f"Hello, my name is {self.name}.")

    @classmethod
    def species(cls):
        # Class method: receives the class, not the instance.
        return cls.__name__

    @staticmethod
    def is_adult(age):
        # Static method: no implicit first argument.
        return age >= 18


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        # Instance method can access both instance data and parent behavior.
        print(f"Name: {self.name}, Age: {self.age}")

    def greet(self):
        # Method overriding: child changes the inherited behavior.
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


# Driver code to show how the classes work.
obj = Child("Mani", 6)
obj.display()
obj.greet()
print('Parent species:', Parent.species())
print('Child species:', Child.species())
print('Is 20 adult?', Parent.is_adult(20))
print('Is 16 adult?', Child.is_adult(16))

