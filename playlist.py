from song import *

class Playlist:
    def __init__(self, id, name, owner):
        self.name = str(name)
        self.first_song = None
        self.song = None
        self.owner = owner

        """
        The ID to keep track of the playlist will be formated as the following 5-digit string:
        * * * _ _ First 3 digits will be the user ID, with with 0 as placeholders if the ID is single or double digit
        _ _ _ * * The fourth and fift digit will be the playlist number owned by the user, in the sequence they were created
        with 00 as the library playlist, 1 as the first, 2 as the second ...
        The 00000 playlist will be the complete playlist of all songs
        """
        
        self.id = str(id)

    def add_song(self, id, title, artist, genre, bpm, meta):
        if not self.is_duplicate(str(id)):
            if self.first_song is None: #if this is first song
                self.song = Song(id, title, artist, genre, bpm, meta)
                self.first_song = self.song
            else: # if there is already first song
                a_song = Song(id, title, artist, genre, bpm, meta)
                self.song.set_next(a_song) # "linking" the list
                self.song = a_song

    def is_duplicate(self, id): # check for any duplicate in the current playlist
        current_song = self.first_song
        while current_song is not None:
            if current_song.get_id() == id:
                return True
            current_song = current_song.get_next()

        return False

    def search_song_title(self, query):
        search_result = Playlist("99990", "Search Result", self)
        current_song = self.first_song
        while current_song is not None:
            if query.lower() in current_song.get_title().lower():
                search_result.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
            current_song = current_song.get_next()

        return search_result
    
    def search_song_artist(self, query):
        search_result = Playlist("99991", "Search Result", self)
        current_song = self.first_song
        while current_song is not None:
            if query.lower() in current_song.get_artist().lower():
                search_result.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
            current_song = current_song.get_next()

        return search_result
    
    def search_song_genre(self, query):
        search_result = Playlist("99992", "Search Result", self)
        current_song = self.first_song
        while current_song is not None:
            if query.lower() in current_song.get_genre().lower():
                search_result.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
            current_song = current_song.get_next()

        return search_result
    
    def search_song_meta(self, query): # since the user cannot see meta, the meta has to exactly match to be searched
        search_result = Playlist("99993", "Search Result", self)
        current_song = self.first_song
        while current_song is not None:
            meta_lst = current_song.get_meta()
            for meta in meta_lst:
                if query.lower()==meta.lower():
                    print(query, meta)
                    search_result.add_song(current_song.get_id(), current_song.get_title(), current_song.get_artist(), current_song.get_genre(), current_song.get_bpm(), current_song.get_meta())
                    break
            current_song = current_song.get_next()

        return search_result

    def search_song_id(self, id):
        current_song = self.first_song

        while current_song is not None:
            if current_song.get_id() == id:
                return current_song
            else:
                current_song = current_song.get_next()
        return None
    
    def append(self, playlist):
        self.song = self.get_last_song()
        
        if self.song is not None and playlist.get_first_song() is not None:
            self.song.set_next(playlist.get_first_song())
        elif self.song is None and playlist.get_first_song() is not None:
            self.first_song = playlist.get_first_song()
    
    def set_first_song(self, new_first_song):
        self.first_song = new_first_song
        
    # =============== Accessor Methods ==============
    def get_id(self):
        return self.id

    def get_first_song(self):
        return self.first_song
    
    def get_last_song(self):
        self.song = self.first_song
        
        if self.song is not None:
            while self.song.get_next() is not None:
                self.song = self.song.get_next()
        
        return self.song
    
    def slice(self, end):
        self.song = self.first_song
        for i in range(0, end-1):
            self.song = self.song.get_next()

        self.song.set_next(None)
        
    # ============== Testing ===============
    def print_list(self): #print list for testing purposes
        self.first_song.print_all()