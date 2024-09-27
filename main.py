from gui import *
from music_player_system import *

def main():
    gui = GUI()
    music_player_system = MusicPlayerSystem()
    music_player_system.update()
    gui.update()

if __name__ == "__main__":
    main()