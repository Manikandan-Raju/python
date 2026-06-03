import pytest
import calculator
from calculator import add, divide, multiply, subtract


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (-4, 4, 0),
        (100, 1, 101),
    ],
    ids=["positive", "negative", "large"],
)
def test_add_with_parametrization(a, b, expected):
    """
    Demonstrate parameterized pytest tests with custom ids.
    
    ids parameter:
    - Provides human-readable names for each parameter set
    - Without ids: test_add_with_parametrization[2-3-5], [p-4-4-0], etc. (hard to read)
    - With ids: test_add_with_parametrization[positive], [negative], [large] (clear & descriptive)
    - ids must match the number of parameter tuples (3 tuples = 3 ids)
    
    When you run: pytest -v testing/test_calculator_pytest_advanced.py::test_add_with_parametrization
    Output shows:
        test_add_with_parametrization[positive] PASSED
        test_add_with_parametrization[negative] PASSED
        test_add_with_parametrization[large] PASSED
    """
    assert add(a, b) == expected


def test_subtract_and_multiply(calculator_functions):
    """Use a dictionary fixture to share calculator functions."""
    assert calculator_functions["subtract"](5, 2) == 3
    assert calculator_functions["multiply"](5, 2) == 10


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (8, 4, 2.0),
        (7, 2, 3.5),
    ],
    ids=["even-division", "odd-division"],
)
def test_divide_with_parametrization(a, b, expected):
    assert divide(a, b) == expected


def test_divide_raises_value_error():
    """Use pytest.raises to verify exceptions."""
    with pytest.raises(ValueError, match="zero"):
        divide(10, 0)


def test_monkeypatch_add(monkeypatch):
    """Show how to monkeypatch a module function in pytest."""
    monkeypatch.setattr(calculator, "add", lambda a, b: 999)
    assert calculator.add(1, 2) == 999


def test_write_results_to_tmp_path(tmp_path):
    """
    Demonstrate tmp_path fixture for temporary file creation.
    
    tmp_path fixture:
    - Built-in pytest fixture (not defined in conftest.py or anywhere else)
    - Provided automatically by pytest
    - Creates a unique temporary directory for each test
    - Auto-cleanup: directory is deleted after test runs
    - Type: pathlib.Path object
    
    Where does tmp_path come from?
    - pytest has ~20+ built-in fixtures available automatically
    - No import or definition needed
    - Just add 'tmp_path' as a function parameter
    - pytest injects it automatically when running the test
    
    Other built-in pytest fixtures:
    - capfd: capture stdout/stderr
    - monkeypatch: mock/patch functions
    - capsys: capture print output
    - tmpdir: temporary directory (older API)
    - request: test request object
    - caplog: capture logging output
    
    Usage: tmp_path / "filename" creates a Path object for file operations
    """
    output_file = tmp_path / "result.txt"
    output_file.write_text(f"result={add(10, 5)}")
    assert output_file.read_text() == "result=15"


def test_capture_printed_output(capfd):
    """Demonstrate capturing stdout/stderr output."""
    print(add(1, 2))
    captured = capfd.readouterr()
    assert captured.out.strip() == "3"


@pytest.mark.skip(reason="Demonstration of a skipped test")
def test_skip_demo():
    assert add(2, 2) == 4


@pytest.mark.xfail(reason="Example xfail for unsupported behavior")
def test_xfail_demo():
    assert divide(1, 0) == 0


@pytest.mark.slow
def test_slow_math_operation():
    assert multiply(7, 6) == 42


def test_sample_numbers_fixture(sample_numbers):
    """Use a parametrized fixture defined in conftest.py."""
    a, b, expected = sample_numbers
    assert add(a, b) == expected
