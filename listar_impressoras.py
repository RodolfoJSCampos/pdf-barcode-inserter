import win32print

impressoras = win32print.EnumPrinters(2)
for impressora in impressoras:
    print(impressora[2])  # Nome da impressora

# Listar impressoras na rede Windows via prompt de comando:
# wmic printer get name