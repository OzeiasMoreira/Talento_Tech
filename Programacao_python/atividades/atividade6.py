from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk, messagebox

class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    @abstractmethod
    def mostrar(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.porte = porte

    def getPorte(self):
        return self.porte

    def setPorte(self, porte):
        self.porte = porte

    def mostrar(self):
        return f"Cachorro - Nome: {self.nome}, Idade: {self.idade} anos, Porte: {self.porte}"


class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def getRaca(self):
        return self.raca

    def setRaca(self, raca):
        self.raca = raca

    def mostrar(self):
        return f"Gato - Nome: {self.nome}, Idade: {self.idade} anos, Raça: {self.raca}"


animais = []

def adicionar_animal():
    nome = entry_nome.get()
    idade = entry_idade.get()

    if not nome or not idade:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    tipo = combobox_tipo.get()
    detalhe = entry_detalhe.get()

    if tipo == "Cachorro":
        novo_animal = Cachorro(nome, idade, detalhe)
    elif tipo == "Gato":
        novo_animal = Gato(nome, idade, detalhe)
    else:
        messagebox.showerror("Erro", "Selecione um tipo válido.")
        return

    animais.append(novo_animal)
    messagebox.showinfo("Sucesso", f"{tipo} cadastrado com sucesso!")
    atualizar_lista()
    limpar_campos()


def atualizar_lista():
    lista_animais.delete(0, tk.END)
    for animal in animais:
        lista_animais.insert(tk.END, animal.mostrar())


def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_detalhe.delete(0, tk.END)
    combobox_tipo.set("")


root = tk.Tk()
root.title("Sistema de Cadastro de Animais")

notebook = ttk.Notebook(root)

tab_cadastro = ttk.Frame(notebook)
notebook.add(tab_cadastro, text="Cadastro")

tab_lista = ttk.Frame(notebook)
notebook.add(tab_lista, text="Lista de Animais")

notebook.pack(expand=1, fill="both")

frame_cadastro = ttk.LabelFrame(tab_cadastro, text="Cadastro de Animal")
frame_cadastro.pack(padx=10, pady=10, fill="both", expand=True)

ttk.Label(frame_cadastro, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entry_nome = ttk.Entry(frame_cadastro)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_cadastro, text="Idade:").grid(row=1, column=0, padx=5, pady=5)
entry_idade = ttk.Entry(frame_cadastro)
entry_idade.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_cadastro, text="Tipo:").grid(row=2, column=0, padx=5, pady=5)
combobox_tipo = ttk.Combobox(frame_cadastro, values=["Cachorro", "Gato"])
combobox_tipo.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_cadastro, text="Porte/Raça:").grid(row=3, column=0, padx=5, pady=5)
entry_detalhe = ttk.Entry(frame_cadastro)
entry_detalhe.grid(row=3, column=1, padx=5, pady=5)

botao_adicionar = ttk.Button(frame_cadastro, text="Adicionar", command=adicionar_animal)
botao_adicionar.grid(row=4, column=0, columnspan=2, pady=10)

frame_lista = ttk.LabelFrame(tab_lista, text="Lista de Animais")
frame_lista.pack(padx=10, pady=10, fill="both", expand=True)

lista_animais = tk.Listbox(frame_lista, height=15)
lista_animais.pack(padx=5, pady=5, fill="both", expand=True)

root.mainloop()
