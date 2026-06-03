# Robot Framework Example Project

This is a small Robot Framework example project showing:
- Robot test cases in `.robot`
- a Python keyword library
- a simple test execution workflow

## Setup

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run tests

From the workspace root:

```bash
./robot_project/run_robot.sh
```

Or from the `robot_project` folder:

```bash
cd robot_project
./run_robot.sh
```

On Windows (command prompt):

```bat
cd robot_project
run_robot.bat
```

On Windows PowerShell:

```powershell
Set-Location robot_project
python -m robot.run tests\01_example.robot
```

If Robot Framework is not installed yet, install dependencies first:

```bash
cd robot_project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Project structure

- `requirements.txt` — robotframework dependency
- `keywords/ExampleLibrary.py` — Python keyword library for Robot
- `tests/01_example.robot` — example Robot Framework test cases
- `run_robot.sh` — convenience script to run the tests
