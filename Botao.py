# Botao.py

import tkinter as tk

class Botao(tk.Button):
    def __init__(self, master, cor, largura=100, altura=50, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.cor = cor
        self.largura = largura
        self.altura = altura
        self.configure(width=self.largura, height=self.altura)


"""

Classe: 

"Botao"

Atributos:

"cor, largura e altura"


"""