# 03_decorator_arguments.py
# Decorators can accept arguments by adding another outer function.

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

# This prints the greeting three times.
greet("Alice")
