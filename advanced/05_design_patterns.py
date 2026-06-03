# 05_design_patterns.py
# Advanced design pattern examples: singleton and factory.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    pass


s1 = Singleton()
s2 = Singleton()
print('Singleton same instance:', s1 is s2)


class Animal:
    def speak(self):
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        return 'Woof'


class Cat(Animal):
    def speak(self):
        return 'Meow'


class AnimalFactory:
    @staticmethod
    def create(animal_type: str) -> Animal:
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        raise ValueError('Unknown animal type')


print('Factory dog:', AnimalFactory.create('dog').speak())
print('Factory cat:', AnimalFactory.create('cat').speak())
