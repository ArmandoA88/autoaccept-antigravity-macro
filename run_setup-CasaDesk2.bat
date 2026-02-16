@echo off
cd /d "%~dp0"

echo [Step 1] Checking Python...
python --version >NUL 2>&1
if %errorlevel% neq 0 (
    echo Python is not recognized. Please install Python.
    pause
    exit /b
)

echo [Step 2] Checking PyAutoGUI library...
python -c "import pyautogui;" >NUL 2>&1
if %errorlevel% neq 0 (
    echo PyAutoGUI missing. Installing dependencies...
    pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
    if %errorlevel% neq 0 (
        echo Failed to install dependencies.
        pause
        exit /b
    )
) else (
    echo Dependencies are ready.
)

echo.
echo [Step 3] Starting Setup Wizard...
python setup_macro.py

echo.
echo Setup finished.
pause
