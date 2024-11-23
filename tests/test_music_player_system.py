import unittest
from music_player_system import *
from unittest.mock import MagicMock

# run with this: python -m unittest discover tests

class TestMusicPlayerSystem(unittest.TestCase):
    def setUp(self):
        self.mock_music_player_system = MusicPlayerSystem()
        
    def test_create_playlist_1(self):
        userId = 1
        playlistName = "Test Playlist"
        
        # Act: put the funciton you want to test here
        self.mock_music_player_system.create_playlist(userId, playlistName)
        
        # Assert: test if it works as expected
        self.assertTrue(self.mock_music_player_system.get_user(userId).get_playlist_name(playlistName) is not None)
        
    def test_create_playlist_2(self):
        userId = 100
        playlistName = "Test Playlist 2"
        
        # Act: put the funciton you want to test here
        self.mock_music_player_system.create_playlist(userId, playlistName)
        
        # Assert: test if it works as expected
        self.assertTrue(self.mock_music_player_system.get_user(userId).get_playlist_name(playlistName) is not None)
        
    def test_create_playlist_non_existent_user(self):
        userId = 1000
        playlistName = "Test Playlist 3"
        
        try:
            self.mock_music_player_system.create_playlist(userId, playlistName)
            self.assertTrue(True)
        except Exception as e:
            self.fail("Raised an exception: " + e)
            
    def test_creat_playlist_duplicate_name(self):
        userId = 100
        playlistName = "Test Playlist 4"
        
        # Act: put the funciton you want to test here
        self.mock_music_player_system.create_playlist(userId, playlistName)
        self.mock_music_player_system.create_playlist(userId, playlistName)
        
        # Assert: test if it works as expected
        count = 0
        for playlist in self.mock_music_player_system.get_user(userId).get_all_playlist():
            if playlist.get_name() == playlistName:
                count += 1
                
        self.assertEqual(1, count)
        
    def test_add_song_to_user(self):
        userId = 1
        playlistId = "00101"
        songId = "s139"
        
        self.mock_music_player_system.add_song_to_playlist(userId, playlistId, songId)
        
        self.assertTrue(self.mock_music_player_system.get_user(userId).get_library().search_song_id(songId) is not None)
        
    def test_add_song_to_non_user(self):
        userId = 1000
        playlistId = "00101"
        songId = "s139"
        
        try:
            self.mock_music_player_system.add_song_to_playlist(userId, playlistId, songId)
            self.assertTrue(True)
        except Exception as e:
            self.fail("Raised an exception: " + str(e))

    def test_add_non_song_to_user(self):
        userId = 1
        playlistId = "00101"
        songId = "s1145"
        
        try:
            self.mock_music_player_system.add_song_to_playlist(userId, playlistId, songId)
        except Exception as e:
            self.fail("Raised an exception: " + str(e))
            
    def test_get_popular_song(self):
        # adding song 25 to all users, boosting its trend
        for i in range(0, 100):
            self.mock_music_player_system.add_song_to_library(i, "s25")
        
        # the correct result should have song 25 as most popular
        self.assertTrue(self.mock_music_player_system.get_most_popular_songs(3).get_first_song().get_id())
        
    def test_gen_suggestion_for_non_user(self):
        userId = 500
        playlistId = "50000"
        
        try:
            self.mock_music_player_system.generate_suggestions(userId, playlistId)
            self.assertTrue(True)
        except Exception as e:
            self.fail("Raised an exception: " + str(e))