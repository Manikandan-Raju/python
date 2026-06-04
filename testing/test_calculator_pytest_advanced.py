import pytest
import calculator
from pathlib import Path
from typing import Any, Dict, Tuple
from unittest.mock import MagicMock
from calculator import add, divide, multiply, subtract, some


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (-4, 4, 0),
        (100, 1, 101),
    ],
    ids=["positive", "negative", "large"],
)
def test_add_with_parametrization(a: int, b: int, expected: int) -> None:
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


def test_subtract_and_multiply(calculator_functions: Dict[str, Any]) -> None:
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
def test_divide_with_parametrization(a: float, b: float, expected: float) -> None:
    assert divide(a, b) == expected


def test_divide_raises_value_error():
    """Use pytest.raises to verify exceptions."""
    with pytest.raises(ValueError, match="zero"):
        divide(10, 0)


def test_monkeypatch_add(monkeypatch: pytest.MonkeyPatch) -> None:
    """Show how to monkeypatch a module function in pytest."""
    monkeypatch.setattr(calculator, "add", lambda a, b: 999)
    assert calculator.add(1, 2) == 999


def test_monkeypatch_some(monkeypatch: pytest.MonkeyPatch) -> None:
    """Demonstrate monkeypatching an internal function used by another function."""
    monkeypatch.setattr(calculator, "add", lambda a, b: 42)

    # calculator.some currently uses calculator.add() internally.
    assert calculator.some(1, 2) == 42


def test_write_results_to_tmp_path(tmp_path: Path) -> None:
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


def test_capture_printed_output(capfd: pytest.CaptureFixture[str]) -> None:
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


def test_sample_numbers_fixture(sample_numbers: Tuple[int, int, int]) -> None:
    """Use a parametrized fixture defined in conftest.py."""
    a, b, expected = sample_numbers
    assert add(a, b) == expected


def test_mock(mocker: Any) -> None:
    """Use the pytest-mock plugin's mocker fixture."""
    mock_add = mocker.patch("calculator.add", return_value=42)
    result = some(1, 2)  # some() calls add() internally
    # Check exactly one call
    mock_add.assert_called_once_with(1, 2)
    assert some(1,2) == 42


def test_magic_mock() -> None:
    """Demonstrate unittest.mock.MagicMock for a calculator-style object.

    MagicMock creates a fake object whose methods can be configured and inspected.
    This differs from monkeypatch, which replaces real module attributes in-place.
    """
    magic_calc = MagicMock(name="magic_calc")
    magic_calc.add.return_value = 10
    magic_calc.subtract.return_value = -1
    magic_calc.multiply.return_value = 2
    magic_calc.divide.return_value = 0.5

    result = (
        magic_calc.add(1, 2)
        + magic_calc.subtract(1, 2)
        + magic_calc.multiply(1, 2)
        + magic_calc.divide(1, 2)
    )

    assert result == 11.5
    magic_calc.add.assert_called_once_with(1, 2)
    assert magic_calc.subtract.call_count == 1


def test_pytest_magic_mock(mocker: Any) -> None:
    m = mocker.MagicMock(name="magic_calc")
    m.add.return_value = 10
    assert m.add(1, 2) == 10

    # `m` is a standalone MagicMock object, so calling `some()` still uses
    # the real calculator.add() function unless that function is patched.
    mocker.patch("calculator.add", return_value=999)

    assert some(1, 2) == 999


@pytest.fixture(params=[(1, 2, 3), (2, 3, 5), (3, 4, 7)])
def some_fixture(request: pytest.FixtureRequest) -> Tuple[int, int, int]:

    return request.param

def test_some_fixture(some_fixture: Tuple[int, int, int]) -> None:
    a,b, expected = some_fixture
    assert add(a,b) == expected


@pytest.mark.parametrize("a,b,expected", [(1,2,3),(2,3,5),(3,4,7)], ids=["case1","case2","case3"])
def test_some_parametrize(a: int, b: int, expected: int) -> None:
    assert add(a,b) == expected
    