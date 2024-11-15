class Song:
    def __init__(self, id, title, artist, genre, bpm, meta, frequency=0, popularity_score=0.0):
        # each song is a link
        self.next = None
        
        # normal attributes
        self.id = str(id)
        self.title = str(title)
        self.artist = str(artist)
        self.genre = str(genre)
        self.bpm = int(bpm)
        self.meta = meta
        
        # similarity is used in the search funcitons
        self.similarity = 0.0
        
        # frequency and popularity is used in trend analysis
        'Note that for each addition to playlist, one frequency count is given, for an addition to a library, five frequency count is given'
        self.frequency_count = frequency
        self.popularity_score = popularity_score
    
    # common funciton to use in linked list    
    def set_next(self, next):
        self.next = next
    
    # Trend analysis code to update the frequency count and popularity score
    def update_frequency(self, n):
        self.frequency_count += n

    # updates the popularity by EMA formula
    def update_popularity(self):
        alpha = 0.35 # The alpha determines how much the value is affected by the trend
        
        # correctly initiates the score
        if self.popularity_score == 0:
            self.popularity_score = self.frequency_count
        else:
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
    
    # returns the numeric part of the id, as it starts with 's'
    def get_numeric_id(self):
        id_num = int(self.id[1:])
        return id_num
    
    def get_popularity(self):
        return self.popularity_score
    
    def get_frequency(self):
        return self.frequency_count