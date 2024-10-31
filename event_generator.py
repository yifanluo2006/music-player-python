from music_player_system import *

import time

class EventGenerator:
    def __init__(self, music_player_system):
        pass

    def update_event_generation(self):
        print("running event generator")
        start = time.time()

        if time.time() - start > 1:
            self.update_event_generation()

    def generate_create_playlist_event(self):
        pass