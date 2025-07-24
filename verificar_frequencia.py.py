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

# Flags de controle
tem_alerta_critico = False
tem_alerta_atencao = False

# Listas para exibir depois
alertas_critico = []
alertas_atencao = []

# Verifica os alunos
for match in padrao.finditer(texto):
    nome = match.group(1).strip()
    falta_percentual = int(match.group(2))

    if falta_percentual > 25:
        alertas_critico.append((nome, falta_percentual))
        tem_alerta_critico = True
    elif 20 <= falta_percentual <= 25:
        alertas_atencao.append((nome, falta_percentual))
        tem_alerta_atencao = True

# Exibição final
print("\n🔴 ALERTA CRÍTICO (faltas acima de 25%):")
if tem_alerta_critico:
    for nome, perc in alertas_critico:
        print(f"❌ {nome} está com {perc}% de faltas!")
else:
    print("✅ Nenhum aluno acima de 25% de faltas.")

print("\n🟠 ALERTA DE ATENÇÃO (entre 20% e 25%):")
if tem_alerta_atencao:
    for nome, perc in alertas_atencao:
        print(f"⚠️  {nome} está com {perc}% de faltas.")
else:
    print("✅ Nenhum aluno entre 20% e 25% de faltas.")
