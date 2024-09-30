from playlist import *

class User:
    def __init__(self, id, username):
        self.next = None

        self.id = id
        self.username = username
        self.library = Playlist()
        self.playlists = []
        self.populate_user_information()

    def populate_user_information():
        file = open("./data/user_" + str(id), "r") #reads the text file
        content = file.read()
        print(content)

    def set_next(self, next):
        self.next = next