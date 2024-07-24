

class A:
    i = 1
    j = 2
    def __init__(self) -> None:
        self.a = 1
    
    def method(self):
        print("A")

class Z:
    def __init__(self) -> None:
        # super().__init__()
        self.a = 26
    
    def method(self):
        print("Z")


class B(A,Z):
    def __init__(self) -> None:
        super().__init__()
        pass
        # self.a = 2
    
    # def method(self):
    #     print("B")

class C(A):
    def __init__(self) -> None:
        super().__init__()
        self.a = 3
        
    # def method(self):
    #     print("C")

class D(C,B):
    def __init__(self) -> None:
        super().__init__()
        pass


d = D()
d.method()
print(d.a)