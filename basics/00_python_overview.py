# 00_python_overview.py
# Python is an interpreted language with a compilation step to bytecode.

# 1. Source code
# Python code is written in .py files. This is the human-readable source.

# 2. Compilation
# CPython compiles the source into bytecode, which lives in .pyc files.
# This is not machine code, but a lower-level portable representation.

# 3. Interpreter / Virtual Machine
# The Python interpreter executes bytecode on the Python Virtual Machine (PVM).
# CPython is the most common implementation, but there are others like PyPy and Jython.

# Example:
print('Hello from Python')

# Behind the scenes, CPython performs these steps:
#  - parse source into an abstract syntax tree (AST)
#  - compile AST into bytecode
#  - execute bytecode in the interpreter loop

# Source -> bytecode -> execution
# The process is roughly:
#   python script.py
#     source file parsed -> AST
#     AST compiled -> bytecode
#     bytecode executed by CPython runtime

# Python is not "compiled to native object code" like C/C++ by default.
# Instead, it uses an interpreter and a runtime engine.

# Note:
#  - A .pyc file is cached compiled bytecode.
#  - The interpreter still loads the bytecode and executes it at runtime.
