"""Namespace example: global, local, nested, and nonlocal scope.

This file shows how Python resolves names in different namespaces:
- global namespace: module-level variables
- local namespace: variables inside a function
- nested local namespace: variables inside an inner function

It also shows how `global` and `nonlocal` change where assignments apply.
"""

# global_var is in the global namespace
global_var = 10
print("global_var initialized to", global_var)

def local_example():
    print("\n--- local_example start ---")
    local_var = 99
    print("local_var local to local_example() =", local_var)
    print("local_var is only visible inside local_example()")
    print("--- local_example end ---")


def outer_function():
    print("\n--- outer_function start ---")
    outer_var = 20
    print("outer_var local to outer_function =", outer_var)

    def inner_function():
        print("  --- inner_function start ---")
        inner_var = 30
        print("  inner_var local to inner_function =", inner_var)

        # `global` makes global_var refer to the module-level name
        global global_var
        global_var = 40
        print("  module-level global_var changed to", global_var)

        # This creates/changes module-level outer_var, not outer_function's local outer_var
        global outer_var
        outer_var = 50
        print("  module-level outer_var changed to", outer_var)
        print("  --- inner_function end ---")

    inner_function()
    print("outer_function sees its own outer_var =", outer_var)
    print("--- outer_function end ---")


def nonlocal_example():
    print("\n--- nonlocal_example start ---")
    outer_var = 20
    print("outer_var before nonlocal =", outer_var)

    def inner_nonlocal():
        # nonlocal means use the nearest enclosing function's variable
        # instead of creating a new local variable here.
        nonlocal outer_var
        outer_var = 50
        print("  nonlocal inner changed outer_var to", outer_var)

    inner_nonlocal()
    print("outer_var after nonlocal =", outer_var)
    print("--- nonlocal_example end ---")


def a():
    outer_var = 2
    print("a() local outer_var =", outer_var)


print("call outer_function")
outer_function()
print("module-level outer_var after outer_function =", outer_var)
nonlocal_example()
a()
print("module-level outer_var after a() =", outer_var)
print("module-level global_var =", global_var)
