@echo off
REM Run Robot Framework tests on Windows using the repository virtualenv.
set SCRIPT_DIR=%~dp0
set ROOT_DIR=%SCRIPT_DIR%..\
set VENV_ROBOT=%ROOT_DIR%\.venv\Scripts\robot.exe
set VENV_PYTHON=%ROOT_DIR%\.venv\Scripts\python.exe
set REQ_FILE=%SCRIPT_DIR%requirements.txt

if exist "%VENV_ROBOT%" (
  "%VENV_ROBOT%" "%SCRIPT_DIR%tests\01_example.robot"
  exit /b %errorlevel%
)

if exist "%VENV_PYTHON%" (
  "%VENV_PYTHON%" -m robot.run "%SCRIPT_DIR%tests\01_example.robot"
  exit /b %errorlevel%
)

echo Robot Framework is not installed in %ROOT_DIR%\.venv\Scripts
echo Install dependencies with:
echo     "%VENV_PYTHON%" -m pip install -r "%REQ_FILE%"
exit /b 1
