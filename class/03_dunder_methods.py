# 03_dunder_methods.py
# Special methods let objects support built-in operations.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __bool__(self):
        return self.x != 0 or self.y != 0

p1 = Point(1, 2)
p2 = Point(3, 4)
print("p1:", p1)
print("p2:", p2)
print("p1 + p2:", p1 + p2)
print("p1 == p2:", p1 == p2)
print("bool(Point(0,0)):", bool(Point(0, 0)))
