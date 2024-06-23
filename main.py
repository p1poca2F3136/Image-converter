import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Função para alternar entre os modos claro e escuro
def alternar_modo():
    global modo_escuro
    modo_escuro = not modo_escuro
    if modo_escuro:
        root.config(bg='#2d2d2d')
        label_entrada.config(bg='#2d2d2d', fg='white')
        label_saida.config(bg='#2d2d2d', fg='white')
        entry_entrada.config(bg='#383838', fg='white')
        entry_saida.config(bg='#383838', fg='white')
        btn_selecionar_entrada.config(bg='#4d4d4d', fg='white')
        btn_selecionar_saida.config(bg='#4d4d4d', fg='white')
        btn_converter.config(bg='#007acc', fg='white')
    else:
        root.config(bg='white')
        label_entrada.config(bg='white', fg='black')
        label_saida.config(bg='white', fg='black')
        entry_entrada.config(bg='white', fg='black')
        entry_saida.config(bg='white', fg='black')
        btn_selecionar_entrada.config(bg='lightgray', fg='black')
        btn_selecionar_saida.config(bg='lightgray', fg='black')
        btn_converter.config(bg='#4CAF50', fg='white')

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff;*.webp;*.ico;*.eps;*.pdf")])
    entrada_var.set(caminho_arquivo)

def salvar_como():
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".png",
                                                   filetypes=[("PNG files", "*.png"),
                                                              ("JPEG files", "*.jpg;*.jpeg"),
                                                              ("BMP files", "*.bmp"),
                                                              ("GIF files", "*.gif"),
                                                              ("TIFF files", "*.tiff"),
                                                              ("WebP files", "*.webp"),
                                                              ("ICO files", "*.ico"),
                                                              ("EPS files", "*.eps"),
                                                              ("PDF files", "*.pdf")])
    saida_var.set(caminho_arquivo)

def converter_imagem():
    caminho_entrada = entrada_var.get()
    caminho_saida = saida_var.get()

    if not caminho_entrada or not caminho_saida:
        messagebox.showerror("Erro", "Por favor, selecione o arquivo de entrada e o caminho de saída.")
        return

    formato_saida = caminho_saida.split('.')[-1].upper()

    if formato_saida == 'JPG':
        formato_saida = 'JPEG'

    try:
        imagem = Image.open(caminho_entrada)
        if formato_saida in ['JPEG', 'JPG']:
            imagem = imagem.convert("RGB")
        imagem.save(caminho_saida, formato_saida)
        messagebox.showinfo("Sucesso", f"Imagem convertida e salva em {caminho_saida}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configurar a janela principal
root = tk.Tk()
root.title("Conversor de Imagens")

# Variáveis globais
entrada_var = tk.StringVar()
saida_var = tk.StringVar()
modo_escuro = False  # Inicialmente em modo claro

# Criar e posicionar os widgets
label_entrada = tk.Label(root, text="Arquivo de entrada:", bg='white')
label_entrada.grid(row=0, column=0, padx=10, pady=10)
entry_entrada = tk.Entry(root, textvariable=entrada_var, width=50)
entry_entrada.grid(row=0, column=1, padx=10, pady=10)
btn_selecionar_entrada = tk.Button(root, text="Selecionar", command=selecionar_arquivo, bg='lightgray')
btn_selecionar_entrada.grid(row=0, column=2, padx=10, pady=10)

label_saida = tk.Label(root, text="Salvar como:", bg='white')
label_saida.grid(row=1, column=0, padx=10, pady=10)
entry_saida = tk.Entry(root, textvariable=saida_var, width=50)
entry_saida.grid(row=1, column=1, padx=10, pady=10)
btn_selecionar_saida = tk.Button(root, text="Selecionar", command=salvar_como, bg='lightgray')
btn_selecionar_saida.grid(row=1, column=2, padx=10, pady=10)

btn_converter = tk.Button(root, text="Converter", command=converter_imagem, bg='#4CAF50', fg='white')
btn_converter.grid(row=2, column=1, padx=10, pady=20)

# Botão para alternar o modo claro/escuro
btn_modo = tk.Button(root, text="Modo Escuro", command=alternar_modo, bg='#007acc', fg='white')
btn_modo.grid(row=3, column=1, pady=10)

# Executar a aplicação
root.mainloop()