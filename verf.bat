@echo off
tasklist | find /i "Torch.Server.exe"
If errorlevel 1 start C:\Serverino\Torch.Server.exe
If errorlevel 1 echo "Server est� off iniciando"
if errorlevel 0 echo "O server est� rodando"