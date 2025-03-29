
import tkinter as tk
from tkinter import messagebox

def cadastrar_usuario():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    email = entry_email.get()
    
    if nome and cpf and email:
        messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

root = tk.Tk()
root.title("Cadastro de Usuário")
root.geometry("400x300")  
root.resizable(False, False) 

window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_left = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

label_nome = tk.Label(root, text="Nome:")
label_nome.pack(pady=5)
entry_nome = tk.Entry(root, width=40)  
entry_nome.pack(pady=5)

label_cpf = tk.Label(root, text="CPF:")
label_cpf.pack(pady=5)
entry_cpf = tk.Entry(root, width=40)  
entry_cpf.pack(pady=5)

label_email = tk.Label(root, text="Email:")
label_email.pack(pady=5)
entry_email = tk.Entry(root, width=40)  
entry_email.pack(pady=5)

botao_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_usuario)
botao_cadastrar.pack(pady=20)

root.mainloop()
