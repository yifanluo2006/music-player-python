from playlist import *
from song import *

class MusicPlayerSystem:
    def __init__(self):
        self.complete_list = Playlist()
        self.populate_complete_list()

    def update(self):
        pass

    def populate_complete_list(self):
        file = open("./data/song_list.txt", "r")
        content = file.read()
        print(content)
        # self.complete_list.add_song()