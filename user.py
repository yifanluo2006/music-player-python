from playlist import *

class User:
    def __init__(self, id, complete_playlist, username = None, password = None):
        
        self.next = None
        self.username = username
        self.password = password

        self.id = int(id)
        self.library = Playlist("{0:03d}".format(self.id) + "00", "Library", self)

        self.playlists = []
        if self.username is None:
            self.populate_user_information(complete_playlist)
        print("User" + str(self.id) + " " + str(self.username) + " is successfully created")
        print("")
        print("")

    def populate_user_information(self, complete_playlist):
        file = open("./data/user_" + str(self.id) + ".txt", "r") #reads the text file
        content = file.read()
        user_info_list = content.split('\n')

        self.username = user_info_list[1]
        print("================== Importing User " + self.username + " ================")
        self.password = user_info_list[2]
        
        playlist_num = int(user_info_list[3])
        for i in range(0, playlist_num):
            self.add_playlist(user_info_list[3+i*2+1]) # that is the name element in the .txt file
            playlist_song_list = user_info_list[3+i*2+2].split(",")
            for song_id in playlist_song_list:
                current_song = complete_playlist.search_song_id('s' + str(song_id))
                self.playlists[i].add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
        
        for playlist in self.playlists:
            current_song = playlist.get_first_song()
            
            while current_song is not None:
                self.add_song_to_library(current_song.get_id(), complete_playlist)
                current_song = current_song.get_next()
        
    def add_song_to_library(self, songID, complete_playlist):
        current_song = complete_playlist.search_song_id(songID)
        current_song.update_frequency(1) # reference to the song in the complete list
        self.library.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
        print(current_song.get_title() + " is added to " + self.username + "'s library")

    def add_song_to_playlist(self, playlistId, songID, complete_playlist):
        current_song = complete_playlist.search_song_id(songID)
        for playlist in self.playlists:
            if playlist.get_id()==playlistId:
                self.add_song_to_library(songID, complete_playlist)
                playlist.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
                print(current_song.get_title() + " is added to " + self.username + "'s playlist " + playlist.get_name())

    def add_playlist(self, playlist_name):
        p = Playlist("{0:03d}".format(self.id) + "{0:02d}".format(len(self.playlists) + 1), playlist_name, self)
        self.playlists.append(p)
        print("New playlist " + playlist_name + " is created")

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
        
    def get_password(self):
        return self.password
        
    def get_all_playlist(self):
        return self.playlists
    
    def get_library(self):
        return self.library
    
    # ================= Testing ===================
    def print_info(self):
        print(self.id)
        print(self.username)
        print(self.password)
        print(self.library.print_list())
        for playlist in self.playlists:
            print(playlist.name)
            print(playlist.print_list())