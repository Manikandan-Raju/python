# In Python, a decorator is a design pattern that 
# allows you to modify the functionality of a 
# function by wrapping it in another function.

def capitalize(func):
    def inner(name):
        name = name.capitalize()
        return func(name)
    return inner

def greet(func):
    def inner(name):
        name = "Hi , I am " + name
        return func(name)
    return inner

def add_stars(func):
    def inner(name):
        name = "***********\n" + name + "\n*************"
        return func(name)
    return inner


@capitalize
@greet
@add_stars
def show(name):
    print(name)


show("mani")