import unittest
from classes.room import *
from classes.guest import *
from classes.song import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Deluxe")
        self.room_2 = Room("Super Deluxe")
        self.room_3 = Room("Penthouse")

        self.guest_1 = Guest("Tiger Woods")
        self.guest_2 = Guest("Mark Wahlberg")
        self.guest_3 = Guest("The Rock")

        self.song_1 = Song("The Rolling Stones - Gimmie shelter")
        self.song_2 = Song("Black Sabbath - Paranoid")
        self.song_3 = Song("Foo Fighters - Everlong")

    def test_room_name(self):
        self.assertEqual("Penthouse", self.room_3.name)

    def test_guess_check_in(self):
        self.room_1.guest_check_in(self.guest_1)
        self.assertEqual(1, len(self.room_1.guests))

    def test_guess_check_out(self):
        self.room_1.guest_check_in(self.guest_1)
        self.room_1.guest_check_out(self.guest_1)
        self.assertEqual(0, len(self.room_1.guests))

    def test_room_add_song_name(self):
        self.room_1.add_songs_rooms(self.song_1)
        self.assertEqual(1, len(self.room_1.songs))

    
    


  

    


