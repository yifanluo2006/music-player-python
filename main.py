from gui import *
from music_player_system import *
from event_generator import *

import logging

# Setting up logger configuration for user and event
# Setup for user action logging
user_action_logger = logging.getLogger("user_action_logger")
user_action_logger.setLevel(logging.INFO)
user_formatter = logging.Formatter('USER: %(asctime)s | %(name)s | %(levelname)s | %(message)s')

user_console_handler = logging.StreamHandler()
user_console_handler.setFormatter(user_formatter)

user_file_handler = logging.FileHandler("./logs/user_action.log")
user_file_handler.setFormatter(user_formatter)

user_action_logger.addHandler(user_console_handler)
user_action_logger.addHandler(user_file_handler)

# Setup for event generation logging
event_generation_logger = logging.getLogger("event_generation_logger")
event_generation_logger.setLevel(logging.INFO)
event_formatter = logging.Formatter('EVENT: %(asctime)s | %(name)s | %(levelname)s | %(message)s')

event_console_handler = logging.StreamHandler()
event_console_handler.setFormatter(event_formatter)

event_file_handler = logging.FileHandler("./logs/event_generation.log")
event_file_handler.setFormatter(event_formatter)

event_generation_logger.addHandler(event_console_handler)
event_generation_logger.addHandler(event_file_handler)

# Setup for system event loging
system_logger = logging.getLogger("system_logger")
system_logger.setLevel(logging.INFO)
system_formatter = logging.Formatter('SYSTEM: %(asctime)s | %(name)s | %(levelname)s | %(message)s')

system_console_handler = logging.StreamHandler()
system_console_handler.setFormatter(system_formatter)

system_file_handler = logging.FileHandler("./logs/system_event.log")
system_file_handler.setFormatter(system_formatter)

system_logger.addHandler(system_console_handler)
system_logger.addHandler(system_file_handler)

def main(): # This is the main method, this will always run as the program starts
    
    # Initialize all objects
    gui = GUI()
    music_player_system = MusicPlayerSystem()
    event_generator = EventGenerator(music_player_system)

    # Update GUI and event generator
    # event_generator.update_event_generation()
    gui.update(music_player_system)
    
    # stops event generator after GUI is closed
    event_generator.set_stop()
    
if __name__ == "__main__":
    main()