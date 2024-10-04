class Song:
    def __init__(self, id, title, artist, genre, bpm, meta):
        self.next = None
        
        self.id = int(id)
        self.title = str(title)
        self.artist = str(artist)
        self.genre = str(genre)
        self.bpm = int(bpm)
        self.meta = meta

    def set_next(self, next):
        self.next = next
    
    # ================ Accessor Methods ===============

    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.title
    
    def get_artist(self):
        return self.artist
    
    def get_genre(self):
        return self.genre
    
    def get_bpm(self):
        return self.bpm
    
    def get_meta(self):
        return self.meta
    
    def get_next(self):
        return self.next

    # ================ Testing ==================== 
    def print_all(self): # this is a test method that prints the attributes of the current song and calls the next one to print
        self.print_attributes()
        if self.next != None:
            self.next.print_all()
    
    def print_attributes(self):
        print(self.id, self.title, self.artist, self.genre, self.bpm, self.meta)