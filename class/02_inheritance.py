"""Multiple inheritance example with Python MRO, super(), and attribute lookup."""

class A:
    i = 1
    j = 2

    def __init__(self) -> None:
        self.a = 1
        super().__init__()


    def method(self):
        print("A")


class Z:
    def __init__(self) -> None:
        # Z does not call super().__init__(), so its own initialization
        # only applies if Z.__init__ is reached by super() in the MRO.
        super().__init__()
        self.a = 26

    def method(self):
        print("Z")


class B(A, Z):
    # B inherits from A first, then Z. This means the MRO for B is:
    # B -> A -> Z -> object
    # So super().__init__() in B calls A.__init__ before Z.__init__.
    def __init__(self) -> None:
        # super() follows the MRO, not the textual order of the base classes.
        super().__init__()
        # B itself does not set self.a, so the final value depends on
        # whichever __init__ runs later in the MRO chain.

    # If B defined method(), it would override A.method() and Z.method()
    # for B and any subclasses of B.
    # def method(self):
    #     print("B")


class C(A):
    def __init__(self) -> None:
        super().__init__()
        self.a = 3

    # def method(self):
    #     print("C")


class D(C, B):
    def __init__(self) -> None:
        super().__init__()
        # D does not override `method` or `a`.


print("D MRO:", [cls.__name__ for cls in D.__mro__])

# Create an instance of D.
d = D()

# method() is resolved by the MRO: D -> C -> B -> A -> Z -> object.
# Since C and B do not override method(), A.method() is called.
d.method()

# Attribute `a` is assigned by A.__init__ and then overwritten by C.__init__.
print("d.a =", d.a)
b= B()
print("b.a =", b.a)