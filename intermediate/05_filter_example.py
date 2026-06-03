# filter_example.py
# Demonstrates Python's built-in filter() for selecting items from a sequence.

values = [10, 15, 20, 25, 30, 35]

# filter keeps elements where the predicate returns True.
even_values = filter(lambda x: x % 2 == 0, values)
print("Original:", values)
print("Even values:", list(even_values))

# filter with a named function makes the code clearer.
def is_large(x):
    return x > 20

large_values = filter(is_large, values)
print("Values greater than 20:", list(large_values))
