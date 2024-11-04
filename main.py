from gui import *
from music_player_system import *
from event_generator import *

def main(): # This is the main method, this will always run as the program starts
    
    # Initialize all objects
    gui = GUI()
    music_player_system = MusicPlayerSystem()
    event_generator = EventGenerator(music_player_system)

    # Update GUI and event generator
    event_generator.update_event_generation()
    gui.update(music_player_system)
    
    # stops event generator after GUI is closed
    event_generator.set_stop()
    

if __name__ == "__main__":
    main()