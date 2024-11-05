import tkinter as tk
from music_player_system import *
from event_generator import *

import logging

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
        self.generate = None
        self.loggedin = False
        self.previous_playlists = []
        self.search_history = []
        self.clicked = tk.StringVar()
        self.clicked.set("History")
        self.history_menu = None

        self.user_action_logger = logging.getLogger("user_action_logger")

    def update(self, system): #essentially reset the screen
        if(self.loggedin == False):
             self.loginscreen(system)
        else:
            self.main_screen()
            self.display_user(system, self.current_user)
            if self.current_playlist is not None:
                self.display_playlist(system, self.current_playlist, self.current_user, True)
        self.window.mainloop()

#===================================================LOGIN=====================================================================#

    def loginscreen(self, system):
        mainloginframe = tk.Frame(master = self.window, width = 1100, height = 1000, bg = "black") #creating main segments of the login screen
        mainloginframe.place(x=0, y=0)
        subframe = tk.Frame(master = mainloginframe, width = 400, height = 1000, bg = 'black')
        subframe.place(x=350, y=150)
        subframe.pack_propagate(0)
        logintext = tk.Label(subframe, text = 'LOGIN', font = ("Arial", 50), fg = "white", bg = "black")
        logintext.pack()
        usernametext = tk.Label(subframe, text = 'USERNAME', font = ("Arial", 15), pady=10, fg = "white", bg = "black")
        usernametext.pack()
        usernameinput = tk.Text(subframe, height=1, width = 15)
        usernameinput.pack()
        passwordtext = tk.Label(subframe, text = "PASSWORD", font = ("Arial", 15), pady = 10, fg = "white", bg = "black")
        passwordtext.pack()
        passwordinput = tk.Text(subframe, height = 1, width = 15)
        passwordinput.pack()

        confirmbutton = tk.Button(subframe, text = "CONFIRM", command = lambda: self.loginattempt(system, subframe, usernameinput, passwordinput, errormessage, mainloginframe))
        confirmbutton.pack() #interactables

        newuserbutton = tk.Button(subframe, text = "NEW USER", command = lambda: self.newuserpopup(system, subframe, newuserbutton))
        newuserbutton.pack()

        errormessage = tk.Label(subframe, text = "INCORRECT USERNAME OR PASSWORD", fg = 'red', bg = 'black', font = ("Arial", 10))
        

        
    def loginattempt(self, system, subframe, userinput, passinput, error, bigboyframe):
        username = userinput.get(1.0, "end-1c") #grabbing the input text from the login username and password
        password = passinput.get(1.0, "end-1c") # text boxes

        if username == "Jaden" and password == "Yifan":
            self.adminwindow(system)
            self.loggedin = True #tells the gui to no longer display the login window
            bigboyframe.destroy() 
        elif(system.login_authentication(username, password) == None):
            error.pack() #send error message
        else:
            self.current_user = system.login_authentication(username, password).id #check within backend function
            self.loggedin = True #tells the gui to no longer display the login window
            bigboyframe.destroy() 
            self.update(system)
            


    def newuserpopup(self, system, subframe, button):
        #disabling the button once clicked to avoid creating infinite windows
        button = tk.Button(subframe, state = 'disabled', text = "NEW USER", command = lambda: self.newuserpopup(system, subframe))

        newprofilezone = tk.Frame(master = subframe, width = 400, height = 210, bg = "grey")
        newprofilezone.place(x=0,y=300)
        newprofilezone.pack_propagate(0)

        newprofilelabel = tk.Label(newprofilezone, text = 'NEW PROFILE', font = ("Arial", 20), bg = "gray")
        newprofilelabel.pack()

        usernametext = tk.Label(newprofilezone, text = 'USERNAME', font = ("Arial", 10), pady=10, bg = "gray") #all of this is to create a popup
        usernametext.pack()
        usernameinput = tk.Text(newprofilezone, height = 1, width = 15)
        usernameinput.pack()
        passwordtext = tk.Label(newprofilezone, text = "PASSWORD", font = ("Arial", 10), pady = 10, bg = "gray")
        passwordtext.pack()
        passwordinput = tk.Text(newprofilezone, height = 1, width = 15)
        passwordinput.pack()

        errormessage = tk.Label(newprofilezone, text = " ", fg = 'red', bg = "gray")

        confirmbutton = tk.Button(newprofilezone, text = "CREATE", padx=5, pady=5, command = lambda: self.usercreation(usernameinput, passwordinput, system, newprofilezone, errormessage))
        confirmbutton.pack()

        errormessage.pack()


    def usercreation(self, userinput, passinput, system, frame, error):
        username = userinput.get(1.0, "end-1c") #getting the user and password inputs
        password = passinput.get(1.0, "end-1c")
        errormessage = tk.Label(frame)
        if(len(username) < 3):
            error.config(text = "USERNAME TOO SHORT") #assign error message text
           
        elif(len(password) < 8):
            error.config(text = "PASSWORD TOO SHORT")
           
        elif(system.login_authentication(username, password) != None):
            error.config(text = "USER ALREADY IN USE")
           
        else:
            system.add_user(username, password)
            error.config(text = "USER ADDED")
        

#======================================================="ADMIN WINDOW"==================================================================#


    def adminwindow(self, system):
        self.main_screen()
        self.logout_button(system)
        self.test_button(system)
        self.log_buttons(system)
        
    def test_button(self, system):
        button = tk.Button(self.leftBar, text = "TEST ALL CASES", command = lambda: self.test_all(system))
        button.pack()

    def test_all(self, system):
        testuser = system.first_user

        system.create_playlist(testuser.id, "NEW PLAYLIST")
        testplaylist = testuser.playlists[-1]
        if testuser.playlists:
            print("SUCCESSFULLY CREATED PLAYLIST: " + testuser.playlists[-1].name)
        system.add_song_to_playlist(testuser.id, testplaylist.id, "s15")
        if(testplaylist.first_song.id == "s15"):
            print("SUCCESSFULLY ADDED " + testplaylist.first_song.title + " TO " + testuser.playlists[-1].name)
        # ADD A SONG FROM GENERATED SUGGESTIONS
        # REMOVE A SONG
    
    def log_buttons(self, system):
        full_log = tk.Button(self.leftBar, text = "FULL LOG", command = lambda: self.display_log(system, 0))
        manual_log = tk.Button(self.leftBar, text = "MANUAL LOGS", command = lambda: self.display_log(system, 1))
        event_log = tk.Button(self.leftBar, text = "EVENTS", command = lambda: self.display_log(system, 2))
        full_log.pack()
        manual_log.pack()
        event_log.pack()

    def display_log(self, system, type):
        if type == 0:
            file = open("./logs/system_event.log", "r")
            content = file.read()
            event_list = content.split('\n')
            for event in event_list:
                log = tk.Label(self.content_frame, text = event, bg = "black", fg = "white")
                log.pack()
            print("PASSED DISPLAYING FULL LOG")
        elif type == 1:
            file = open("./logs/user_action.log", "r")
            content = file.read()
            event_list = content.split('\n')
            for event in event_list:
                log = tk.Label(self.content_frame, text = event, bg = "black", fg = "white")
                log.pack()
        elif type == 2:
            file = open("./logs/event_generation.log", "r")
            content = file.read()
            event_list = content.split('\n')
            for event in event_list:
                log = tk.Label(self.content_frame, text = event, bg = "black", fg = "white")
                log.pack()


#===================================================================================================================================================================================

    def main_screen(self):
        self.leftBar = tk.Frame(master = self.window, width = 250, bg = "grey") #creates the MAIN segments
        self.leftBar.pack(fill = tk.BOTH, side=tk.LEFT) #of the gui, 90% of what is displayed goes here
        self.leftBar.pack_propagate(0)
        
        self.right_side_frame = tk.Frame(self.window)
        self.right_side_frame.pack(fill=tk.BOTH, side = tk.RIGHT, expand = True)

        self.rightSide = tk.Canvas(master = self.right_side_frame, bg = "black")
        self.rightSide.pack(fill = tk.BOTH, side=tk.LEFT, expand = True)
        
        self.scrollbar = tk.Scrollbar(self.right_side_frame, orient="vertical", command=self.rightSide.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y) #mmm scrollbar, this caused so much pain
        self.rightSide.configure(yscrollcommand=self.scrollbar.set)

        self.content_frame = tk.Frame(self.rightSide, bg="black")
        self.rightSide.create_window((0, 0), window=self.content_frame, anchor="nw")
        self.content_frame.bind("<Configure>", lambda event: self.rightSide.configure(scrollregion=self.rightSide.bbox("all")))



    def display_user(self, system, userID):
        
        user = system.get_user(userID)
        name = tk.Label(self.leftBar, text=user.username, fg = "black", bg = "grey") 
        name.pack(side = tk.TOP) #displaying what user is active at the top of the left bar
        
        self.displaySearch(system) #placing all the different varieties of buttons
        self.for_you(system)
        self.display_discovery_button(system)
        self.display_library_button(user, system)
        
        section_title = tk.Label(self.leftBar, text="Playlists", fg="black", bg="grey")
        section_title.pack(side=tk.TOP)
        
        for p in range(len(user.playlists)): #displaying each playlist individually with it own personal button
            tempframe = tk.Frame(master = self.leftBar, width = 250, height = 50, relief = tk.RAISED)
            tempframe.pack_propagate(0)
            tempframe.pack(side = tk.TOP)
            B = tk.Button(tempframe, text = user.playlists[p].name, relief = tk.RAISED, command = lambda p=p: self.choose_playlist(user, system, p))
            B.pack(side = tk.LEFT) 
        self.add_playlist_button(system, userID) #creating the button which allows you to view playlists
        self.logout_button(system)
    
    def logout_button(self, system):
        button = tk.Button(self.leftBar, text = "LOGOUT 🚪", command = lambda: self.logout(system))
        button.pack(side = tk.BOTTOM) 

    def logout(self, system): #essentially resets GUI entirely
        self.rightSide.destroy()
        self.leftBar.destroy()
        self.right_side_frame.destroy()
        self.loggedin = False
        self.update(system)


    def add_playlist_button(self, system, userID): #the button to create playlists
        playlistbutton = tk.Button(self.leftBar, text = "Add Playlist", pady = 5, command = lambda: self.add_playlist_menu(system, playlistbutton))
        playlistbutton.pack()

    def add_playlist_menu(self, system, playlistbutton): # the popup to create your new playlist
        
        playlistbutton.config(state = tk.DISABLED)
        newplaylistframe = tk.Frame(self.leftBar, width = 250, height = 100)
        newplaylistframe.pack()
        errormessage = tk.Label(newplaylistframe, text = "PLAYLIST NAME ALREADY TAKEN", fg = "red")
        newplaylistframe.pack_propagate(0)
        playlistname = tk.Entry(newplaylistframe, width = 30)
        playlistname.pack()
        confirmbutton = tk.Button(newplaylistframe, text = "CONFIRM", command = lambda: self.addplaylist(playlistname, system, newplaylistframe, errormessage))
        cancelbutton = tk.Button(newplaylistframe, text = "CANCEL", command = lambda: self.destroyframe(newplaylistframe, playlistbutton))
        confirmbutton.pack()
        cancelbutton.pack()

    def destroyframe(self, frame, button): #removes itself
        frame.destroy()
        button.config(state = tk.NORMAL)

    def addplaylist(self, nameinput, system, frame, errormessage):
        valid = True
        
        name = nameinput.get()
        for p in range(len(system.get_user(self.current_user).playlists)):
            invalidname = system.get_user(self.current_user).playlists[p].name
            if(name == invalidname):
                    valid = False
                    errormessage.pack_forget()
                    errormessage.pack()
                    break
        if valid == True:
            system.create_playlist(self.current_user, name)
            self.reset_left()
            self.display_user(system, self.current_user)
        


    def display_playlist(self, system, playlist, user, clear):  

        user = system.get_user(self.current_user)
        if clear == True: #this segment completely clears out the right side, it does not work in tandem
            self.rightSide.delete("all") #with things like the Suggestions button, hence why its optional
            self.content_frame = tk.Frame(self.rightSide, bg="black")
            self.rightSide.create_window((0, 0), window=self.content_frame, anchor="nw")
            self.content_frame.bind("<Configure>", lambda event: self.rightSide.configure(scrollregion=self.rightSide.bbox("all")))
             
        playlistInfo = tk.Frame(master=self.content_frame, width=850, height=30, relief=tk.RAISED, bg="black")
        playlistInfo.pack()
        playlistInfo.pack_propagate(0)
        
        infoText = tk.Label(playlistInfo, text = str(playlist.name), fg = "white", bg = "black")
        infoText.pack()

       
        
        self.display_songs(system, self.content_frame, playlist.first_song, user, playlist) #displays each individual song
        if clear == True and playlist.id != "99979" and playlist.id != "00000" and playlist.id != "99989" and playlist.id != "99979" and playlist.id != "99990" and playlist.name != "Complete Library":
            self.display_generate_suggestions_button(playlist, system)

    def display_generate_suggestions_button(self, playlist, system):
        errormessage = tk.Label(self.content_frame, text = "NO SONGS TO GATHER DATA FROM", bg = "black", fg = "red")
        self.generate = tk.Button(self.content_frame, text = 'GENERATE SUGGESTIONS', command = lambda: self.generate_suggestions(playlist, system, errormessage))
        self.generate.pack(side = tk.BOTTOM) 

    def generate_suggestions(self, playlist, system, errormessage):
        errormessage.pack_forget()
        if playlist.first_song == None:
            errormessage.pack()
        else:
            self.display_playlist(system, system.generate_suggestions(self.current_user, playlist.id), self.current_user, False)
            self.generate.pack_forget() #generates suggestions specific to playlist then removes self

    def display_songs(self, system, frame, song, user, currentplaylist):
        songcounter = 0
        while song is not None: #creates a display window for each new song
            container = tk.Frame(master = frame, width = 850, height = 50, highlightbackground = "black", highlightthickness = 1)
            container.pack()
            container.pack_propagate(0)
            info = tk.Label(container, text = song.title + ", " + song.artist + ", " + song.genre)
            info.pack()
            options = [ #a list of all playlists available to add songs to, will be expanded upon per user later
                user.library.name
            ]

            for p in range(len(user.playlists)):

                addition = user.playlists[p].name #adds all of the users individual playlists
                options.append(addition)

            clicked = tk.StringVar() #keeps track of what is chosen in the menus

            add_to_button = tk.Button(container, text = "ADD TO:", width = 8, command = lambda s=song, c = clicked:  self.addtoplaylist(c, system, s))
            add_to_button.place(x=300, y=23) #creates the button to add to a playlist
            
            if currentplaylist.id != "00000" and currentplaylist.id != "99989" and currentplaylist.id != "99979" and currentplaylist.id != "99990" and currentplaylist.name != "Complete Library":
                remove_button = tk.Button(container, text = "-", fg = "red", command = lambda removed = song, con = container: self.remove_song(system, currentplaylist, con, removed))
                remove_button.place(x=800, y=5) #ensures you can remove songs, as long as its not in suggestions, for you, or the complete list
            
            clicked.set("Library") #initial menu value
            dropmenu = tk.OptionMenu(container, clicked, *options)
            dropmenu.pack()

            songcounter += 1
            song=song.get_next() #repeats the loop
            
            if(songcounter > 101):  #once the amount of songs reaches 100, create a new page for the songs
                new_page = Playlist("{0:03d}".format(self.current_user) + "99", currentplaylist.name, system.get_user(self.current_user))
                while song is not None:
                    new_page.add_song(song.id, song.title, song.artist, song.genre, song.bpm, song.meta)
                    song=song.get_next()
                next_page_button = tk.Button(self.content_frame, text = ">", command = lambda: self.next_page(currentplaylist, new_page, system))
                next_page_button.pack(side = tk.BOTTOM)
            
    def remove_song(self, system, currentplaylist, container, song):
        container.destroy() #remove from GUI
        system.delete_song_in_playlist(song, currentplaylist) #remove from backend

    def next_page(self, previous, next, system):
        self.previous_playlists.append(previous) #keep track of all previous pages
        self.display_playlist(system, next, self.current_user, True)
        if(len(self.previous_playlists) != 0): #creates a button to go to prev pages IF previous pages exist
                prev_page_button = tk.Button(self.content_frame, text = "<", command = lambda: self.prev_page(system))
                prev_page_button.pack(side = tk.BOTTOM)
        self.rightSide.yview("moveto", 0)

    def prev_page(self, system):
        self.display_playlist(system, self.previous_playlists[-1], self.current_user, True)
        self.previous_playlists.pop() #goes to the most recent previous page
        if(len(self.previous_playlists) != 0):
                prev_page_button = tk.Button(self.content_frame, text = "<", command = lambda: self.prev_page(system))
                prev_page_button.pack(side = tk.BOTTOM)
        self.rightSide.yview("moveto", 0)
        

    def addtoplaylist(self, name, system, song): #where the magic happens
        playlist = name.get()
        user = system.get_user(self.current_user)
        if(user != None):

            if(playlist == "Library"):
                system.add_song_to_library(self.current_user, song.id)
            else:
                for index, item in enumerate(user.playlists): #checks until it finds the correct playlist to add to
                    if item.name == playlist:
                        system.add_song_to_playlist(user.id, item.id, song.id)
                    
        
        
    def choose_playlist(self, user, system, playlist_index):
        self.previous_playlists = []
        self.reset_right()
        if playlist_index == -1:
            self.current_playlist = user.library
        else:
            self.current_playlist = user.playlists[playlist_index]
        self.display_playlist(system, self.current_playlist, user, True)

    def displaySearch(self, system):
        
        searchbar = tk.Frame(master = self.leftBar, width = 250, height = 75) #the searchbar area being created
        searchbar.pack(side = tk.TOP)
        searchbar.pack_propagate(0)
        if self.search_history: #passes through if search history is not empty
            self.clicked = tk.StringVar()
            self.clicked.set("History")
            history = tk.OptionMenu(searchbar, self.clicked, *self.search_history)
            history.pack(side = tk.BOTTOM)
        search_button = tk.Button(searchbar, text = '🔍', command = lambda: self.search(search_input, system))
        search_button.pack(side = tk.LEFT)
        search_input = tk.Entry(searchbar, width = 45)
        search_input.pack(side = tk.LEFT)

        if self.search_history:
            self.clicked.set("History")
            if self.history_menu is not None and self.history_menu.winfo_exists():
                menu = self.history_menu['menu']
                menu.delete(0, 'end')
                for item in self.search_history:
                    menu.add_command(label = item, command = tk._setit(self.clicked, item))
            else:
                self.history_menu = tk.OptionMenu(searchbar, self.clicked, *self.search_history)
                self.history_menu.pack(side = tk.BOTTOM)
        

    def search(self, search_input, system):
        inp = search_input.get().strip() #inputs anything insert into text box into the backend search function
        

        if self.clicked.get() != "History" and self.clicked.get():
            inp = self.clicked.get()
            self.clicked.set("History")
        elif inp:
            self.search_history.append(inp)
            self.update_search_history
        
        result = system.search_songs(inp)

        self.user_action_logger.info("Searching for query " + str(inp))
        self.reset_right()
        self.reset_left()

        self.display_user(system, self.current_user)
        self.current_playlist = result #search result is returned as a playlist, allowing for easy display
        self.display_playlist(system, result, self.current_user, True)

    def update_search_history(self):
        if self.history_menu is not None and self.history_menu.winfo_exists():
            menu = self.history_menu['menu']
            menu.delete(0, 'end')
            for item in self.search_history:
                menu.add_command(label=item, command = tk._setit(self.clicked, item))
        

    def reset_right(self):
        self.rightSide.delete("all") #removes everything in the right side of the screen

    def reset_left(self):
        self.leftBar.destroy() #removes everything in the left side of the screen
        self.leftBar = tk.Frame(master = self.window, width = 250, bg = "grey")
        self.leftBar.pack(fill = tk.BOTH, side=tk.LEFT)
        self.leftBar.pack_propagate(0)
        self.history_menu = None

    def display_discovery_button(self, system):
        discovery = tk.Button(self.leftBar, text = "Browse", width = 250, command = lambda: self.discovery_button(system))
        discovery.pack(side = tk.TOP)

    def discovery_button(self, system):
        
        self.display_playlist(system, system.get_most_popular_songs(3), system.get_user(self.current_user), True)

        self.user_action_logger.info("Fetching most trending songs")

        self.display_playlist(system, system.complete_list, system.get_user(self.current_user), False)

    def display_library_button(self, user, system):
        librarybutton = tk.Button(self.leftBar, text = "Library", width = 250, command = lambda: self.choose_playlist(user, system, -1))
        librarybutton.pack(side = tk.TOP)

    def for_you(self, system):
        foryoubutton = tk.Button(self.leftBar, text = "For You", width = 250, command = lambda: self.foryoucommand(system))
        foryoubutton.pack()
    
    def foryoucommand(self, system):
        user = system.get_user(self.current_user)
        self.display_playlist(system, system.generate_suggestions(user.id, user.library.id), user, True)