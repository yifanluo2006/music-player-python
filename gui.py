import tkinter as tk
from music_player_system import *

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1100x800")
        

    def update(self, system):
         self.main_screen()
         self.display_user(system, 1)
         self.display_playlist(system, 1)
         self.window.mainloop()

    def main_screen(self):
        pass

    def display_user(self, system, userID):
        leftBar = tk.Frame(master = self.window, width = 250, bg = "grey")
        leftBar.pack(fill = tk.BOTH, side=tk.LEFT)
        leftBar.pack_propagate(0)
        rightSide = tk.Frame(master = self.window, width = 1000, bg = "black")
        rightSide.pack(fill = tk.BOTH, side=tk.LEFT)
        rightSide.pack_propagate(0)
        user = system.get_user(userID)
        name = tk.Label(leftBar, text="TEST", fg = "black", bg = "grey") # set text to username once one is established
        name.pack(side = tk.TOP)
        for p in range(len(user.playlists)):
        

    def display_playlist(self, system, playlist):
        pass
        
