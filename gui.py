import tkinter as tk
from music_player_system import *

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1100x800")
        self.current_playlist = None
        self.right_side_frame = tk.Frame()
        self.rightSide = tk.Canvas()
        self.leftBar = tk.Frame()
        self.scrollbar = tk.Scrollbar(self.rightSide)
        self.current_user = 1

    def update(self, system):
         self.main_screen()
         self.display_user(system, self.current_user)
         if(self.current_playlist != None):
             self.display_playlist(system, self.current_playlist)
         self.window.mainloop()

         

    def main_screen(self):
        self.leftBar = tk.Frame(master = self.window, width = 250, bg = "grey")
        self.leftBar.pack(fill = tk.BOTH, side=tk.LEFT)
        self.leftBar.pack_propagate(0)



        self.rightSide = tk.Canvas(master = self.right_side_frame, width = 850, height = 2000, bg = "black", yscrollcommand = self.scrollbar.set)
        self.rightSide.pack(fill = tk.X, side=tk.RIGHT)
        self.rightSide.pack_propagate(0)

    def display_user(self, system, userID):
        
        user = system.get_user(userID)
        name = tk.Label(self.leftBar, text=user.username, fg = "black", bg = "grey") 
        name.pack(side = tk.TOP)
        
        self.displaySearch(system)
        self.for_you(system)
        self.display_discovery_button()
        self.display_library_button(user, system)
        
        for p in range(len(user.playlists)):
            tempframe = tk.Frame(master = self.leftBar, width = 250, height = 50, relief = tk.RAISED)
            tempframe.pack_propagate(0)
            tempframe.pack(side = tk.TOP)
            playlistdisp = tk.Label(tempframe, text = user.playlists[p].name)
            playlistdisp.pack(side = tk.LEFT)
            B = tk.Button(tempframe, text = "?", relief = tk.RAISED, command = lambda p=p: self.choose_playlist(user, system, p))
            B.pack(side = tk.LEFT)
        self.add_playlist_button(system, userID)

    def add_playlist_button(self, system, userID):
        playlistbutton = tk.Button(self.leftBar, text = "Add Playlist", pady = 5, command = lambda: self.add_playlist_menu(system, playlistbutton))
        playlistbutton.pack()

    def add_playlist_menu(self, system, playlistbutton):
        playlistbutton.config(state = tk.DISABLED)
        newplaylistframe = tk.Frame(self.leftBar, width = 250, height = 100)
        newplaylistframe.pack()
        newplaylistframe.pack_propagate()
        playlistname = tk.Text(newplaylistframe, height = 10, width = 30)
        playlistname.pack()
        confirmbutton = tk.Button(newplaylistframe, text = "CONFIRM", command = lambda: self.addplaylist(playlistname, system, newplaylistframe))
        cancelbutton = tk.Button(newplaylistframe, text = "CANCEL", command = lambda: self.destroyframe(newplaylistframe, playlistbutton))
        confirmbutton.pack()
        cancelbutton.pack()

    def destroyframe(self, frame, button):
        frame.destroy()
        button.config(state = tk.NORMAL)

    def addplaylist(self, nameinput, system, frame):
        name = nameinput.get(1.0, "end-1c")
        system.create_playlist(self.current_user, name)
        self.reset_left()
        self.display_user(system, self.current_user)
        


    def display_playlist(self, system, playlist):       
        playlistInfo = tk.Frame(master = self.rightSide, width = 850, height = 30, relief = tk.RAISED, bg = "black")
        playlistInfo.pack()
        playlistInfo.pack_propagate(0)
        
        infoText = tk.Label(playlistInfo, text = str(playlist.name), fg = "white", bg = "black")
        infoText.pack()

        print(playlist.first_song.genre)

        #  + " OWNER: " + str(playlist.owner.username)

        #scrollbar goes here
        self.scrollbar = tk.Scrollbar(self.rightSide)
        self.scrollbar.config(command = self.rightSide.yview)
        self.scrollbar.pack(side = tk.RIGHT, fill =tk.Y)
        
        self.display_songs(system, self.rightSide, self.current_playlist.first_song)
        

    def display_songs(self, system, frame, first):
        container = tk.Frame(master = frame, width = 850, height = 50)
        container.pack()
        container.pack_propagate(0)
        info = tk.Label(container, text = first.title + ", " + first.artist + ", " + first.genre)
        info.pack()
        if(first.next != None):
            self.display_songs(system, frame, first.next)
        
    def choose_playlist(self, user, system, playlist_index):
        
        self.reset_right()
        if(playlist_index == -1):
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
        search_input = tk.Text(searchbar, height = 10, width = 30)
        search_input.pack(side = tk.LEFT)


    def search(self, search_input, system):
        inp = search_input.get(1.0, "end-1c")
        
        self.reset_right()

        result = system.search_songs_in_playlist(self.current_playlist, inp)
        
        self.current_playlist = result
        self.display_playlist(system, result)

    def reset_right(self):
        self.rightSide.destroy()
        self.rightSide = tk.Canvas(master = self.window, width = 850, bg = "black")
        self.rightSide.pack(fill = tk.BOTH, side=tk.RIGHT)
        self.rightSide.pack_propagate(0)

    def reset_left(self):
        self.leftBar.destroy()
        self.leftBar = tk.Frame(master = self.window, width = 250, bg = "grey")
        self.leftBar.pack(fill = tk.BOTH, side=tk.LEFT)
        self.leftBar.pack_propagate(0)

    def display_discovery_button(self):
        discovery = tk.Button(self.leftBar, text = "Discovery", width = 250, command = self.discovery_button)
        discovery.pack(side = tk.TOP)

    def discovery_button(self):
        pass

    def display_library_button(self, user, system):
        librarybutton = tk.Button(self.leftBar, text = "Library", width = 250, command = lambda: self.choose_playlist(user, system, -1))
        librarybutton.pack(side = tk.TOP)

    def for_you(self, system):
        foryoubutton = tk.Button(self.leftBar, text = "For You", width = 250, command = self.foryoucommand)
        foryoubutton.pack()
    
    def foryoucommand():
        pass