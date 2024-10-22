from playlist import *
from song import *
from user import *

class MusicPlayerSystem:
    def __init__(self):
        self.complete_list = Playlist("00000", "Complete Library", self) # initial playlist created
        self.populate_complete_list() # and populated

        self.first_user = None
        self.user = None
        for i in range(1, 8):
            self.import_user()
        print("Total user count = " + str(self.get_user_num()))

    def populate_complete_list(self): # import the initial list with all songs
        file = open("./data/song_list.txt", "r") #reads the text file
        content = file.read()
        song_list = content.split('\n') #splits the entire elements of each song into a list, seperated by new line operator \n
        
        for song in song_list: # use this for loop to add songs into the list
            song_element = song.split(',')
            self.complete_list.add_song(song_element[0], song_element[1], song_element[2], song_element[3], song_element[4], [song_element[5], song_element[6], song_element[7]])
    
    def import_user(self):
        id = self.get_user_num() + 1
        if self.first_user is None:
            self.user = User(id, self.complete_list)
            self.first_user = self.user
        else:
            a_user = User(id, self.complete_list)
            self.user.set_next(a_user)
            self.user = a_user
            
    def add_user(self, name, password):
        id = self.get_user_num() + 1
        if self.first_user is None:
            self.user = User(id, self.complete_list, name, password)
            self.first_user = self.user
            print("Total user count = " + str(self.get_user_num()))
        else:
            a_user = User(id, self.complete_list, name, password)
            self.get_last_user().set_next(a_user)
            self.user = a_user
            print("Total user count = " + str(self.get_user_num()))
            
    def login_authentication(self, name, password):
        current_user = self.first_user
        while current_user is not None:
            if current_user.get_name() == name and current_user.get_password() == password:
                return current_user
            current_user = current_user.get_next()
        
        return None

    def add_song_to_library(self, userId, songId):
        self.user = self.get_user(userId)
        self.user.add_song_to_library(songId, self.complete_list)

    def create_playlist(self, userId, playlistName):
        self.user = self.get_user(userId)
        self.user.add_playlist(playlistName)
        print("playlist added" + str(playlistName) + str(userId))

    def add_song_to_playlist(self, userId, playlistId, songId):
        self.user = self.get_user(userId)
        self.user.add_song_to_playlist(playlistId, songId, self.complete_list)

    def delete_song_in_playlist(self, song, playlist):
        current_song = playlist.get_first_song()

        if current_song.get_id() == song.get_id():
            playlist.set_first_song(song.get_next())
            return

        while current_song is not None:
            previous_song = current_song
            current_song = current_song.get_next()
            if current_song.get_id() == song.get_id():
                previous_song.set_next(current_song.get_next)

    #************************IMPORTANT: TO BE COMPLETED*******************************
    def generate_suggestions(self, userId, playlistId):
        suggested_songs = Playlist("99979", "Suggestion", self)

        current_song = self.complete_list.get_first_song()
        for i in range (0, 5):
            suggested_songs.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
            current_song = current_song.get_next()
            
        return suggested_songs
    #*********************************************************************************

    #************************IMPORTANT: TO BE COMPLETED*******************************
    ##########################Need to implement Fuzzy Search##########################
    def get_most_popular_songs(self, n):
        popular_songs = Playlist("99989", "Top " + str(n) + " Songs", self)

        current_song = self.complete_list.get_first_song()
        for i in range (0, n):
            popular_songs.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
            current_song = current_song.get_next()

        return popular_songs
    #*********************************************************************************

    #************************IMPORTANT: TO BE COMPLETED*******************************
    def search_songs_in_playlist(self, playlist, query): # returns result in linked list
        search_result = self.search_songs_title(playlist, query)
        search_result.append(self.search_songs_artist(playlist, query))
        search_result.append(self.search_songs_genre(playlist, query))
        search_result.append(self.search_songs_meta(playlist, query))
        return search_result
    #*********************************************************************************

    def search_songs_in_library(self, user, query): # searches in library
        search_result = self.search_songs_in_playlist(user.get_library(), query)
        return search_result

    def search_songs(self, query): # searches in complete list (entire collection)
        search_result = self.search_songs_in_playlist(self.complete_list, query)
        return search_result

    def search_songs_title(self, playlist, query): # searches by title, used by other search functions
        search_result = playlist.search_song_title(query)
        return search_result

    def search_songs_artist(self, playlist, query): # searches by artist, used by other search functions
        search_result = playlist.search_song_artist(query)
        return search_result

    def search_songs_genre(self, playlist, query): # searches by genre, used by other search functions
        search_result = playlist.search_song_genre(query)
        return search_result
    
    def search_songs_meta(self, playlist, query): #searches b meta tags, used by other search functions
        search_result = playlist.search_song_meta(query)
        return search_result
    # ================= Accessor Methods =======================
    def get_user(self, id):
        current_user = self.first_user

        while current_user != None:
            if current_user.get_id() == int(id):
                return current_user
            else:
                current_user = current_user.get_next()

        return None

    def get_playlist(self, id):
        if int(id[0:3]) == 0:
            return self.complete_list
        else:
            self.user = self.get_user(int(id[0:3]))
            self.user.get_playlist(id)

    def get_user_num(self):
        num = 0
        user = self.first_user
        while user is not None:
            num+=1
            user = user.get_next()
            
        return num
    
    def get_last_user(self):
        
        user = self.first_user
        while user.get_next() is not None:
            user = user.get_next()
            
        return user
        
    # =============== Testing ===============
    def test_print(self):
        self.complete_list.print_list()