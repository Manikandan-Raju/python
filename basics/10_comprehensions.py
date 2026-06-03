# 10_comprehensions.py
# List, dict, and set comprehensions are compact and common in interviews.

numbers = range(1, 11)
print("Numbers:", list(numbers))

# List comprehension with condition
squares = [x * x for x in numbers if x % 2 == 0]
print("Even squares:", squares)

# Dict comprehension from a list
square_map = {x: x * x for x in numbers}
print("Square map:", square_map)

# Set comprehension removes duplicates automatically
chars = {c for c in 'interview' if c in 'aeiou'}
print("Vowels in 'interview':", chars)
