from playlist import *

class User:
    def __init__(self, id, complete_playlist):
        self.next = None
        self.username = None
        self.password = None

        self.id = int(id)
        self.library = Playlist("{0:03d}".format(self.id) + "00", "Library", self)

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
            current_song = complete_playlist.search_song_id(int(song_id))
            self.library.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
        
        playlist_num = int(user_info_list[4])
        for i in range(0, playlist_num):
            self.add_playlist(user_info_list[4+i*2+1]) # that is the name element in the .txt file
            playlist_song_list = user_info_list[4+i*2+2].split(",")
            for song_id in playlist_song_list:
                current_song = complete_playlist.search_song_id(int(song_id))
                self.playlists[i].add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())

    def add_song_to_library(self, songID, complete_playlist):
        current_song = complete_playlist.search_song_id(songID)
        if self.library.search_song_id(songID) == None:
            self.library.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())

    def add_song_to_playlist(self, playlistId, songID, complete_playlist):
        current_song = complete_playlist.search_song_id(songID)
        for playlist in self.playlists:
            if playlist.get_id == playlistId and playlist.search_song_id(songID) == None:
                playlist.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
                self.add_song_to_library(songID, complete_playlist)

    def add_playlist(self, playlist_name):
        p = Playlist("{0:03d}".format(self.id) + "{0:02d}".format(len(self.playlists) + 1), playlist_name, self)
        self.playlists.append(p)

    def set_next(self, next):
        self.next = next

    # ================= Accessor Methods ==================
    def get_name(self):
        return self.username
    
    def get_next(self):
        return self.next
    
    def get_id(self):
        return self.id
    
    def get_playlist(self, index):
        if index == 0:
            return self.library
        else:
            return self.playlists[index-1]
    
    # ================= Testing ===================
    def print_info(self):
        print(self.id)
        print(self.username)
        print(self.password)
        print(self.library.print_list())
        for playlist in self.playlists:
            print(playlist.name)
            print(playlist.print_list())