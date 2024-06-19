#!/bin/sh
echo "run"
pip install -r requirements.txt
pytest --cov=regex . --cov-report html