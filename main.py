from gui import *
from music_player_system import *

def main(): # This is the main method, this will always run as the program starts
    
    #The reason this is done is because of OOP Principles, in which we let each class handle itself
    gui = GUI()
    music_player_system = MusicPlayerSystem()
    
    # music_player_system.test_print() # test to verify it works, and it does
    gui.update(music_player_system)

if __name__ == "__main__":
    main()