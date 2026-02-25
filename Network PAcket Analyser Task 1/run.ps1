# Simple script to run the Network Packet Analyzer app
# Requires Python 3.13 with Flask and Scapy installed

$PythonPath = "C:\Users\ASUS\AppData\Local\Programs\Python\Python313\python.exe"

if (-not (Test-Path $PythonPath)) {
    Write-Host "Error: Python executable not found at $PythonPath" -ForegroundColor Red
    exit 1
}

Write-Host "Starting Network Packet Analyzer..." -ForegroundColor Green
Write-Host "Server will run on http://127.0.0.1:5000" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop" -ForegroundColor Yellow
Write-Host ""

& $PythonPath app.py
