import unittest
from music_player_system import *
from unittest.mock import MagicMock

# run with this: python -m unittest discover tests

class TestMusicPlayerSystem(unittest.TestCase):
    def setUp(self):
        self.mock_music_player_system = MagicMock(spec=MusicPlayerSystem)
        
    def test_create_playlist(self):
        userId = 1
        playlistName = "Test Playlist"
        
        # Act: put the funciton you want to test here
        self.mock_music_player_system.create_playlist(userId, playlistName)
        
        # Assert: test if it works as expected
        self.assertTrue(self.mock_music_player_system.get_user(userId).get_playlist_name() is not None)