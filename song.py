class Song:
    def __init__(self, id, title, artist, genre, bpm, meta):
        self.next = None
        
        self.id = str(id)
        self.title = str(title)
        self.artist = str(artist)
        self.genre = str(genre)
        self.bpm = int(bpm)
        self.meta = meta
        
    def set_next(self, next):
        self.next = next
    
    # Trend analysis code to update the frequency count and popularity score
    def update_frequency(self, n):
        self.frequency_count += n

    def update_popularity(self):
        
        alpha = 0.35 # The alpha determines how much the value is affected by the trend
        self.popularity_score = (self.frequency_count * alpha) + (self.popularity_score * (1-alpha))

    def update_similarity(self, n):
        self.similarity = n
    
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
    
    def get_meta(self):
        return self.meta
    
    def get_numeric_id(self):
        id_num = int(self.id[1:])
        return id_num
    
    def get_popularity(self):
        return self.popularity_score
    
    def get_frequency(self):
        return self.frequency_count

    # ================ Testing ==================== 
    # def print_all(self): # this is a test method that prints the attributes of the current song and calls the next one to print
    #     self.print_attributes()
    #     if self.next != None:
    #         self.next.print_all()
    
    # def print_attributes(self):
    #     print(self.id, self.title, self.artist, self.genre, self.bpm, self.meta)