import tkinter as tk
from encoder_decoder_gui import abrir_encoder_decoder
from xor_tool_gui import abrir_xor_tool
from base_converter_gui import abrir_base_converter

janela = tk.Tk()
janela.title("CTF Tools Educacional Pro")

largura = 400
altura = 300
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura // 2)
pos_y = (altura_tela // 2) - (altura // 2)
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
janela.configure(bg="#222222")  # Fundo escuro

# === Ícone personalizado ===
icone = tk.PhotoImage(file="C:/Users/Max/Documents/CTF Tools Educacional/MM.png")  # Atualize o caminho se necessário
janela.iconphoto(False, icone)

fonte_titulo = ("Consolas", 14, "bold")
fonte_rodape = ("Consolas", 8)
cor_fundo = "#222222"
cor_texto = "#00FFFF"
cor_hover = "#333333"

def on_enter(e):
    e.widget['bg'] = cor_hover

def on_leave(e):
    e.widget['bg'] = cor_fundo

tk.Label(janela, text="Selecione uma Ferramenta", font=fonte_titulo,
         fg=cor_texto, bg=cor_fundo).pack(pady=20)

botoes_info = [
    ("Encoder/Decoder", abrir_encoder_decoder),
    ("XOR Tool", abrir_xor_tool),
    ("Base Converter", abrir_base_converter),
]

for texto, comando in botoes_info:
    botao = tk.Button(
        janela, text=texto, command=comando,
        font=("Consolas", 11),
        bg=cor_fundo, fg=cor_texto, relief="raised", borderwidth=2,
        activebackground="#111111", activeforeground=cor_texto,
        cursor="hand2"
    )
    botao.pack(pady=5, ipadx=10, ipady=2)
    botao.bind("<Enter>", on_enter)
    botao.bind("<Leave>", on_leave)

tk.Label(janela, text="Versão 1.0 • Desenvolvido por Prof. Max Muller", font=fonte_rodape,
         fg="#555555", bg=cor_fundo).pack(side="bottom", pady=5)

janela.mainloop()
