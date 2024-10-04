import tkinter as tk
from music_player_system import *

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1100x800")
        self.current_playlist = None
        

    def update(self, system):
         self.main_screen()
         self.display_user(system, 1)
         if(self.current_playlist != None):
             self.display_playlist(system, self.current_playlist)
         self.window.mainloop()

    def main_screen(self):
        pass

    def display_user(self, system, userID):
        leftBar = tk.Frame(master = self.window, width = 250, bg = "grey")
        leftBar.pack(fill = tk.BOTH, side=tk.LEFT)
        leftBar.pack_propagate(0)
        topBar = tk.Frame(master = leftBar, width = 250)
        topBar.pack_propagate(0)
        topBar.pack()
        user = system.get_user(userID)
        name = tk.Label(topBar, text="TEST", fg = "black", bg = "grey") # set text to username once one is established
        name.pack(side = tk.TOP)
        for p in range(len(user.playlists)+1):
            tempframe = tk.frame(master = leftBar, width = 250, relief = tk.RAISED)
            tempframe.pack+propagate(0)
            tempframe.pack()
            playlistdisp = tk.Label(tempframe, text = user.playlists[p].name)
            playlistdisp.pack(side = tk.LEFT)
            B = tk.Button(tempframe, text = "+", relief = tk.RAISED, command = self.choose_playlist(p))
            B.pack(side = tk.LEFT)

    def display_playlist(self, system, playlist):
        rightSide = tk.Frame(master = self.window, width = 1000, bg = "black")
        rightSide.pack(fill = tk.BOTH, side=tk.LEFT)
        rightSide.pack_propagate(0)
        playlistInfo = tk.Frame(master = rightSide, width = 1000, relief = tk.RAISED)
        playlistInfo.pack()
        playlistInfo.pack_propagate(0)
        
        
    def choose_playlist(self, p):
        self.current_playlist = p