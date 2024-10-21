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
        self.loggedin = False

    def update(self, system):
         if(self.loggedin == False):
             self.loginscreen(system)
         else:
            self.main_screen()
            self.display_user(system, self.current_user)
            if self.current_playlist is not None:
                 self.display_playlist(system, self.current_playlist, self.current_user)
         self.window.mainloop()

#===================================================LOGIN=====================================================================#

    def loginscreen(self, system):
        mainloginframe = tk.Frame(master = self.window, width = 500, height = 1000, bg = "grey")
        mainloginframe.place(x=300, y=0)
        subframe = tk.Frame(master = mainloginframe, width = 400, height = 500, bg = 'gray')
        subframe.place(x=50, y=150)
        subframe.pack_propagate(0)
        logintext = tk.Label(subframe, text = 'LOGIN', font = ("Arial", 25))
        logintext.pack()
        usernametext = tk.Label(subframe, text = 'USERNAME', font = ("Arial", 10), pady=10)
        usernametext.pack()
        usernameinput = tk.Text(subframe, height=1, width = 15)
        usernameinput.pack()
        passwordtext = tk.Label(subframe, text = "PASSWORD", font = ("Arial", 10), pady = 10)
        passwordtext.pack()
        passwordinput = tk.Text(subframe, height = 1, width = 15)
        passwordinput.pack()

        confirmbutton = tk.Button(subframe, text = "CONFIRM", command = lambda: self.loginattempt(system, subframe, usernameinput, passwordinput, errormessage, mainloginframe))
        confirmbutton.pack()

        newuserbutton = tk.Button(subframe, text = "NEW USER", command = lambda: self.newuserpopup(system, subframe, newuserbutton))
        newuserbutton.pack()

        errormessage = tk.Label(subframe, text = "INCORRECT USERNAME OR PASSWORD", fg = 'red', bg = 'gray', font = ("Arial", 10))
        

        
    def loginattempt(self, system, subframe, userinput, passinput, error, bigboyframe):
        username = userinput.get(1.0, "end-1c")
        password = passinput.get(1.0, "end-1c")
        
        if(system.login_authentication(username, password) == None):
            error.pack()
        else:
            self.current_user = system.login_authentication(username, password).id
            self.loggedin = True
            bigboyframe.destroy()
            self.update(system)
            print(self.current_user)


    def newuserpopup(self, system, subframe, button):
        button = tk.Button(subframe, state = 'disabled', text = "NEW USER", command = lambda: self.newuserpopup(system, subframe))

        newprofilezone = tk.Frame(master = subframe, width = 400, height = 250)
        newprofilezone.place(x=0,y=300)
        newprofilezone.pack_propagate(0)

        newprofilelabel = tk.Label(newprofilezone, text = 'NEW PROFILE', font = ("Arial", 10))
        newprofilelabel.pack()

        usernametext = tk.Label(newprofilezone, text = 'USERNAME', font = ("Arial", 10), pady=10)
        usernametext.pack()
        usernameinput = tk.Text(newprofilezone, height = 1, width = 15)
        usernameinput.pack()
        passwordtext = tk.Label(newprofilezone, text = "PASSWORD", font = ("Arial", 10), pady = 10)
        passwordtext.pack()
        passwordinput = tk.Text(newprofilezone, height = 1, width = 15)
        passwordinput.pack()

        errormessage = tk.Label(newprofilezone, text = " ", fg = 'red')

        confirmbutton = tk.Button(newprofilezone, text = "CREATE", command = lambda: self.usercreation(usernameinput, passwordinput, system, newprofilezone, errormessage))
        confirmbutton.pack()

        errormessage.pack()


    def usercreation(self, userinput, passinput, system, frame, error):
        username = userinput.get(1.0, "end-1c")
        password = passinput.get(1.0, "end-1c")
        errormessage = tk.Label(frame)
        if(len(username) < 3):
            error.config(text = "USERNAME TOO SHORT")
           
        elif(len(password) < 8):
            error.config(text = "PASSWORD TOO SHORT")
           
        elif(system.login_authentication(username, password) != None):
            error.config(text = "USER ALREADY IN USE")
           
        else:
            system.add_user(username, password)
            error.config(text = "USER ADDED")
        

#============================================================================================================================#


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
        


    def display_playlist(self, system, playlist, user):  
        
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
        
        self.display_songs(system, self.content_frame, self.current_playlist.first_song, user)

        

    def display_songs(self, system, frame, song, user):
        
        while song is not None:
            container = tk.Frame(master = frame, width = 850, height = 50)
            container.pack()
            container.pack_propagate(0)
            info = tk.Label(container, text = song.title + ", " + song.artist + ", " + song.genre)
            info.pack()
            options = [
                user.library.name
            ]

            for p in range(len(user.playlists)):

                addition = user.playlists[p].name
                options.append(addition)

            clicked = tk.StringVar()

            add_to_button = tk.Button(container, text = "ADD TO:", width = 8, command = lambda s=song, c = clicked:  self.addtoplaylist(c, system, s))
            add_to_button.place(x=300, y=24)
            
            
            clicked.set("Library")
            dropmenu = tk.OptionMenu(container, clicked, *options)
            dropmenu.pack()

            song = song.get_next()

    def addtoplaylist(self, name, system, song):
        playlist = name.get()
        user = system.get_user(self.current_user)
        if(playlist == "Library"):
            system.add_song_to_library(self.current_user, song.id)
        else:
            for index, item in enumerate(user.playlists):
                print(item.name)
                if item.name == playlist:
                    system.add_song_to_playlist(user.id, item.id, song.id) # doesnt seem to be working quite yet
                    
        
        
    def choose_playlist(self, user, system, playlist_index):
        
        self.reset_right()
        if playlist_index == -1:
            self.current_playlist = user.library
        else:
            self.current_playlist = user.playlists[playlist_index]
        self.display_playlist(system, self.current_playlist, user)

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