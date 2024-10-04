class Song:
    def __init__(self, id, title, artist, genre, bpm, meta):
        self.next = None
        
        self.id = int(id)
        self.title = title
        self.artist = artist
        self.genre = genre
        self.bpm = int(bpm)
        self.meta = meta

    def set_next(self, next):
        self.next = next
    
    # ================ Accessor Methods ===============

    def get_id(self):
        return self.id
    
    def get_next(self):
        return self.next
    
    def get_title(self):
        return self.title

    # ================ Testing ==================== 
    def print_all(self): # this is a test method that prints the attributes of the current song and calls the next one to print
        self.print_attributes()
        if self.next != None:
            self.next.print_all()
    
    def print_attributes(self):
        print(self.id, self.title, self.artist, self.genre, self.bpm, self.meta)