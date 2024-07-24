# In Python, a decorator is a design pattern that 
# allows you to modify the functionality of a 
# function by wrapping it in another function.

def add_stars(func):
    def inner(s):
        print("\n***********")
        func(s)
        print("***********\n")
    return inner


def greet(func):
    def inner(s):
        print("Hello! ",end="")
        func(s)
    return inner

def capitalize(func):
    def inner(s:str):
        if not s.startswith('m'):
            raise ValueError
        else:
            s = s.capitalize()
        func(s)
    return inner

@add_stars
@greet
@capitalize
def out(s):
    print(s)
    
out("mani")