from playlist import *

class User:
    def __init__(self, id, complete_playlist):
        self.next = None
        self.username = None
        self.password = None

        self.id = id
        self.library = Playlist(self.id * 10 + 0, "Library", self)
        self.playlists = []
        self.populate_user_information(complete_playlist)

    def populate_user_information(self, complete_playlist):
        file = open("./data/user_" + str(self.id) + ".txt", "r") #reads the text file
        content = file.read()
        user_info_list = content.split('\n')

        self.username = user_info_list[1]
        self.password = user_info_list[2]
        library_songs = user_info_list[3].split(",")
        for song_id in library_songs:
            self.library.add_song(complete_playlist.search_song_id(song_id))
        # print(user_list)
        
    def create_new_playlist(self, name):
        new_playlist = Playlist(self.id * 10 + len(self.playlists) + 1, name, self)
        self.playlists.append(new_playlist)

    def set_next(self, next):
        self.next = next

    def get_name(self):
        return self.username