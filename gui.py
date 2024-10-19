import tkinter as tk
from music_player_system import *

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1100x800")
        self.current_playlist = None
        self.current_user = 1
        self.right_side_frame = tk.Frame()
        self.rightSide = tk.Canvas()
        self.leftBar = tk.Frame()
        self.scrollbar = tk.Scrollbar()

    def update(self, system):
         self.main_screen()
         self.display_user(system, self.current_user)
         if self.current_playlist is not None:
             self.display_playlist(system, self.current_playlist)
         self.window.mainloop()

         

    def main_screen(self):
        self.leftBar = tk.Frame(master = self.window, width = 250, bg = "grey")
        self.leftBar.pack(fill = tk.BOTH, side=tk.LEFT)
        self.leftBar.pack_propagate(0)
        
        self.right_side_frame = tk.Frame(self.window)
        self.right_side_frame.pack(fill=tk.BOTH, side = tk.RIGHT, expand = True)

        self.rightSide = tk.Canvas(master = self.right_side_frame, bg = "black")
        self.rightSide.pack(fill = tk.BOTH, side=tk.LEFT, expand = True)
        
        self.scrollbar = tk.Scrollbar(self.right_side_frame, orient="vertical", command=self.rightSide.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.rightSide.configure(yscrollcommand=self.scrollbar.set)



    def display_user(self, system, userID):
        
        user = system.get_user(userID)
        name = tk.Label(self.leftBar, text=user.username, fg = "black", bg = "grey") 
        name.pack(side = tk.TOP)
        
        self.displaySearch(system)
        self.for_you(system)
        self.display_discovery_button()
        self.display_library_button(user, system)
        
        section_title = tk.Label(self.leftBar, text="Playlists", fg="black", bg="grey")
        section_title.pack(side=tk.TOP)
        
        for p in range(len(user.playlists)):
            tempframe = tk.Frame(master = self.leftBar, width = 250, height = 50, relief = tk.RAISED)
            tempframe.pack_propagate(0)
            tempframe.pack(side = tk.TOP)
            B = tk.Button(tempframe, text = user.playlists[p].name, relief = tk.RAISED, command = lambda p=p: self.choose_playlist(user, system, p))
            B.pack(side = tk.LEFT)
        self.add_playlist_button(system, userID)

    def add_playlist_button(self, system, userID):
        playlistbutton = tk.Button(self.leftBar, text = "Add Playlist", pady = 5, command = lambda: self.add_playlist_menu(system, playlistbutton))
        playlistbutton.pack()

    def add_playlist_menu(self, system, playlistbutton):
        playlistbutton.config(state = tk.DISABLED)
        newplaylistframe = tk.Frame(self.leftBar, width = 250, height = 100)
        newplaylistframe.pack()
        newplaylistframe.pack_propagate(0)
        playlistname = tk.Entry(newplaylistframe, width = 30)
        playlistname.pack()
        confirmbutton = tk.Button(newplaylistframe, text = "CONFIRM", command = lambda: self.addplaylist(playlistname, system, newplaylistframe))
        cancelbutton = tk.Button(newplaylistframe, text = "CANCEL", command = lambda: self.destroyframe(newplaylistframe, playlistbutton))
        confirmbutton.pack()
        cancelbutton.pack()

    def destroyframe(self, frame, button):
        frame.destroy()
        button.config(state = tk.NORMAL)

    def addplaylist(self, nameinput, system, frame):
        name = nameinput.get()
        system.create_playlist(self.current_user, name)
        self.reset_left()
        self.display_user(system, self.current_user)
        


    def display_playlist(self, system, playlist):  
        
        self.rightSide.delete("all")
        
        self.content_frame = tk.Frame(self.rightSide, bg="black")
        self.rightSide.create_window((0, 0), window=self.content_frame, anchor="nw")
        self.content_frame.bind("<Configure>", lambda event: self.rightSide.configure(scrollregion=self.rightSide.bbox("all")))
             
        playlistInfo = tk.Frame(master=self.content_frame, width=850, height=30, relief=tk.RAISED, bg="black")
        playlistInfo.pack()
        playlistInfo.pack_propagate(0)
        
        infoText = tk.Label(playlistInfo, text = str(playlist.name), fg = "white", bg = "black")
        infoText.pack()

        # print(playlist.first_song.genre)
        #  + " OWNER: " + str(playlist.owner.username)
        
        self.display_songs(system, self.content_frame, self.current_playlist.first_song)

        

    def display_songs(self, system, frame, song):
        
        while song is not None:
            container = tk.Frame(master = frame, width = 850, height = 50)
            container.pack()
            container.pack_propagate(0)
            info = tk.Label(container, text = song.title + ", " + song.artist + ", " + song.genre)
            info.pack()
            song = song.get_next()
        
    def choose_playlist(self, user, system, playlist_index):
        
        self.reset_right()
        if playlist_index == -1:
            self.current_playlist = user.library
        else:
            self.current_playlist = user.playlists[playlist_index]
        self.display_playlist(system, self.current_playlist)

    def displaySearch(self, system):
        searchbar = tk.Frame(master = self.leftBar, width = 250, height = 50)
        searchbar.pack(side = tk.TOP)
        searchbar.pack_propagate(0)
        search_button = tk.Button(searchbar, text = '🔍', command = lambda: self.search(search_input, system))
        search_button.pack(side = tk.LEFT)
        search_input = tk.Entry(searchbar, width = 45)
        search_input.pack(side = tk.LEFT)


    def search(self, search_input, system):
        inp = search_input.get()
        
        self.reset_right()

        # result = system.search_songs_in_playlist(self.current_playlist, inp)
        result = system.search_songs(inp)
        
        self.current_playlist = result
        self.display_playlist(system, result)

    def reset_right(self):
        self.rightSide.delete("all")

    def reset_left(self):
        self.leftBar.destroy()
        self.leftBar = tk.Frame(master = self.window, width = 250, bg = "grey")
        self.leftBar.pack(fill = tk.BOTH, side=tk.LEFT)
        self.leftBar.pack_propagate(0)

    def display_discovery_button(self):
        discovery = tk.Button(self.leftBar, text = "Browse", width = 250, command = self.discovery_button)
        discovery.pack(side = tk.TOP)

    def discovery_button(self):
        pass

    def display_library_button(self, user, system):
        librarybutton = tk.Button(self.leftBar, text = "Library", width = 250, command = lambda: self.choose_playlist(user, system, -1))
        librarybutton.pack(side = tk.TOP)

    def for_you(self, system):
        foryoubutton = tk.Button(self.leftBar, text = "For You", width = 250, command = self.foryoucommand)
        foryoubutton.pack()
    
    def foryoucommand(self):
        pass