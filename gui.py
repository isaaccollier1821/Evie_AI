import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading

from commands import run_command
from system_commands import run_system_command
from intent import detect_intent

class EvieGUI:

    def __init__(self):

        self.window = tk.Tk()

        self.window.title("Evie 🤖")

        self.window.geometry("700x600")

        self.chat = ScrolledText(
            self.window,
            wrap=tk.WORD,
            state="disabled",
            font=("Segoe UI", 11)
        )

        self.chat.pack(fill="both", expand=True, padx=10, pady=10)

        self.entry = tk.Entry(
            self.window,
            font=("Segoe UI", 12)
        )

        self.entry.pack(fill="x", padx=10)

        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(
            self.window,
            text="Send",
            command=self.send_message
        )

        self.send_button.pack(pady=10)
        self.add_message("Evie", "Hello! I am Evie. How can I help?")

    def add_message(self, speaker, message):

        self.chat.config(state="normal")

        self.chat.insert(
            tk.END,
            f"{speaker}: {message}\n\n"
        )

        self.chat.config(state="disabled")

        self.chat.see(tk.END)


    def send_message(self, event=None):

      message = self.entry.get().strip()

      if message == "":
        return

      self.add_message("You", message)

      self.entry.delete(0, tk.END)

      self.add_message("Evie", "Thinking...")

      threading.Thread(
        target=self.get_response,
        args=(message,),
        daemon=True
    ).start()

    def get_response(self, message):

        from ai_brain import ask_evie
        from voice import speak

        intent = detect_intent(message)

        if intent == "battery":
            response = run_system_command(message)

        elif intent == "screenshot":
            response = run_system_command(message)

        elif intent == "open_app":
            response = run_command(message)

        else:
          response = ask_evie(message)


        self.chat.config(state="normal")

        self.chat.delete(
        "end-3l",
        "end-1l"
    )

        self.chat.config(state="disabled")

        self.add_message("Evie", response)

        speak(response) 


    def run(self):

        self.window.mainloop()