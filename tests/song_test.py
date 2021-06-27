import unittest
# from classes.guest import Guest
# from classes.room import Room
from classes.song import Song

class TestSong(unittest.TestCase):

     def setUp(self):
        self.song_1 = Song("The Rolling Stones - Gimmie shelter")
        self.song_2 = Song("Black Sabbath - Paranoid")
        self.song_3 = Song("Foo Fighters - Everlong")

     def test_play_song(self):
        self.assertEqual("The Rolling Stones - Gimmie shelter", self.song_1.name)
        self.assertEqual("Black Sabbath - Paranoid", self.song_2.name)
        self.assertEqual("Foo Fighters - Everlong", self.song_3.name)

    



