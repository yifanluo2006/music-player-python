import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1000x800")

    def update(self):
        self.window.mainloop()