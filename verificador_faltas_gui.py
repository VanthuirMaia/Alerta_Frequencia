import os
import fitz  # PyMuPDF
import re
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class VerificadorFaltasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Verificador de Faltas - PDF")
        self.root.geometry("600x400")
        
        # Variável para guardar o caminho do PDF selecionado
        self.pdf_path = None
        
        # Botão para selecionar PDF
        self.btn_selecionar = tk.Button(root, text="Selecionar PDF", command=self.selecionar_pdf)
        self.btn_selecionar.pack(pady=10)
        
        # Label para mostrar qual arquivo foi selecionado
        self.lbl_arquivo = tk.Label(root, text="Nenhum arquivo selecionado")
        self.lbl_arquivo.pack()
        
        # Botão para verificar faltas
        self.btn_verificar = tk.Button(root, text="Verificar", command=self.verificar_faltas, state=tk.DISABLED)
        self.btn_verificar.pack(pady=10)
        
        # Área de texto para mostrar resultados
        self.txt_resultado = scrolledtext.ScrolledText(root, width=70, height=15)
        self.txt_resultado.pack(pady=10)

        # Rodapé com sua marca
        self.lbl_marca = tk.Label(
            root,
            text="Vanthuir Maia | Tel: (87) 99607-5897 | Email: vanmaiasf@gmail.com",
            font=("Arial", 9),
            fg="gray"
        )
        self.lbl_marca.pack(side=tk.BOTTOM, pady=5)
    
    def selecionar_pdf(self):
        caminho = filedialog.askopenfilename(
            title="Selecione o arquivo PDF",
            filetypes=[("Arquivos PDF", "*.pdf")],
        )
        if caminho:
            self.pdf_path = caminho
            self.lbl_arquivo.config(text=os.path.basename(caminho))
            self.btn_verificar.config(state=tk.NORMAL)
            self.txt_resultado.delete("1.0", tk.END)
    
    def verificar_faltas(self):
        if not self.pdf_path:
            messagebox.showwarning("Atenção", "Selecione um arquivo PDF primeiro!")
            return
        
        try:
            with fitz.open(self.pdf_path) as doc:
                texto = ""
                for pagina in doc:
                    texto += pagina.get_text()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível abrir o PDF:\n{e}")
            return
        
        # Regex igual ao seu script original
        padrao = re.compile(
            r'\d+\s+\d{4}\.\d+\.\d+\s+([A-ZÁÂÉÍÓÚÇÑ ]+)\s+Em Processo\s+\d+\s+\d+\s+(\d+)'
        )
        
        alertas_critico = []
        alertas_atencao = []
        
        for match in padrao.finditer(texto):
            nome = match.group(1).strip()
            falta_percentual = int(match.group(2))
            if falta_percentual > 25:
                alertas_critico.append((nome, falta_percentual))
            elif 20 <= falta_percentual <= 25:
                alertas_atencao.append((nome, falta_percentual))
        
        # Exibe resultado no campo de texto
        self.txt_resultado.delete("1.0", tk.END)
        
        self.txt_resultado.insert(tk.END, "🔴 ALERTA CRÍTICO (faltas acima de 25%):\n")
        if alertas_critico:
            for nome, perc in alertas_critico:
                self.txt_resultado.insert(tk.END, f"❌ {nome} está com {perc}% de faltas!\n")
        else:
            self.txt_resultado.insert(tk.END, "✅ Nenhum aluno acima de 25% de faltas.\n")
        
        self.txt_resultado.insert(tk.END, "\n🟠 ALERTA DE ATENÇÃO (entre 20% e 25%):\n")
        if alertas_atencao:
            for nome, perc in alertas_atencao:
                self.txt_resultado.insert(tk.END, f"⚠️  {nome} está com {perc}% de faltas.\n")
        else:
            self.txt_resultado.insert(tk.END, "✅ Nenhum aluno entre 20% e 25% de faltas.\n")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = VerificadorFaltasApp(root)
    root.mainloop()
