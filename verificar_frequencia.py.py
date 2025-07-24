import os
import glob
import fitz  # PyMuPDF
import re

# Caminho da pasta onde estão os PDFs
caminho_pasta = "pdf"

# Lista todos os arquivos PDF da pasta
arquivos_pdf = glob.glob(os.path.join(caminho_pasta, "*.pdf"))

# Verifica se há pelo menos um PDF na pasta
if not arquivos_pdf:
    raise FileNotFoundError("❌ Nenhum arquivo PDF encontrado na pasta 'pdf'.")

# Pega o PDF mais recente (última modificação)
pdf_mais_recente = max(arquivos_pdf, key=os.path.getmtime)
print(f"📄 Lendo o arquivo: {pdf_mais_recente}")

# Abre o PDF e extrai o texto
with fitz.open(pdf_mais_recente) as doc:
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()

# Expressão regular para capturar Nome e % de Faltas
padrao = re.compile(
    r'\d+\s+\d{4}\.\d+\.\d+\s+([A-ZÁÂÉÍÓÚÇÑ ]+)\s+Em Processo\s+\d+\s+\d+\s+(\d+)'
)

print("\n📢 Alunos com mais de 25% de faltas:")
encontrou_alertas = False

# Verifica alunos acima do limite
for match in padrao.finditer(texto):
    nome = match.group(1).strip()
    falta_percentual = int(match.group(2))
    if falta_percentual > 25:
        print(f"⚠️  {nome} está com {falta_percentual}% de faltas!")
        encontrou_alertas = True

if not encontrou_alertas:
    print("✅ Nenhum aluno com mais de 25% de faltas.")
