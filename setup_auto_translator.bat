@echo off
REM Auto Gemini Translator Setup and Test Script
echo ========================================
echo Auto Gemini Translator Setup
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found! Please install Python first.
    pause
    exit /b 1
)

echo ✓ Python found
echo.

REM Install dependencies
echo Installing dependencies...
pip install requests
if errorlevel 1 (
    echo ⚠ Warning: Could not install requests. You may need to install it manually.
) else (
    echo ✓ Dependencies installed successfully
)
echo.

REM Check if Vietnamese prompt files exist
if not exist "vietnamese_prompt_batch_001.txt" (
    echo ❌ Vietnamese prompt files not found!
    echo Running create_vietnamese_prompts.py first...
    python create_vietnamese_prompts.py
    echo.
)

echo ✓ Vietnamese prompt files ready
echo.

REM Prompt for API key
echo Please enter your Gemini API key:
echo (Get it from: https://aistudio.google.com/app/apikey)
set /p API_KEY="API Key: "

if "%API_KEY%"=="" (
    echo ❌ No API key provided!
    pause
    exit /b 1
)

echo.
echo ========================================
echo Running Test Translation (3 batches)
echo ========================================
echo.

REM Run test
python auto_gemini_translator.py --api-key %API_KEY% --test

echo.
echo ========================================
echo Test completed!
echo ========================================
echo.

echo To translate all 117 batches, run:
echo python auto_gemini_translator.py --api-key %API_KEY%
echo.

pause