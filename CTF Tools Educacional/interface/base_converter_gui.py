import sys
import os
import tkinter as tk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.base_converter.base_converter import (
    bin_to_dec, dec_to_bin, hex_to_dec, dec_to_hex, ascii_to_bin
)

def abrir_base_converter():
    janela = tk.Toplevel()
    janela.title("Conversor de Bases")
    janela.configure(bg="#222222")

    largura, altura = 400, 250
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

    entrada_valor = tk.StringVar()
    saida = tk.StringVar()
    metodo_var = tk.StringVar(value="Texto → Binário")

    def converter():
        entrada = entrada_valor.get()
        metodo = metodo_var.get()
        try:
            if metodo == "Binário → Decimal":
                resultado = bin_to_dec(entrada)
            elif metodo == "Decimal → Binário":
                resultado = dec_to_bin(int(entrada))
            elif metodo == "Decimal → Hexadecimal":
                resultado = dec_to_hex(int(entrada))
            elif metodo == "Hexadecimal → Decimal":
                resultado = hex_to_dec(entrada)
            elif metodo == "Texto → Binário":
                resultado = ascii_to_bin(entrada)
            else:
                resultado = "Método inválido"
            saida.set(str(resultado))
        except Exception as e:
            saida.set(f"Erro: {str(e)}")

    def on_enter(e):
        e.widget['bg'] = cor_hover

    def on_leave(e):
        e.widget['bg'] = cor_fundo

    tk.Label(janela, text="Entrada:", font=fonte_padrao, fg=cor_texto, bg=cor_fundo).pack(pady=(10, 2))

    entrada = tk.Entry(janela, textvariable=entrada_valor, font=fonte_padrao,
                       bg="#111111", fg=cor_texto, insertbackground=cor_texto, width=50)
    entrada.pack()

    opcoes = [
        "Binário → Decimal",
        "Decimal → Binário",
        "Decimal → Hexadecimal",
        "Hexadecimal → Decimal",
        "Texto → Binário"
    ]

    menu = tk.OptionMenu(janela, metodo_var, *opcoes)
    menu.config(font=fonte_padrao, bg=cor_fundo, fg=cor_texto, activebackground=cor_hover, activeforeground=cor_texto)
    menu["menu"].config(bg=cor_fundo, fg=cor_texto)
    menu.pack(pady=5)

    botao = tk.Button(janela, text="Converter", command=converter,
                      font=fonte_padrao, bg=cor_fundo, fg=cor_texto,
                      relief="raised", borderwidth=2, activebackground="#111111", activeforeground=cor_texto, cursor="hand2")
    botao.pack(pady=5)
    botao.bind("<Enter>", on_enter)
    botao.bind("<Leave>", on_leave)

    tk.Label(janela, textvariable=saida, font=fonte_padrao, fg=cor_texto, bg=cor_fundo, wraplength=380, justify="center").pack(pady=10)
