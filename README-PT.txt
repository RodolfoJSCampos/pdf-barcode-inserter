---------------- O PROGRAMA ----------------
Este programa tem como objetivo ler um PDF gerado pelo sistema
de vendas da JDSystem, extrair o número do pedido, gerar um
código de barras com esse número e inserir esse código no PDF
antes de enviá-lo para impressão.


-------------- FUNCIONALIDADES --------------
📥 Lê o conteúdo de uma nota pdf (gerado via WSGE - Vendas)

🔎 Extrai automaticamente o número do pedido a partir do texto Pedido Nº: xxxxxxx

🧱 Gera um código de barras Code128

🖨️ Insere o código de barras no PDF, logo abaixo da linha Data: dd/mm/aaaa

💾 Salva o PDF modificado

🖨️ Envia o PDF final para uma impressora de rede específica, definida no código


----------------- INSTALAÇÃO -----------------
Instalações necessárias para rodar o programa:

1. Python:
https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe

2. Pip:
python get-pip.py

3. Dependencias:
pip install pdfplumber PyPDF2 reportlab pywin32

4. PDFCreator:
https://www.pdfforge.org/pdfcreator/download

5. Leitor padrão de PDF:
https://www.sumatrapdfreader.org/download-free-pdf-viewer


----------------- CONFIGURAÇÃO -----------------
Configurações necessárias para rodar o programa:

1. Criar pastas:
C:\PDFCreator
C:\Projetos

2. Inserir todos os arquivos dessa pasta no diretório C:\Projetos

3. Configurando o PDFCreator:
Criar perfil com os seguinte parâmetros,
Program File:
C:\PDFCreator\executar_script.bat
Additional Program Parameters:
<OutputFilePath>
Marque ✅ Esperar fim.

4. Selecionar a nova impressora virtual como impressora primária no PDFCreator.

5. Editar impressora no código Python:
Use o arquivo listar_impressoras.py para localizar a impressora alvo.
Altere o caminho ou nome da impressora na linha 67 do arquivo inserir_codigo.py

6. Defina o Sumatra como leitor de PDF padrão do sistema.


----------------- COMO USAR -----------------
Selecione a impressora virtual criada quando for imprimir a nota.

O PDFCreator chama o arquivo .bat, que por sua vez executa o .py
gerado a partir de linha de comando (cmd).

O script:

Processa o PDF de entrada

Gera e insere o código de barras

Salva o PDF final

Envia o PDF final para a impressora real


------------ OBSERVAÇÕES FINAIS ------------
📌 Esse README foi criado para o SO Windows 10 (64 bits).

📌 O script procura por Pedido Nº: xxxxxxx dentro do PDF.

📌 O PDF final sobrescreve sempre o arquivo C:\Projetos\saida_com_codigo.pdf

📌 A impressão ocorre de forma automática, sem abrir o Adobe Reader
(se for usado o SumatraPDF ou uma impressora com driver silencioso)
