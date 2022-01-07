
pyinstaller gopy.py  --onefile 
del /q E:\Gopro-Connect-Chapter\gopy.exe 
move E:\Gopro-Connect-Chapter\dist\gopy.exe E:\Gopro-Connect-Chapter\gopy.exe
rmdir /q /s E:\Gopro-Connect-Chapter\dist
rmdir /q /s E:\Gopro-Connect-Chapter\build
rmdir /q /s E:\Gopro-Connect-Chapter\__pycache__
pause

