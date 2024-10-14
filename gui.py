import tkinter as tk
from music_player_system import *

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1100x800")
        self.current_playlist = None
        self.rightSide = tk.Frame()
        self.leftBar = tk.Frame()


    def update(self, system):
         self.main_screen()
         self.display_user(system, 1)
         if(self.current_playlist != None):
             self.display_playlist(system, self.current_playlist)
         self.window.mainloop()

         

    def main_screen(self):
        self.leftBar = tk.Frame(master = self.window, width = 250, bg = "grey")
        self.leftBar.pack(fill = tk.BOTH, side=tk.LEFT)
        self.leftBar.pack_propagate(0)
        self.rightSide = tk.Frame(master = self.window, width = 1000, bg = "black")
        self.rightSide.pack(fill = tk.BOTH, side=tk.LEFT)
        self.rightSide.pack_propagate(0)

    def display_user(self, system, userID):
        
        user = system.get_user(userID)
        name = tk.Label(self.leftBar, text=user.username, fg = "black", bg = "grey") # set text to username once one is established
        name.pack(side = tk.TOP)
        for p in range(len(user.playlists)):
            tempframe = tk.Frame(master = self.leftBar, width = 250, height = 50, relief = tk.RAISED)
            tempframe.pack_propagate(0)
            tempframe.pack(side = tk.TOP)
            playlistdisp = tk.Label(tempframe, text = user.playlists[p].name)
            playlistdisp.pack(side = tk.LEFT)
            B = tk.Button(tempframe, text = "?" + str(p), relief = tk.RAISED, command = lambda p=p: self.choose_playlist(user, system, p))
            B.pack(side = tk.LEFT)

    def display_playlist(self, system, playlist):       
        print("displaying playlist") 
        playlistInfo = tk.Frame(master = self.rightSide, width = 1000, height = 30, relief = tk.RAISED, bg = "black")
        playlistInfo.pack()
        playlistInfo.pack_propagate(0)
        
        infoText = tk.Label(playlistInfo, text = str(playlist.name) + " OWNER: " + str(playlist.owner.username), fg = "white", bg = "black")
        infoText.pack()
        
        self.display_songs(system, self.rightSide, self.current_playlist.first_song)
        

    def display_songs(self, system, frame, first):
        container = tk.Frame(master = frame, width = 1000, height = 50)
        container.pack()
        container.pack_propagate(0)
        info = tk.Label(container, text = first.title + ", " + first.artist + ", " + first.genre)
        info.pack()
        print(first.title + ", " + first.artist + ", " + first.genre)
        if(first.next != None):
            self.display_songs(system, frame, first.next)
        
    def choose_playlist(self, user, system, playlist_index):
                 
        self.rightSide.destroy()
        self.rightSide = tk.Frame(master = self.window, width = 1000, bg = "black")
        self.rightSide.pack(fill = tk.BOTH, side=tk.LEFT)
        self.rightSide.pack_propagate(0)
    
        self.current_playlist = user.playlists[playlist_index]
        self.display_playlist(system, self.current_playlist)