import sys
import re
import io
import pdfplumber
import win32print
import win32api
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from reportlab.lib.pagesizes import A4

# --- 1. Receber PDF original como argumento ---
if len(sys.argv) < 2:
    print("Erro: caminho do PDF não fornecido.")
    sys.exit(1)

entrada_pdf = sys.argv[1]
saida_pdf = "C:\\Projetos\\saida_com_codigo.pdf"

print(f"Processando arquivo: {entrada_pdf}")

# --- 2. Extrair número do pedido ---
with pdfplumber.open(entrada_pdf) as pdf:
    texto_total = "\n".join(page.extract_text() or '' for page in pdf.pages)

match = re.search(r"(?i)pedido\s*(n[º°]|\bnro\b|number)\s*:\s*(\d+)", texto_total)
pedido_num = match.group(2) if match else "0000000"
print(f"Número do pedido encontrado: {pedido_num}")

# --- 3. Abrir PDF original ---
reader = PdfReader(entrada_pdf)
writer = PdfWriter()
page_width, page_height = A4

# --- 4. Adicionar código de barras em cada página ---
for pagina in reader.pages:
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    # Gerar código de barras com largura maior e altura menor
    barcode = code128.Code128(pedido_num, barHeight=15, barWidth=1.2)

    # Centralizar horizontalmente
    x = 420

    # Posicionar logo abaixo de "Data: dd/mm/aaaa"
    y = 765  # ponto Y no PDF (mais alto que o rodapé padrão)

    barcode.drawOn(c, x, y)
    c.save()

    buffer.seek(0)
    camada_codigo = PdfReader(buffer).pages[0]

    pagina.merge_page(camada_codigo)
    writer.add_page(pagina)

# --- 5. Salvar novo PDF ---
with open(saida_pdf, "wb") as f:
    writer.write(f)

print(f"Arquivo salvo em: {saida_pdf}")

saida_pdf = r"C:\Projetos\saida_com_codigo.pdf"

# Nome da impressora de rede
impressora = r"\\ESCRITORIO-PC\HP LaserJet Professional M1132 MFP"

try:
    # Define a impressora temporariamente como padrão
    win32print.SetDefaultPrinter(impressora)
    # Envia o PDF para a impressora
    win32api.ShellExecute(0, "print", saida_pdf, None, ".", 0)
    print(f"PDF enviado para a impressora: {impressora}")
except Exception as e:
    print(f"Erro ao imprimir: {e}")
