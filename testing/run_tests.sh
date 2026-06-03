#!/usr/bin/env bash
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"
if [ -f .venv/bin/activate ]; then
  # Activate the local testing virtualenv when present.
  source .venv/bin/activate
fi
pytest
