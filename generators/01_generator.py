"""Generator example showing how yield produces values lazily.

Remember this:
- A generator produces one value at a time.
- It does not compute the whole sequence up front.
- Use `next()` or a `for` loop to consume values.
"""

def all_even():
    """Infinite generator that yields even numbers starting from 0."""
    n = 0
    while True:
        # `yield` pauses the function and returns one value.
        # When `next()` is called again, execution resumes after this line.
        yield n
        n += 2


# Create the generator object. No values are produced yet.
gen = all_even()
print("generator object created:", gen)

# Use the generator lazily, here printing first 10 even numbers.
# The generator only calculates each value when needed.
print("first 10 even numbers:")
for _ in range(10):
    print(next(gen))

# Generators are memory efficient because they never store the whole list.
# If we used a list instead, all values would be stored in memory.

# Example generator expression: similar behavior, but shorter syntax.
# This also creates a generator, not a list.
gen_expr = (i for i in range(0, 20, 2))
print("generator expression output:", list(gen_expr))

# Once a generator is exhausted, it cannot be reused.
# A fresh generator must be created to iterate again.
