cd C:\Windows\system32
sc config "Dnscache" start= disabled
sc stop "Dnscache"
if EXIST "C:\Python27\python.exe" (C:\AdBlock\start.bat && EXIT) else (msiexec /i C:\AdBlock\python.msi)
cd C:\AdBlock
start.bat
EXIT