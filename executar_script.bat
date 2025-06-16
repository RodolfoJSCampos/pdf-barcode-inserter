@echo off
echo Arquivo recebido: %1
cd /d C:\PDFCreator\pdf-barcode-inserter\
C:\Users\W10\AppData\Local\Programs\Python\Python313\python.exe inserir_codigo.py "%1"
