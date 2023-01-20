import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Thunderstruck", "ACDC")

    def test_song_has_a_name(self):
        self.assertEqual("Thunderstruck", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("ACDC", self.song.artist)
