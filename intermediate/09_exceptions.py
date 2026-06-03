# 09_exceptions.py
# Shows basic exception handling and custom exception classes.

class NegativeValueError(ValueError):
    pass


def compute_square_root(x):
    if x < 0:
        raise NegativeValueError("Cannot compute square root of negative value")
    return x ** 0.5

for value in [9, 0, -4]:
    try:
        print(f"sqrt({value}) =", compute_square_root(value))
    except NegativeValueError as exc:
        print("Caught error:", exc)
    finally:
        print("Done with value", value)
