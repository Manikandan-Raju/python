# 12_dev_workflow.py
# Overview of Python developer workflow tools: style, linting, formatting, testing, typing, and virtualenv.

# 1. Style and standards
# PEP 8 is the standard style guide for Python.
# PEP 257 covers docstrings.
# PEP 20 is the Zen of Python.

print('PEP 8 says: use 4 spaces, short lines, and readable names.')

# 2. Formatting
# A formatter makes code consistent automatically.
# Common tools:
#   black myfile.py
#   isort mypackage/
#   autopep8 --in-place myfile.py

# 3. Linting
# Linters find style issues and possible bugs.
# Common tools:
#   flake8 mypackage/
#   pylint mypackage/
#   pycodestyle myfile.py

# 4. Testing
# Test frameworks help verify behavior.
# - unittest (built into Python)
# - pytest
# - doctest
# Example:
#   pytest tests/
#   python -m unittest discover

# 5. Type checking
# Optional static type checking is useful for finding mistakes early.
#   mypy mypackage/
#   pyright .

# 6. Virtual environments and dependency management
# Use an isolated environment so dependencies do not conflict.
#   python -m venv .venv
#   source .venv/bin/activate
#   pip install -r requirements.txt

# 7. Packaging and metadata
# Modern Python projects often use pyproject.toml.
# Example in code organization:
#   src/mypackage/__init__.py
#   tests/test_example.py

# 8. Version control and CI
# Good practice for interview-ready projects:
# - use git for source control
# - write clear commit messages
# - use automated CI to run lint, format, and tests

# Basic example testable code and docstring:

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


if __name__ == '__main__':
    print('add(2, 3) =', add(2, 3))
