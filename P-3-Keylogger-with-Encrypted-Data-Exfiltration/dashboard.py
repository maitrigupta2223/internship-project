import tkinter as tk
from datetime import datetime
from encryption import encrypt_data
import requests

log_file = "logs/encrypted_logs.txt"

def log_event():
    text = entry.get()

    if text:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = f"{timestamp} - {text}"

        encrypted = encrypt_data(log)

        with open(log_file,"ab") as f:
            f.write(encrypted+b"\n")

        status_label.config(text="Log saved and encrypted")

def send_logs():
    with open(log_file,"rb") as f:
        data = f.read()

    requests.post("http://127.0.0.1:5000/upload",data=data)

    status_label.config(text="Logs sent to server")

root = tk.Tk()
root.title("Secure Activity Monitor")
root.geometry("600x400")
root.configure(bg="#1e1e1e")

title = tk.Label(root,text="Secure Activity Monitor",
font=("Arial",16,"bold"),fg="white",bg="#1e1e1e")
title.pack(pady=10)

entry = tk.Entry(root,width=40)
entry.pack(pady=10)

log_btn = tk.Button(root,text="Log Activity",command=log_event,bg="#4CAF50",fg="white")
log_btn.pack(pady=5)

send_btn = tk.Button(root,text="Send Logs",command=send_logs,bg="#2196F3",fg="white")
send_btn.pack(pady=5)

status_label = tk.Label(root,text="",fg="white",bg="#1e1e1e")
status_label.pack(pady=10)

root.mainloop()
