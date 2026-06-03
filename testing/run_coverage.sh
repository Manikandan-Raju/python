#!/usr/bin/env bash
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
if [ -f .venv/bin/activate ]; then
  source .venv/bin/activate
fi
coverage run -m pytest
coverage report -m
coverage html
echo "Coverage HTML report generated at: $SCRIPT_DIR/htmlcov/index.html"
