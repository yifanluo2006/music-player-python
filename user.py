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
            print(song_id)
            current_song = complete_playlist.search_song_id(int(song_id))
            print(type(current_song))
            self.library.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
        
        playlist_num = int(user_info_list[4])
        for i in range(0, playlist_num):
            self.create_new_playlist(user_info_list[4+i*2+1])
            playlist_song_list = user_info_list[4+i*2+2].split(",")
            for song_id in playlist_song_list:
                current_song = complete_playlist.search_song_id(int(song_id))
                self.playlists[i].add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
        
    def create_new_playlist(self, name):
        new_playlist = Playlist(self.id * 10 + len(self.playlists) + 1, name, self)
        self.playlists.append(new_playlist)

    def set_next(self, next):
        self.next = next

    # ================= Accessor Methods ==================
    def get_name(self):
        return self.username