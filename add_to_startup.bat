@echo off
cd /d "%~dp0"

:: 1. Generate run_silent.vbs with dynamic path
set "VBS_PATH=%~dp0run_silent.vbs"
set "BAT_PATH=%~dp0run_macro.bat"

echo Creating run_silent.vbs...
> "%VBS_PATH%" echo Set WshShell = CreateObject("WScript.Shell")
>> "%VBS_PATH%" echo WshShell.Run chr(34) ^& "%BAT_PATH%" ^& chr(34), 0
>> "%VBS_PATH%" echo Set WshShell = Nothing

:: 2. Create Shortcut to run_silent.vbs in Startup folder
set "STARTUP_DIR=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
set "SHORTCUT_PATH=%STARTUP_DIR%\AutoAcceptMacro.lnk"

echo.
echo --- Add to Startup ---
echo This will make the macro run silently in the background when you log in.
echo.

powershell -NoProfile -Command "$s=(New-Object -COM WScript.Shell).CreateShortcut(\"%SHORTCUT_PATH%\");$s.TargetPath=\"%VBS_PATH%\";$s.WorkingDirectory=\"%~dp0\";$s.Save()"

if exist "%SHORTCUT_PATH%" (
    echo [SUCCESS] Shortcut created successfully.
    echo The macro will now start automatically when you restart.
) else (
    echo [ERROR] Failed to create shortcut.
)
echo.
pause
