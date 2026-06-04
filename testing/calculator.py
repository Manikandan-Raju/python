"""Simple calculator module used for unit testing and pytest examples."""

from __future__ import annotations

def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Raises ValueError when dividing by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def some(a: float, b: float) -> float:
    return add(a,b) #+ subtract(a,b) + multiply(a,b) + divide(a,b)