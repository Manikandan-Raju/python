# 01_metaclasses.py
# Advanced metaprogramming: how metaclasses control class creation.

class UpperAttrMeta(type):
    def __new__(cls, name, bases, attrs):
        uppercase_attrs = {
            key.upper(): value
            for key, value in attrs.items()
            if not key.startswith('__')
        }
        return super().__new__(cls, name, bases, uppercase_attrs)


class MyClass(metaclass=UpperAttrMeta):
    value = 5


print('Has VALUE:', hasattr(MyClass, 'VALUE'))
print('VALUE:', MyClass.VALUE)
