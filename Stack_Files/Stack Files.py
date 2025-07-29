import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import threading
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    entry_pasta.delete(0, tk.END)
    entry_pasta.insert(0, pasta)
    listar_arquivos(pasta)

def listar_arquivos(pasta):
    listbox.delete(0, tk.END)
    extensao = extensao_entrada_var.get().lstrip(".").lower()
    ext = "." + extensao    
    arquivos = [f for f in os.listdir(pasta) if f.lower().endswith(ext)]
    for arquivo in arquivos:
        listbox.insert(tk.END, arquivo)

def selecionar_destino():
    extensao = extensao_saida_var.get()
    filetypes = [("CSV files", "*.csv"), ("Excel files", "*.xlsx"), ("Text files", "*.txt")]
    destino = filedialog.asksaveasfilename(defaultextension=extensao, filetypes=filetypes)
    entry_destino.delete(0, tk.END)
    entry_destino.insert(0, destino)

def mesclar_arquivos():
    pasta = entry_pasta.get()
    destino = entry_destino.get()
    arquivos_selecionados = [listbox.get(i) for i in listbox.curselection()]
    codificacao = codificacao_var.get()
    delimitador_amigavel = delimitador_var.get()
    delimitadores = {
        "Comma - ,": ",",
        "Semicolon - ;": ";",
        "Tab - \\t": "\t"
    }
    delimitador = delimitadores.get(delimitador_amigavel, ",")
    extensao_entrada = extensao_entrada_var.get()
    extensao_saida = extensao_saida_var.get()

    if not pasta or not destino:
        messagebox.showerror("Error!", "Please select the folder and the destination!")
        return
    
    if var_todos.get():
        ext = extensao_entrada.lower().lstrip(".")
        arquivos_selecionados = [f for f in os.listdir(pasta) if f.lower().endswith(ext)]

    if not arquivos_selecionados:
        messagebox.showerror("Error!", "No file selected!")
        return
    
    progress_window = tk.Toplevel(tela)
    progress_window.title("Progress")
    progress_window.geometry("350x180")
    progress_window.iconbitmap(icon_path)
    
    file_label = tk.Label(progress_window, text= "Starting...", wraplength=300)
    file_label.pack(pady=5)
    
    progress = ttk.Progressbar(progress_window, length=300, mode='determinate')
    progress.pack(pady=10)
    
    cancelar = False
    
    def cancelar_processo():
        nonlocal cancelar
        cancelar = True
        progress_window.destroy()
    
    btn_cancelar = tk.Button(progress_window, text="Cancel", command=cancelar_processo)
    btn_cancelar.pack(pady=5)
    
    def processar():
        try:
            caminhos_arquivos = [os.path.join(pasta, f) for f in arquivos_selecionados]
            dfs = []
            for i, arquivo in enumerate(caminhos_arquivos):
                if cancelar:
                    return
                file_label.config(text=f"Processing: {os.path.basename(arquivo)}")
                if extensao_entrada in [".csv", ".txt"]:
                    df = pd.read_csv(arquivo, encoding=codificacao, delimiter=delimitador)
                else:
                    df = pd.read_excel(arquivo, engine="openpyxl")
                dfs.append(df)
                progress['value'] = (i + 1) / len(caminhos_arquivos) * 100
                tela.update_idletasks()
            
            df_final = pd.concat(dfs, ignore_index=True)
            
            if extensao_saida == ".csv":
                df_final.to_csv(destino, index=False, sep=delimitador)
            elif extensao_saida == ".xlsx":
                df_final.to_excel(destino, index=False)
            elif extensao_saida == ".txt":
                df_final.to_csv(destino, index=False, sep="\t")
            
            messagebox.showinfo("Success!", f"Files stacked successfully!\nFiles processed: {', '.join(arquivos_selecionados)}")
        except Exception as e:
            messagebox.showerror("Error!", "An error occurred: {str(e)}")
        finally:
            progress_window.destroy()
    
    threading.Thread(target=processar).start()

tela = tk.Tk()
icon_path = resource_path('empilhadeira.ico')
tela.title("Stack Files")
tela.geometry("500x600")
tela.iconbitmap(icon_path)

tk.Label(tela, text="1. Select the input file extension:").pack()
extensao_entrada_var = tk.StringVar(value=".csv")
extensoes = [".csv", ".xlsx", ".txt"]
extensao_entrada_combobox = ttk.Combobox(tela, textvariable=extensao_entrada_var, values=extensoes, state="readonly")
extensao_entrada_combobox.pack()

tk.Label(tela, text="2. Select the folder containing the files:").pack()
entry_pasta = tk.Entry(tela, width=60)
entry_pasta.pack()
tk.Button(tela, text="Browse", command=selecionar_pasta).pack()

tk.Label(tela, text="3. Choose the delimiter and encoding:").pack()
delimitador_var = tk.StringVar(value="Comma - ,")
delimitadores_amigaveis = ["Comma - ,", "Semicolon - ;", "Tab - \\t"]
delimitador_combobox = ttk.Combobox(tela, textvariable=delimitador_var, values=delimitadores_amigaveis, state="readonly")
delimitador_combobox.pack()
codificacao_var = tk.StringVar(value="utf-8")
codificacao_combobox = ttk.Combobox(tela, textvariable=codificacao_var, values=["utf-8", "utf-16", "latin1"], state="readonly")
codificacao_combobox.pack()

var_todos = tk.BooleanVar()
chk_todos = tk.Checkbutton(tela, text="Select all files automatically", variable=var_todos)
chk_todos.pack()

tk.Label(tela, text="4. Select the desired files:").pack()
listbox = tk.Listbox(tela, selectmode=tk.MULTIPLE, width=60, height=10)
listbox.pack()

tk.Label(tela, text="5. Select the output file extension:").pack()
extensao_saida_var = tk.StringVar(value=".csv")
extensao_saida_combobox = ttk.Combobox(tela, textvariable=extensao_saida_var, values=extensoes, state="readonly")
extensao_saida_combobox.pack()

tk.Label(tela, text="6. Select the name and destination of the final file:").pack()
entry_destino = tk.Entry(tela, width=60)
entry_destino.pack()
tk.Button(tela, text="Save As", command=selecionar_destino).pack()

tk.Button(tela, text="7. Stack Files", command=mesclar_arquivos).pack(pady=10)

tela.mainloop()
