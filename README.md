# Verificador de Faltas - PDF

Aplicação desktop simples para verificar faltas de alunos a partir de arquivos PDF, com interface gráfica amigável desenvolvida em Python usando Tkinter.

---

## Funcionalidades

- Seleção fácil de arquivos PDF via interface.
- Análise automática dos dados de faltas extraídos do PDF.
- Alertas visuais para alunos com faltas críticas (>25%) e atenção (20% a 25%).
- Exibição clara dos resultados em uma área de texto rolável.
- Inclusão de dados de contato do desenvolvedor na interface para fácil identificação.

---

## Tecnologias utilizadas

- Python 3.x
- PyMuPDF (`fitz`) para leitura e extração de texto de PDFs
- Tkinter para interface gráfica (GUI)

---

## Como usar

### Pré-requisitos

- Python 3 instalado (https://www.python.org/downloads/)
- Biblioteca PyMuPDF instalada:

```bash
pip install pymupdf
```

### Executando o script diretamente

1. Clone ou faça download do projeto.
2. Execute no terminal:

```bash
python verificador_faltas_gui.py
```

3. Na janela que abrir:
   - Clique em **Selecionar PDF** e escolha o arquivo desejado.
   - Clique em **Verificar** para gerar os alertas.

---

## Gerando executável standalone (Windows)

Para facilitar a distribuição, você pode gerar um executável que não exige Python instalado:

1. Instale o PyInstaller:

```bash
pip install pyinstaller
```

2. Gere o executável:

```bash
pyinstaller --onefile --windowed verificador_faltas_gui.py
```

3. O arquivo executável estará na pasta `dist/`.

---

## Personalização

No código, substitua os dados de contato no rodapé da interface para os seus:

```python
text="Seu Nome | Tel: (XX) XXXXX-XXXX | Email: seuemail@exemplo.com"
```

---

## Contato do desenvolvedor

Vanthuir Maia  
Telefone: (87) 99607-5897  
Email: vanmaiasf@gmail.com | vanthuir.dev@gmail.com

---

## Licença

Este projeto está sob a licença MIT — sinta-se à vontade para usar e modificar.

---

## Observações

- A aplicação depende do padrão textual do PDF para extrair os dados corretamente. Caso o formato do PDF seja diferente, a regex pode precisar de ajustes.
- Para suporte ou dúvidas, entre em contato com o desenvolvedor.

---

_Desenvolvido por Vanthuir Maia_
