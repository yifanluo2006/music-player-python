from playlist import *
from song import *
from user import *

class MusicPlayerSystem:
    def __init__(self):
        self.complete_list = Playlist(0, "Complete Library", self) # initial playlist created
        self.populate_complete_list() # and populated

        self.first_user = None
        self.user = None
        self.add_user(1)
        self.first_user.print_info()

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

    def get_user(self, id):
        return self.first_user # implement a search function in the future for the id number
    
    def get_playlist(self, id):
        return self.complete_list # implement in future

    def add_song_to_library(userId, song):
        pass

    def create_playlist(userId, playlistName):
        pass

    def add_song_to_playlist(userId, playlistId, songId):
        pass

    def generate_suggestions(userId, playlistId):
        pass

    def get_most_popular_songs(n):
        pass

    def search_songs(query):
        pass

    # =============== Testing ===============
    def test_print(self):
        self.complete_list.print_list()