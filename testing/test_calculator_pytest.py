import pytest

from calculator import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 2, 5),
        (-1, 5, 4),
        (0, 0, 0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 3, 7),
        (5, 7, -2),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-2, -2) == 4


def test_divide():
    assert divide(9, 3) == 3
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
