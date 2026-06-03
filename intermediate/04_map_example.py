# map_example.py
# Demonstrates Python's built-in map() for applying a function to every item.

values = [1, 2, 3, 4, 5]

# map applies the lambda to each element and returns an iterator.
squared = map(lambda x: x * x, values)
print("Original:", values)
print("Squared:", list(squared))

# map can also work with multiple sequences at once.
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
combined = map(lambda letter, number: f"{letter}{number}", letters, numbers)
print("Combined:", list(combined))
