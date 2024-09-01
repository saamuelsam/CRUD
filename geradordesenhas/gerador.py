import tkinter as tk
from tkinter import messagebox
import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha

def mostrar_senha():
    try:
        comprimento = int(entry_comprimento.get())
        if comprimento <= 0:
            raise ValueError("O comprimento deve ser um número positivo.")
        senha = gerar_senha(comprimento)
        label_senha.config(text=senha)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def copiar_senha():
    senha = label_senha.cget("text")
    if senha:
      root.clipboard_clear()
      root.clipboard_append(senha)
      root.update()
      messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência.")
    else:
      messagebox.showwarning("Aviso", "Nenhuma senha para copiar.")


# Configurar a janela principal
root = tk.Tk()
root.title("Gerador de Senhas")

# Criar e posicionar widgets
tk.Label(root, text="Comprimento da senha:").pack(pady=20)

entry_comprimento = tk.Entry(root)
entry_comprimento.pack(pady=5)

btn_gerar = tk.Button(root, text="Gerar Senha", command=mostrar_senha)
btn_gerar.pack(pady=10)

label_senha = tk.Label(root, text="", font=("Helvetica", 12))
label_senha.pack(pady=5)

btn_copiar = tk.Button(root, text="Copiar Senha", command=copiar_senha)
btn_copiar.pack(pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()