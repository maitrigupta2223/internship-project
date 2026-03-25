import tkinter as tk
from tkinter import ttk
from zxcvbn import zxcvbn
import math
import matplotlib.pyplot as plt

# ----------------------
# Password Entropy
# ----------------------

def calculate_entropy(password):

    if len(password) == 0:
        return 0

    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(not c.isalnum() for c in password):
        charset += 32

    entropy = len(password) * math.log2(charset)
    return round(entropy,2)

# ----------------------
# Strength Analysis
# ----------------------

def analyze_password(event=None):

    password = password_entry.get()

    if password == "":
        return

    result = zxcvbn(password)

    score = result["score"]

    entropy = calculate_entropy(password)

    entropy_label.config(text=f"Entropy: {entropy} bits")

    # strength text
    strength_levels = [
        "Very Weak",
        "Weak",
        "Moderate",
        "Strong",
        "Very Strong"
    ]

    strength_label.config(text=f"Strength: {strength_levels[score]}")

    # color meter
    colors = ["red","orange","yellow","lightgreen","green"]

    strength_bar["value"] = (score+1)*20
    style.configure(
        "Strength.Horizontal.TProgressbar",
        troughcolor="#333",
        background=colors[score]
    )

# ----------------------
# Strength Graph
# ----------------------

def show_graph():

    password = password_entry.get()

    if password == "":
        return

    result = zxcvbn(password)

    score = result["score"]

    labels = ["Very Weak","Weak","Moderate","Strong","Very Strong"]

    values = [0,0,0,0,0]
    values[score] = 1

    plt.figure(figsize=(6,4))
    plt.bar(labels, values)
    plt.title("Password Strength Analysis")
    plt.ylabel("Strength Level")
    plt.show()

# ----------------------
# GUI
# ----------------------

root = tk.Tk()
root.title("Cyber Password Security Analyzer")
root.geometry("600x400")
root.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use("default")

# Title
title = tk.Label(
    root,
    text="Password Strength Analyzer",
    font=("Arial",18,"bold"),
    bg="#1e1e1e",
    fg="cyan"
)

title.pack(pady=15)

# Password Entry
password_entry = tk.Entry(
    root,
    width=35,
    font=("Arial",12)
)

password_entry.pack(pady=10)
password_entry.bind("<KeyRelease>", analyze_password)

# Strength Label
strength_label = tk.Label(
    root,
    text="Strength: ",
    bg="#1e1e1e",
    fg="white",
    font=("Arial",12)
)

strength_label.pack()

# Entropy Label
entropy_label = tk.Label(
    root,
    text="Entropy: ",
    bg="#1e1e1e",
    fg="white",
    font=("Arial",12)
)

entropy_label.pack(pady=5)

# Strength Meter
strength_bar = ttk.Progressbar(
    root,
    style="Strength.Horizontal.TProgressbar",
    orient="horizontal",
    length=300,
    mode="determinate"
)

strength_bar.pack(pady=10)

# Graph Button
graph_button = tk.Button(
    root,
    text="Show Strength Graph",
    command=show_graph,
    bg="#00aaff",
    fg="white",
    font=("Arial",11)
)

graph_button.pack(pady=15)

root.mainloop()
