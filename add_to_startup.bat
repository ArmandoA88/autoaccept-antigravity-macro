@echo off
cd /d "%~dp0"
set "SCRIPT_PATH=%~dp0run_macro.bat"
set "SHORTCUT_PATH=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\AutoAcceptMacro.lnk"

echo --- Add to Startup ---
echo This will make the macro run automatically when you log in.
echo.
echo Target File: %SCRIPT_PATH%
echo Startup Folder: %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
echo.

powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%SHORTCUT_PATH%');$s.TargetPath='%SCRIPT_PATH%';$s.WorkingDirectory='%~dp0';$s.Save()"

if exist "%SHORTCUT_PATH%" (
    echo [SUCCESS] Shortcut created successfully.
    echo The macro will now start automatically when you restart your computer.
) else (
    echo [ERROR] Failed to create shortcut.
)
echo.
pause
