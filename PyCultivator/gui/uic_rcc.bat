@echo off
for %%f in (*.ui) do (
    C:/Python36/python.exe -m PyQt5.uic.pyuic -x %%f -o ui_%%~nf.py
)
:: python -m PyQt5.pyrcc_main -o ..\..\resources\resources_rc.py ..\..\resources\resources.qrc