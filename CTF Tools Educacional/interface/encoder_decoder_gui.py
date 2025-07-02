import sys
import os
import tkinter as tk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.encoder_decoder.encoder_decoder import (
    encode_base64, decode_base64, encode_url, decode_url
)

def abrir_encoder_decoder():
    janela = tk.Toplevel()
    janela.title("Encoder/Decoder")
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

    entrada_texto = tk.StringVar()
    saida = tk.StringVar()
    metodo_var = tk.StringVar(value="Base64")

    def codificar():
        texto = entrada_texto.get()
        metodo = metodo_var.get()
        try:
            if metodo == "Base64":
                resultado = encode_base64(texto)
            elif metodo == "URL":
                resultado = encode_url(texto)
            else:
                resultado = "Método inválido"
            saida.set(resultado)
        except Exception as e:
            saida.set(f"Erro: {str(e)}")

    def decodificar():
        texto = entrada_texto.get()
        metodo = metodo_var.get()
        try:
            if metodo == "Base64":
                resultado = decode_base64(texto)
            elif metodo == "URL":
                resultado = decode_url(texto)
            else:
                resultado = "Método inválido"
            saida.set(resultado)
        except Exception as e:
            saida.set(f"Erro: {str(e)}")

    def on_enter(e):
        e.widget['bg'] = cor_hover

    def on_leave(e):
        e.widget['bg'] = cor_fundo

    tk.Label(janela, text="Texto:", font=fonte_padrao, fg=cor_texto, bg=cor_fundo).pack(pady=(10, 2))

    entrada = tk.Entry(janela, textvariable=entrada_texto, font=fonte_padrao,
                       bg="#111111", fg=cor_texto, insertbackground=cor_texto, width=50)
    entrada.pack()

    menu = tk.OptionMenu(janela, metodo_var, "Base64", "URL")
    menu.config(font=fonte_padrao, bg=cor_fundo, fg=cor_texto,
                activebackground=cor_hover, activeforeground=cor_texto)
    menu["menu"].config(bg=cor_fundo, fg=cor_texto)
    menu.pack(pady=5)

    botao_cod = tk.Button(janela, text="Codificar", command=codificar,
                          font=fonte_padrao, bg=cor_fundo, fg=cor_texto,
                          relief="raised", borderwidth=2, activebackground="#111111",
                          activeforeground=cor_texto, cursor="hand2")
    botao_cod.pack(pady=2)
    botao_cod.bind("<Enter>", on_enter)
    botao_cod.bind("<Leave>", on_leave)

    botao_decod = tk.Button(janela, text="Decodificar", command=decodificar,
                            font=fonte_padrao, bg=cor_fundo, fg=cor_texto,
                            relief="raised", borderwidth=2, activebackground="#111111",
                            activeforeground=cor_texto, cursor="hand2")
    botao_decod.pack(pady=2)
    botao_decod.bind("<Enter>", on_enter)
    botao_decod.bind("<Leave>", on_leave)

    tk.Label(janela, textvariable=saida, font=fonte_padrao,
             fg=cor_texto, bg=cor_fundo, wraplength=380, justify="center").pack(pady=10)
