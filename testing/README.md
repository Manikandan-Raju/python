# Testing Examples

This folder contains examples for Python testing using `unittest`, `pytest`, and `coverage`.

## Files

- `calculator.py` - small example module for arithmetic operations.
- `test_calculator_unittest.py` - basic `unittest` examples.
- `test_calculator_unittest_advanced.py` - advanced `unittest` concepts such as setup/teardown, subtests, skip, and expected failures.
- `test_calculator_pytest.py` - basic `pytest` examples.
- `test_calculator_pytest_advanced.py` - advanced `pytest` concepts including fixtures, markers, xfail, and custom CLI flags.
- `conftest.py` - `pytest` fixture definitions and custom command-line option handling.
- `pytest.ini` - pytest configuration and marker registration.
- `requirements.txt` - test dependencies.
- `run_tests.sh` - convenience script to run pytest from the `testing` folder.
- `run_coverage.sh` - convenience script to run coverage and generate HTML report.

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
cd testing
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
chmod +x run_tests.sh run_coverage.sh
```

> If you already have a shared project virtual environment, install `pytest` and `coverage` there instead of creating a second venv.

## Run tests

### Using unittest

```bash
cd testing
python -m unittest discover -s . -p 'test_*.py'
```

### Using pytest

```bash
cd testing
pytest
```

### Run only the advanced pytest tests

```bash
cd testing
pytest test_calculator_pytest_advanced.py
```

### Run slow tests with pytest

```bash
cd testing
pytest --runslow
```

### Using helper script

```bash
cd testing
./run_tests.sh
```

## Coverage

```bash
cd testing
./run_coverage.sh
```

The HTML report will be generated at `testing/htmlcov/index.html`.

## Concepts covered

- `unittest`
  - `TestCase` classes
  - `setUp`, `tearDown`, `setUpClass`, `tearDownClass`
  - `assertRaises`, `assertRaisesRegex`
  - `subTest`
  - `skip` and `expectedFailure`
- `pytest`
  - simple asserts
  - `@pytest.mark.parametrize`
  - fixtures in `conftest.py`
  - custom markers (`slow`)
  - `pytest.raises`
  - `skip` and `xfail`
  - custom CLI option `--runslow`
- `coverage`
  - measure test coverage
  - generate terminal and HTML reports
