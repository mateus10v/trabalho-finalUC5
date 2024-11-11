import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional

# Definição das classes de dados
@dataclass
class SinaisVitais:
    pressao_arterial: str
    temperatura: float
    frequencia_cardiaca: int
    frequencia_respiratoria: int
    saturacao_oxigenio: int
    glicemia: Optional[float] = None

@dataclass
class NotasEnfermagem:
    queixas: str
    observacoes: str
    procedimentos: List[str]
    complicacoes: List[str]

@dataclass
class PlanoCuidados:
    objetivos: List[str]
    intervencoes: List[str]
    avaliacao: str

class ObservacaoPaciente:
    def __init__(self, id_paciente: str):
        self.id_paciente = id_paciente
        self.data_registro = datetime.now()
        self.sinais_vitais: Optional[SinaisVitais] = None
        self.notas_enfermagem: Optional[NotasEnfermagem] = None
        
    def registrar_sinais_vitais(self, sinais: SinaisVitais):
        self.sinais_vitais = sinais
        
    def adicionar_nota(self, notas: NotasEnfermagem):
        self.notas_enfermagem = notas

class AplicativoEnfermagem(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Sistema de Registro de Enfermagem")
        self.geometry("800x600")
        
        # Criar abas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)
        
        # Aba de Sinais Vitais
        self.aba_sinais = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_sinais, text="Sinais Vitais")
        self.criar_formulario_sinais()
        
        # Aba de Notas
        self.aba_notas = ttk.Frame(self.notebook)
        self.notebook.add(self.aba_notas, text="Notas de Enfermagem")
        self.criar_formulario_notas()
        
        # Inicializar observação
        self.observacao = ObservacaoPaciente("12345")
        
    def criar_formulario_sinais(self):
        # Pressão Arterial
        ttk.Label(self.aba_sinais, text="Pressão Arterial:").grid(row=0, column=0, padx=5, pady=5)
        self.pressao = ttk.Entry(self.aba_sinais)
        self.pressao.grid(row=0, column=1, padx=5, pady=5)
        
        # Temperatura
        ttk.Label(self.aba_sinais, text="Temperatura:").grid(row=1, column=0, padx=5, pady=5)
        self.temperatura = ttk.Entry(self.aba_sinais)
        self.temperatura.grid(row=1, column=1, padx=5, pady=5)
        
        # Frequência Cardíaca
        ttk.Label(self.aba_sinais, text="Freq. Cardíaca:").grid(row=2, column=0, padx=5, pady=5)
        self.freq_cardiaca = ttk.Entry(self.aba_sinais)
        self.freq_cardiaca.grid(row=2, column=1, padx=5, pady=5)
        
        # Frequência Respiratória
        ttk.Label(self.aba_sinais, text="Freq. Respiratória:").grid(row=3, column=0, padx=5, pady=5)
        self.freq_respiratoria = ttk.Entry(self.aba_sinais)
        self.freq_respiratoria.grid(row=3, column=1, padx=5, pady=5)
        
        # Saturação de Oxigênio
        ttk.Label(self.aba_sinais, text="Saturação O2:").grid(row=4, column=0, padx=5, pady=5)
        self.saturacao = ttk.Entry(self.aba_sinais)
        self.saturacao.grid(row=4, column=1, padx=5, pady=5)
        
        # Botão Salvar
        ttk.Button(self.aba_sinais, text="Salvar Sinais Vitais", 
                  command=self.salvar_sinais).grid(row=5, column=0, columnspan=2, pady=20)
        ttk.Button(self.aba_sinais, text="Voltar",
                   command=self.voltar).grid(row=6, column=0, columnspan=2, pady=20)
        
    def voltar(self):
            resposta = messagebox.askesno("confirmar")
            if resposta :
                self.destroy()
        
    def criar_formulario_notas(self):
        # Queixas
        ttk.Label(self.aba_notas, text="Queixas:").grid(row=0, column=0, padx=5, pady=5)
        self.queixas = tk.Text(self.aba_notas, height=3, width=40)
        self.queixas.grid(row=0, column=1, padx=5, pady=5)
        
        # Observações
        ttk.Label(self.aba_notas, text="Observações:").grid(row=1, column=0, padx=5, pady=5)
        self.observacoes = tk.Text(self.aba_notas, height=3, width=40)
        self.observacoes.grid(row=1, column=1, padx=5, pady=5)
        
        # Botão Salvar
        ttk.Button(self.aba_notas, text="Salvar Notas", 
                  command=self.salvar_notas).grid(row=2, column=0, columnspan=2, pady=20)
    
    def salvar_sinais(self):
        try:
            sinais = SinaisVitais(
                pressao_arterial=self.pressao.get(),
                temperatura=float(self.temperatura.get()),
                frequencia_cardiaca=int(self.freq_cardiaca.get()),
                frequencia_respiratoria=int(self.freq_respiratoria.get()),
                saturacao_oxigenio=int(self.saturacao.get())
            )
            self.observacao.registrar_sinais_vitais(sinais)
            messagebox.showinfo("Sucesso", "Sinais vitais registrados!")
        except ValueError as e:
            messagebox.showerror("Erro", "Por favor, verifique os valores digitados")
    
    def salvar_notas(self):
        notas = NotasEnfermagem(
            queixas=self.queixas.get("1.0", tk.END).strip(),
            observacoes=self.observacoes.get("1.0", tk.END).strip(),
            procedimentos=[],
            complicacoes=[]
        )
        self.observacao.adicionar_nota(notas)
        messagebox.showinfo("Sucesso", "Notas registradas!")

if __name__ == "__main__":
    app = AplicativoEnfermagem()
    app.mainloop() 
