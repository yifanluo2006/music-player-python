import tkinter as tk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1100x800")
        

    def update(self):
         self.mainScreen()
         self.window.mainloop()

    def mainScreen(self):
        leftBar = tk.Frame(master = self.window, width = 250, bg = "grey")
        leftBar.pack(fill = tk.BOTH, side=tk.LEFT)
        rightSide = tk.Frame(master = self.window, width = 1000, bg = "black")
        rightSide.pack(fill = tk.BOTH, side=tk.LEFT)