from playlist import *
from song import *
from user import *

class MusicPlayerSystem:
    def __init__(self):
        self.complete_list = Playlist(0, "Complete Library") # initial playlist created
        self.populate_complete_list() # and populated

        self.first_user = None
        self.user = None
        self.populate_users(1)

    def update(self):
        pass

    def populate_complete_list(self): # import the initial list with all songs
        file = open("./data/song_list.txt", "r") #reads the text file
        content = file.read()
        song_list = content.split('\n') #splits the entire elements of each song into a list, seperated by new line operator \n
        
        for song in song_list: # use this for loop to add songs into the list
            song_element = song.split(',')
            self.complete_list.add_song(song_element[0], song_element[1], song_element[2], song_element[3], song_element[4], [song_element[5], song_element[6], song_element[7]])
            
    def populate_users(self, id):
        if self.first_user == None:
            self.user = User(id)
            self.first_user = self.user
        else:
            a_user = User(id)
            self.user.set_next(a_user)
            self.user = a_user

    def get_user(self, id):
        return self.first_user # implement a search function in the future for the id number

    def test_print(self):
        self.complete_list.print_list()