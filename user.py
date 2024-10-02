from playlist import *

class User:
    def __init__(self, id):
        self.next = None

        self.id = id
        self.username = None
       # self.library = Playlist(self.id * 10 + 0, "Library", self)
        self.playlists = []
        self.populate_user_information()

    def populate_user_information(self):
        file = open("./data/user_" + str(self.id) + ".txt", "r") #reads the text file
        content = file.read()
        
    def create_new_playlist(self, name):
        new_playlist = Playlist(self.id + len(self.playlists) + 1, name, self)
        self.playlists.append(new_playlist)

    def set_next(self, next):
        self.next = next

    #def get_name