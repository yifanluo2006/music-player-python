import tkinter as tk
from music_player_system import *

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1100x800")
        

    def update(self, system):
         self.main_screen()
         self.display_users(system, 1)
         self.window.mainloop()

    def main_screen(self):
        leftBar = tk.Frame(master = self.window, width = 250, bg = "grey")
        leftBar.pack(fill = tk.BOTH, side=tk.LEFT)
        rightSide = tk.Frame(master = self.window, width = 1000, bg = "black")
        rightSide.pack(fill = tk.BOTH, side=tk.LEFT)

    def display_users(self, system, userID):
        disp = system.get_user(userID)
        ID = tk.Label(text=disp.id)
        ID.place(400, 400)
        if(disp.next != None):
            self.display_users(self,system,userID+1)