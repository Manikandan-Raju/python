# reduce_example.py
# Demonstrates functools.reduce() for combining items in a sequence.

from functools import reduce

values = [1, 2, 3, 4, 5]

# reduce applies the function cumulatively and returns a single result.
product = reduce(lambda a, b: a * b, values)
print("Values:", values)
print("Product:", product)

# reduce can also start from an initial value.
sum_with_offset = reduce(lambda a, b: a + b, values)
print("Sum with offset 100:", sum_with_offset)

sum_with_offset = reduce(lambda a, b: a + b, values, 100)
print("Sum with offset 100:", sum_with_offset)

# Another example: concatenate strings.
words = ["hello", "world", "from", "reduce"]
phrase = reduce(lambda a, b: a + " " + b, words)
print("Phrase:", phrase)
