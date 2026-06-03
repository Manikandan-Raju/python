"""Iterable vs iterator example with explanations.

Remember:
- Iterable: an object you can loop over (`list`, `tuple`, `str`, etc.)
- Iterator: an object that produces items one by one via `next()`
- `iter(obj)` returns an iterator for an iterable object
"""

numbers = [1, 4, 9]

# Check whether the object supports iteration.
methods = dir(numbers)
if '__iter__' in methods:
    print('list is an iterable')

# Create an iterator from the iterable.
# This is the same as calling numbers.__iter__().
value = iter(numbers)

# `next(iterator)` returns the next item from the iterator.
item1 = next(value)
print('first item from iterator:', item1)

# You can continue consuming values one by one.
item2 = next(value)
item3 = next(value)
print('next items:', item2, item3)

# Once the iterator is exhausted, next() raises StopIteration.
try:
    next(value)
except StopIteration:
    print('iterator exhausted')
