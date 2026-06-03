# 11_data_structures.py
# Study of Python built-in data structures and their important properties.

# List
numbers = [1, 2, 3]
print('List:', numbers)
print('Ordered:', numbers[0], numbers[1])
print('Mutable:', end=' ')
numbers[0] = 10
print(numbers)
print('Duplicates allowed:', [1, 1, 2])
print()

# Tuple
point = (1, 2)
print('Tuple:', point)
print('Ordered:', point[0], point[1])
try:
    point[0] = 10
except TypeError as exc:
    print('Tuple immutable error:', exc)
print('Duplicates allowed:', (1, 1, 2))
print()

# Set
items = {3, 1, 2}
print('Set:', items)
print('Unordered: element order is not guaranteed')
print('Mutable:', end=' ')
items.add(4)
print(items)
print('Duplicates removed:', {1, 1, 2})
print('Hashable values only: use immutable elements like tuples')
print()

# Dictionary
person = {'name': 'Alice', 'age': 30}
print('Dictionary:', person)
print('Key order preserved in Python 3.7+')
print('Mutable:', end=' ')
person['age'] = 31
print(person)
print('Keys must be hashable, values can be any object')
print()

# Summary:
# - list: ordered, mutable, allows duplicates
# - tuple: ordered, immutable, allows duplicates
# - set: unordered, mutable, no duplicates, hashable elements only
# - dict: ordered mapping of keys to values, mutable, keys must be hashable
