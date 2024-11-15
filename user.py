from playlist import *
import logging

class User:
    def __init__(self, id, complete_playlist, username = None, password = None):
        
        # initiates the loggers
        self.system_logger = logging.getLogger("system_logger")
        self.user_action_logger = logging.getLogger("user_action_logger")
        self.event_generation_logger = logging.getLogger("event_generation_logger")

        # each user is also a link in the linked list
        self.next = None
        self.username = username
        self.password = password

        self.id = int(id)
        
        # each user has its own unique library, with the id ending in 00
        self.library = Playlist("{0:03d}".format(self.id) + "00", "Library", self)

        # each user also has a list of playlists
        self.playlists = []
        
        # check if the username is passed in as the parameter or not to see if we are creating a NEW user or importing and EXISTING user from the text file
        if self.username is None:
            # only if the user name is None, meaning that it is importing, do we populate information
            self.populate_user_information(complete_playlist)
        self.system_logger.info("User" + str(self.id) + " " + str(self.username) + " is successfully created")
        print("")

    """ 
    Populates the user's attributes from the text file
    """
    def populate_user_information(self, complete_playlist):
        file = open("./data/user_" + str(self.id) + ".txt", "r") # reads the text file
        content = file.read()
        user_info_list = content.split('\n') # splits by new line seperator

        self.username = user_info_list[1]

        print("")
        self.system_logger.info("Importing user " + self.username + " from database")
        self.password = user_info_list[2]
        
        # splits each element more to each song id
        library_song_list = user_info_list[3].split(",")
        # adds each song into the library
        for song_id in library_song_list:
            current_song = complete_playlist.search_song_id('s' + str(song_id)) # searches for id, adds
            if current_song is not None and self.library.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta()): # adding both adds and returns whether it added successfully in boolean logic
                current_song.update_frequency(5) # updates frequency only if added successfully

        # get the number of playlists
        playlist_num = int(user_info_list[4])
        
        # for loop to iterate through each playlist data and populate all playlists
        for i in range(0, playlist_num):
            self.add_playlist(user_info_list[4+i*2+1]) # that is the name element in the .txt file
            playlist_song_list = user_info_list[4+i*2+2].split(",")
            for song_id in playlist_song_list:
                current_song = complete_playlist.search_song_id('s' + str(song_id))
                if current_song is not None and self.playlists[i].add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta()):
                    current_song.update_frequency(1)
        
        # if a playlist song is not in library, adds to library
        for playlist in self.playlists:
            current_song = playlist.get_first_song()
            
            while current_song is not None:
                self.add_song_to_library(current_song.get_id(), complete_playlist)
                current_song = current_song.get_next()
    
    # adds a song to the user's library
    def add_song_to_library(self, songID, complete_playlist):
        current_song = complete_playlist.search_song_id(songID)
        if current_song is not None and self.library.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta()):
            current_song.update_frequency(5) # reference to the song in the complete list

    # adds a song to a user's playlist
    def add_song_to_playlist(self, playlistId, songID, complete_playlist):
        current_song = complete_playlist.search_song_id(songID)
        if current_song is not None:
            for playlist in self.playlists:
                if playlist.get_id()==playlistId:
                    # adds to library in case song is not in library
                    # if it is already in, that's ok, because we always check for duplicate in the end
                    self.add_song_to_library(songID, complete_playlist)
                    if playlist.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta()):
                        current_song.update_frequency(1) # updates frequency

    # adds a new playlist with custom name
    def add_playlist(self, playlist_name):
        
        # error checking, ensuring there are no duplicates
        is_dup = False
        for playlist in self.playlists:
            if playlist.get_name() == playlist_name:
                is_dup = True
        
        # only adds if there is no duplicate
        if is_dup == False:
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
        if int(index) == 0:
            return self.library
        else:
            return self.playlists[int(index)-1]
        
    def get_password(self):
        return self.password
        
    def get_all_playlist(self):
        return self.playlists
    
    def get_library(self):
        return self.library
    
    def get_playlist_name(self, name):
        for playlist in self.playlists:
            if playlist.get_name() == name:
                return playlist
        
        return None