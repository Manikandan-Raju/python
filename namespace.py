# global_var is in the global namespace
global_var = 10
print("init global_var",global_var)

def outer_function():
    print("Go to outer function")
    #  outer_var is in the local namespace 
    outer_var = 20
    print("init outer_var",outer_var)

    def inner_function():
        print("Go to inner function")
        #  inner_var is also in the local namespace 
        inner_var = 30
        print("init inner_var",inner_var)
        global global_var
        global_var = 40
        print("change global_var to 40 with global keyword",global_var)

        global outer_var
        outer_var = 50
        print("change outer_var to 50 with global keyword",outer_var)
    inner_function()
    print("Out of inner function")
    print("check outer_var",outer_var)
    print("Out of outer function")


def a():
    outer_var = 2
    print("check outer_var",outer_var)


# call the outer function and print local and nested local variables
print("call outer function")
outer_function()
print("check outer_var",outer_var)
a()
print("check outer_var",outer_var)
print("global_var",global_var)