import tkinter as tk

window = tk.Tk()

window.title("Evie")

window.geometry("500x700")

label = tk.Label(
    window,
    text="Hello! I'm Evie 🤖",
    font=("Arial", 18)
)

label.pack(pady=20)

window.mainloop()