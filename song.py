class Song:
    def __init__(self, id, title, artist, genre, bpm, meta):
        self.next = None
        
        self.id = id
        self.title = title
        self.artist = artist
        self.genre = genre
        self.bpm = bpm
        self.meta = meta

    def set_next(self, next):
        self.next = next
        
    def print_all(self): # this is a test method that prints the attributes of the current song and calls the next one to print
        self.print_attributes()
        if self.next != None:
            self.next.print_all()
    
    def print_attributes(self):
        print(self.id, self.title, self.artist, self.genre, self.bpm, self.meta)