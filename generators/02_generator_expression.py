# 02_generator_expression.py
# Generator expressions are a concise alternative to generator functions.

squares = (x * x for x in range(10))
print("Generator object:", squares)
print("First value:", next(squares))
print("Remaining values:", list(squares))

# Generator expressions are lazy and use little memory.
large = (x * x for x in range(1_000_000))
print("First large square:", next(large))
