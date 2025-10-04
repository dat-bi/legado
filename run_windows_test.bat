@echo off
REM Windows-compatible test runner for Gemini models
echo =========================================
echo Testing Gemini Models (Windows Compatible)
echo =========================================
echo.

REM Set UTF-8 encoding for better Unicode support
chcp 65001 >nul 2>&1

REM Check if API key is provided
if "%1"=="" (
    echo Usage: run_windows_test.bat YOUR_API_KEY
    echo.
    echo Example: run_windows_test.bat AIzaSyCKAqER4L2rokAe_VW87Ws6-__0BYkXvYY
    pause
    exit /b 1
)

set API_KEY=%1

echo Testing with API key: %API_KEY:~0,10%...
echo.

REM Run the test
python test_gemini_2_5.py --api-key %API_KEY%

echo.
echo Test completed!
pause