from music_player_system import *
from user import *

import threading
import random

class EventGenerator:
    def __init__(self, music_player_system):
        self.music_player_system = music_player_system
        self.interval = 30
        self.running = True

    def update_event_generation(self):
        if self.running:
            # I am using the threading library to repeatedly call this funciton at regular intervals
            threading.Timer(self.interval, self.update_event_generation).start()
            
            print("")
            print("")
            print("###################### Generating Random Event ########################")
            print("Generating this random event after a " + str(self.interval) + " second interval")
            # time interval until the next one
            self.interval = random.randint(15, 45)
            
            # the number of events (users) to be generated during this event
            event_num = random.randint(3, 5)
            
            # each event in an user
            for i in range(0, event_num):
                # getting a random user
                event_user_id = self.get_random_user()
                
                print("")
                print("================= Event for User " + str(event_user_id) + " " + self.music_player_system.get_user(event_user_id).get_name() + "==================")
                
                # create a random number of new playlist
                for i in range(0, random.randint(0, 2)):
                    self.generate_create_playlist_event(event_user_id)
               
                # mandatory event of adding random number of suggested songs to library
                self.generate_add_suggested_song_library_event(event_user_id)
                
                # ask for suggestions for a random number of playlists and add random number of songs from these suggestions
                for i in range(0, random.randint(0, 3)):
                    self.generate_add_suggested_song_playlist_event(event_user_id)
                
                # adds random number of random songs into a random playlist of the user
                for i in range(0, random.randint(0, 5)):
                    self.generate_add_random_song_event(event_user_id)
                
                # half chance to add trending songs
                if random.randint(0, 1) == 1:
                    self.generate_add_trending_song_event(event_user_id)
                    
                # deletes random number of random songs
                for i in range(0, random.randint(0, 2)):
                    self.generate_delete_random_song_event(event_user_id)
            
            print("Next random event will be generated after a " + str(self.interval) + " second interval")
            print("###################### Random Event Completed ########################")
            print("")
            print("")

    def set_stop(self):
        self.running = False
    
    def get_random_user(self):
        random_user_id = random.randint(1, self.music_player_system.get_user_num())
        return random_user_id
    
    def get_random_playlist(self, event_user_id):
        playlist_num = len(self.music_player_system.get_user(event_user_id).get_all_playlist())
        playlist_id = random.choice(self.music_player_system.get_user(event_user_id).get_all_playlist()).get_id()
        return playlist_id

    def generate_create_playlist_event(self, event_user_id):
        # creates a new playlist by random name from the word bank
        words_1 = ["Rhythmic", "Funky", "Raw", "Blissful", "Hypnotic", "Energetic", "Radiant", "Soothing", "Edgy", "Lively", "Cosmic", "Classic", "Chill", "Epic", "Dreamy", "Smooth", "Serene"]
        words_2 = ["Vibes", "Beats", "Atmospheres", "Journey", "Chronicles", "Essentials", "Flow", "Mood", "Pulse", "Tunes", "Collection", "Hits", "Sounds"]
        playlist_name = random.choice(words_1) + " " + random.choice(words_2)
        self.music_player_system.create_playlist(event_user_id, playlist_name)
        playlist_id = self.music_player_system.get_user(event_user_id).get_all_playlist()[-1].get_id()
        
        # by default adds a random number of random songs from the library to the newly created playlist
        for i in (0, random.randint(5, 8)):
            song_id = self.music_player_system.get_user(event_user_id).get_library().get_index_song(random.randint(0, self.music_player_system.get_user(event_user_id).get_library().get_len()-1)).get_id()
            self.music_player_system.add_song_to_playlist(event_user_id, playlist_id, song_id)
    
    def generate_add_suggested_song_library_event(self, event_user_id):
        library_id = self.music_player_system.get_user(event_user_id).get_library().get_id()
        #asks for suggestions
        library_suggestions = self.music_player_system.generate_suggestions(event_user_id, library_id)
        
        # take random number of suggestions
        # error handling: if all suggestions are used up
        if library_suggestions.get_len() > 0:
            suggestion_num = random.randint(1, library_suggestions.get_len())
        else:
            library_suggestions = 0
            return
        
        current_song = library_suggestions.get_first_song()
        # adds suggestions to library
        while suggestion_num > 0:
            self.music_player_system.add_song_to_library(event_user_id, current_song.get_id())
            current_song = current_song.get_next()
            suggestion_num -= 1
            
    def generate_add_suggested_song_playlist_event(self, event_user_id):
        # get a random playlist the user owns
        playlist_id = self.get_random_playlist(event_user_id)
        
        # the following steps are similar to the previous function(generate_add_suggested_song_library_event)
        playlist_suggestions = self.music_player_system.generate_suggestions(event_user_id, playlist_id)
        
        # take random number of suggestions
        suggestion_num = random.randint(1, playlist_suggestions.get_len())
        
        current_song = playlist_suggestions.get_first_song()
        # adds suggestions to playlist
        while suggestion_num > 0:
            self.music_player_system.add_song_to_playlist(event_user_id, playlist_id, current_song.get_id())
            current_song = current_song.get_next()
            suggestion_num -= 1
        
    def generate_add_random_song_event(self, event_user_id):
        # finds a random song in complete list and adds it to a random playlist
        song_index = random.randint(1, 1000)
        self.music_player_system.get_complete_list().get_index_song(song_index)
        playlist_id = self.get_random_playlist(event_user_id)
        self.music_player_system.add_song_to_playlist(event_user_id, playlist_id, "s" + str(song_index))
        
    def generate_add_trending_song_event(self, event_user_id):
        # requests for trending songs and adds to library
        popular_songs = self.music_player_system.get_most_popular_songs(3)
        self.music_player_system.get_user(event_user_id).get_library().append(popular_songs)
    
    def generate_delete_random_song_event(self, event_user_id):
        # gets random song in library and deletes the song
        library = self.music_player_system.get_user(event_user_id).get_library()
        song = library.get_index_song(random.randint(0, library.get_len() - 1))
        self.music_player_system.delete_song_in_playlist(song, library)