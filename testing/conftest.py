"""
conftest.py is a special pytest file that is automatically discovered and loaded.

How it works:
- pytest automatically finds and loads conftest.py before running tests
- No explicit import needed — pytest handles it
- Fixtures defined here are available to all test files in the same directory
- You can have multiple conftest.py files at different directory levels

pytest discovery order for conftest.py:
1. pytest starts from the test directory or specified path
2. It searches for conftest.py files going up the directory tree
3. Each conftest.py found is loaded and executed
4. Fixtures and hooks from all conftest.py files are available

Example: conftest.py in testing/ makes fixtures available to:
- test_calculator_pytest.py
- test_calculator_pytest_advanced.py
- test_calculator_unittest.py
- All other test files in testing/
"""

import pytest

from calculator import add, subtract, multiply, divide


@pytest.fixture(scope="module")
def calculator_functions():
    """
    Fixture: Provide calculator functions as a reusable dictionary.
    
    Scope: module — created once per test module
    Usage: Any test function can accept this as a parameter
    """
    return {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }


@pytest.fixture(params=[(1, 2, 3), (0, 0, 0), (-1, 1, 0)])
def sample_numbers(request):
    """
    Fixture: Parametrized fixture that yields different tuples.
    
    params: runs the fixture (and any test using it) 3 times
    request.param: the current parameter value
    Usage: Tests that use this fixture will run multiple times
    """
    return request.param


def pytest_addoption(parser):
    """
    Hook: Register custom command-line options.
    
    This allows users to pass --runslow to pytest
    """
    parser.addoption(
        "--runslow",
        action="store_true",
        default=False,
        help="Run slow tests marked with @pytest.mark.slow.",
    )


def pytest_runtest_setup(item):
    """
    Hook: Called before each test runs.
    
    This checks if a test has the 'slow' marker.
    If --runslow is not passed, slow tests are skipped.
    """
    if "slow" in item.keywords and not item.config.getoption("--runslow"):
        pytest.skip("need --runslow option to run")
