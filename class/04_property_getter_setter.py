# 04_property_getter_setter.py
# Demonstrates Python getter/setter behavior using properties.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        """The getter for name."""
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

    @property
    def age(self):
        """The getter for age."""
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"


p = Person("Alice", 30)
print(p)
print("Name:", p.name)
print("Age:", p.age)

p.name = "Bob"
p.age = 25
print("Updated:", p)

try:
    p.age = -1
except ValueError as exc:
    print("Error:", exc)
