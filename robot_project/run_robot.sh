#!/usr/bin/env bash
set -e

# Run Robot Framework tests for the example project using the repository virtualenv.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV_PYTHON="$REPO_ROOT/.venv/bin/python"
VENV_ROBOT="$REPO_ROOT/.venv/bin/robot"
REQ_FILE="$SCRIPT_DIR/requirements.txt"

if [ -x "$VENV_ROBOT" ]; then
  "$VENV_ROBOT" "$SCRIPT_DIR/tests/01_example.robot"
  exit 0
fi

if [ -x "$VENV_PYTHON" ]; then
  if "$VENV_PYTHON" -m robot.run --help >/dev/null 2>&1; then
    "$VENV_PYTHON" -m robot.run "$SCRIPT_DIR/tests/01_example.robot"
    exit 0
  fi

  if "$VENV_PYTHON" -m pip show robotframework >/dev/null 2>&1; then
    echo "Error: Robot Framework is installed, but the module entrypoint failed to run."
    echo "Try reinstalling dependencies:"
    echo "  \"$VENV_PYTHON\" -m pip install -r \"$REQ_FILE\""
    exit 1
  fi

  echo "Robot Framework is not installed in the virtualenv."
  echo "Install it with:"
  echo "  \"$VENV_PYTHON\" -m pip install -r \"$REQ_FILE\""
  exit 1
fi

echo "Virtualenv Python not found at: $VENV_PYTHON"
echo "Create and activate the virtualenv, then install dependencies:"
echo "  python3 -m venv $REPO_ROOT/.venv"
echo "  source $REPO_ROOT/.venv/bin/activate"
echo "  pip install -r $REQ_FILE"
exit 1
