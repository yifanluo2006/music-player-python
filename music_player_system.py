from playlist import *
from song import *
from user import *

class MusicPlayerSystem:
    def __init__(self):
        self.complete_list = Playlist(0, "Complete Library", self) # initial playlist created
        self.populate_complete_list() # and populated

        self.first_user = None
        self.user = None
        for i in range(1, 6):
            self.add_user(i)
        self.first_user.get_next().print_info()

    def update(self):
        pass

    def populate_complete_list(self): # import the initial list with all songs
        file = open("./data/song_list.txt", "r") #reads the text file
        content = file.read()
        song_list = content.split('\n') #splits the entire elements of each song into a list, seperated by new line operator \n
        
        for song in song_list: # use this for loop to add songs into the list
            song_element = song.split(',')
            self.complete_list.add_song(song_element[0], song_element[1], song_element[2], song_element[3], song_element[4], [song_element[5], song_element[6], song_element[7]])
            
    def add_user(self, id):
        if self.first_user == None:
            self.user = User(id, self.complete_list)
            self.first_user = self.user
        else:
            a_user = User(id, self.complete_list)
            self.user.set_next(a_user)
            self.user = a_user

    def add_song_to_library(self, userId, song):
        self.user = self.get_user(userId)
        self.user.add_song_to_library(song, self.complete_list)

    def create_playlist(self, userId, playlistName):
        pass

    def add_song_to_playlist(self, userId, playlistId, songId):
        self.user = self.get_user(userId)
        self.user.add_song_to_playlist(playlistId, songId, self.complete_list)

    def generate_suggestions(self, userId, playlistId):
        pass

    def get_most_popular_songs(self, n):
        pass

    def search_songs(self, query):
        pass

    def get_user(self, id):
        current_user = self.first_user

        while current_user != None:
            if current_user.get_id() == id:
                return current_user
            else:
                current_user = current_user.get_next()

        return None

    def get_playlist(self, id):
        return self.complete_list # implement in future

    # =============== Testing ===============
    def test_print(self):
        self.complete_list.print_list()