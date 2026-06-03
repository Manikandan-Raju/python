# 12_memory_model.py
# Basic Python memory model: stack vs heap and object lifetime.

# In Python, variables are names bound to objects.
# Objects are allocated on the heap.
# The stack holds references and function call frames.

x = 10
y = x
print('x id:', id(x))
print('y id:', id(y))
print('Same integer object reused for small ints? ->', x is y)
print()

# Example with a mutable object:
list_a = [1, 2, 3]
list_b = list_a
print('list_a id:', id(list_a))
print('list_b id:', id(list_b))
list_b.append(4)
print('list_a after append via list_b:', list_a)
print()

# Stack vs heap:
# - Heap: where Python objects live.
# - Stack: where function calls, local variables, and return addresses are tracked.

# Reference counting and garbage collection:
# CPython tracks how many references exist to each object.
# When count reaches zero, the object can be freed.
# A cyclic garbage collector handles reference cycles.

# Example of object lifetime:
def make_list():
    data = [1, 2, 3]
    return data

result = make_list()
print('Returned object still alive because result references it:', result)

# Important note:
# Python variables are labels, not boxes holding values directly.
# The interpreter manages memory automatically, so explicit free/delete is usually not needed.
