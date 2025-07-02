import sys
import os
import tkinter as tk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.xor_tool.xor_tool import xor

def abrir_xor_tool():
    janela = tk.Toplevel()
    janela.title("XOR Tool")
    janela.configure(bg="#222222")

    largura, altura = 400, 280
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

    fonte_padrao = ("Consolas", 11)
    cor_fundo = "#222222"
    cor_texto = "#00FFFF"
    cor_hover = "#333333"
    cor_erro = "#FF5555"

    entrada_texto = tk.StringVar()
    entrada_chave = tk.StringVar()
    saida = tk.StringVar()

    def aplicar_xor():
        texto = entrada_texto.get()
        chave = entrada_chave.get()
        try:
            if not chave:
                saida.set("Erro: A chave não pode estar vazia.")
                return
            resultado = xor(texto, chave)
            saida.set(resultado)
        except Exception as e:
            saida.set(f"Erro: {str(e)}")

    def on_enter(e):
        e.widget['bg'] = cor_hover

    def on_leave(e):
        e.widget['bg'] = cor_fundo

    # Layout
    tk.Label(janela, text="Texto:", font=fonte_padrao, fg=cor_texto, bg=cor_fundo).pack(pady=(10, 2))
    tk.Entry(janela, textvariable=entrada_texto, font=fonte_padrao,
             bg="#111111", fg=cor_texto, insertbackground=cor_texto, width=50).pack()

    tk.Label(janela, text="Chave:", font=fonte_padrao, fg=cor_texto, bg=cor_fundo).pack(pady=(10, 2))
    tk.Entry(janela, textvariable=entrada_chave, font=fonte_padrao,
             bg="#111111", fg=cor_texto, insertbackground=cor_texto, width=50).pack()

    botao = tk.Button(janela, text="Aplicar XOR", command=aplicar_xor,
                      font=fonte_padrao, bg=cor_fundo, fg=cor_texto,
                      relief="raised", borderwidth=2, activebackground="#111111",
                      activeforeground=cor_texto, cursor="hand2")
    botao.pack(pady=10)
    botao.bind("<Enter>", on_enter)
    botao.bind("<Leave>", on_leave)

    tk.Label(janela, textvariable=saida, font=fonte_padrao,
             fg=cor_texto, bg=cor_fundo, wraplength=380, justify="center").pack(pady=10)
