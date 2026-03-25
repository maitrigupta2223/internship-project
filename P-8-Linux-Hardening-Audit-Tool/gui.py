import tkinter as tk
from audit import run_audit

def start_audit():

    results, score = run_audit(gui_mode=True)

    output.delete("1.0", tk.END)

    output.insert(tk.END, f"Security Score: {score}%\n\n")

    for k,v in results.items():
        status = "PASS" if v[0] else "FAIL"

        output.insert(tk.END, f"{k}: {status} - {v[1]}\n")


root = tk.Tk()
root.title("Linux Hardening Audit Tool")
root.geometry("600x400")
root.configure(bg="#0d1117")

title = tk.Label(root,
text="Linux Security Audit Dashboard",
fg="#00e5ff",
bg="#0d1117",
font=("Arial",16))
title.pack(pady=20)

btn = tk.Button(root,
text="Run Audit",
command=start_audit,
bg="#00e5ff")
btn.pack(pady=10)

output = tk.Text(root,
bg="#161b22",
fg="white",
height=15)
output.pack()

root.mainloop()
