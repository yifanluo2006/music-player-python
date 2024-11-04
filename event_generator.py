from music_player_system import *

import threading
import random

class EventGenerator:
    def __init__(self, music_player_system):
        self.music_player_system = music_player_system
        self.interval = 30

    def update_event_generation(self):
        threading.Timer(self.interval, self.update_event_generation).start()
        print("")
        print("###################### Generating Random Event ########################")
        print("Generating random event after " + str(self.interval) + " second interval")
        self.interval = random.randint(15, 45)

        self.generate_create_playlist_event()


    def generate_create_playlist_event(self):
        userId = random.randint(1, self.music_player_system.user.get_user_num() + 1)