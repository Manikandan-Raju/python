


def capitalize(func):
    def inner_func(s:str):
        if s.startswith('m'):
            raise ValueError
        else:
            s = s.capitalize()
        return func(s)
    return inner_func

@capitalize
def greet(s):
    pass
try:
    greet("mani")
except ValueError as e:
    print(str(e))
