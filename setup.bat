@echo off
setlocal

set "SCRIPT_DIR=%~dp0"

if not exist "%USERPROFILE%\scripts" mkdir "%USERPROFILE%\scripts"
copy "%SCRIPT_DIR%pytree.py" "%USERPROFILE%\scripts\pytree.py"

echo %PATH% | findstr /i "%USERPROFILE%\scripts" >nul
if %errorlevel% neq 0 setx PATH "%USERPROFILE%\scripts;%PATH%"

echo @echo off > "%USERPROFILE%\scripts\pytree.bat"
echo python "%USERPROFILE%\scripts\pytree.py" %%* >> "%USERPROFILE%\scripts\pytree.bat"

echo PATH updated. Please restart your terminal or run 'refreshenv'.
echo Setup complete! Run 'pytree' from anywhere.

endlocal
pause
