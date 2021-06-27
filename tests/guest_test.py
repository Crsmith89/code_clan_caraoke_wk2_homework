import unittest
from classes.guest import *


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Tiger Woods")
        self.guest_2 = Guest("Mark Wahlberg")
        self.guest_3 = Guest("The Rock")

      
    def test_guest_name(self):
        self.assertEqual("Tiger Woods", self.guest_1.name)
        

