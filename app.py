import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def mostrar_mensagem():
    messagebox.showinfo("💖", "Feliz Dia dos Namorados!\nVocê é muito especial pra mim ❤️")

# janela
janela = tk.Tk()
janela.title("Surpresa 💌")
janela.geometry("350x520")
janela.configure(bg="#ffe6f0")

# carregar imagem com tratamento de erro
try:
    img = Image.open("foto.png")
    img = img.rotate(90, expand=True)  # gira a imagem (ajuste se precisar)
    img = img.resize((250, 350))
    foto = ImageTk.PhotoImage(img)

    label_img = tk.Label(janela, image=foto, bg="#ffe6f0")
    label_img.pack(pady=10)

except Exception as e:
    label_erro = tk.Label(janela, text="Erro ao carregar imagem 😢", bg="#ffe6f0")
    label_erro.pack()

# texto
label = tk.Label(
    janela,
    text="Clique para sua surpresa 💖",
    bg="#ffe6f0",
    font=("Arial", 12)
)
label.pack(pady=10)

# botão
botao = tk.Button(
    janela,
    text="Abrir ❤️",
    command=mostrar_mensagem,
    bg="#ff66b2",
    fg="white"
)
botao.pack(pady=10)

janela.mainloop()
