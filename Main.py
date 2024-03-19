# Main.py

import tkinter as tk
from tkinter import messagebox
from Botao import Botao
from WallpaperChanger import WallpaperChanger

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Alterar Plano de Fundo")
        self.geometry("800x300")

        self.configure(background="#4B0082")

        self.botao_vermelho = Botao(self, "Vermelho", largura=30, altura=3)
        self.botao_vermelho.config(text="Vermelho", command=self.change_to_red, bg="red")
        self.botao_vermelho.pack(pady=5)

        self.botao_azul = Botao(self, "Azul", largura=30, altura=3)
        self.botao_azul.config(text="Azul", command=self.change_to_blue, bg="blue")
        self.botao_azul.pack(pady=5)

        self.botao_verde = Botao(self, "Verde", largura=30, altura=3)
        self.botao_verde.config(text="Verde", command=self.change_to_green, bg="green")
        self.botao_verde.pack(pady=5)

    def change_to_red(self):
        wallpaper_changer = WallpaperChanger()
        wallpaper_changer.change_wallpaper("C:\\ChangeWallpaper\\wallpapers\\vermelho.png")
        messagebox.showinfo("Mudança de Fundo", "Plano de fundo alterado para vermelho.")

    def change_to_blue(self):
        wallpaper_changer = WallpaperChanger()
        wallpaper_changer.change_wallpaper("C:\\ChangeWallpaper\\wallpapers\\azul.jpg")
        messagebox.showinfo("Mudança de Fundo", "Plano de fundo alterado para azul.")

    def change_to_green(self):
        wallpaper_changer = WallpaperChanger()
        wallpaper_changer.change_wallpaper("C:\\ChangeWallpaper\\wallpapers\\verde.jpg")
        messagebox.showinfo("Mudança de Fundo", "Plano de fundo alterado para verde.")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
