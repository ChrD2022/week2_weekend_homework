import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Room 1", 10.00, 50.00)
        self.guest_1 = Guest("CdeClnG", "Thunderstruck", 100.00)
        self.guest_2 = Guest("CdeClnE", "Shoot to Thrill", 5.00)
        self.song_1 = Song("Thunderstruck", "ACDC")
        self.song_2 = Song("Shoot to Thrill", "ACDC")

    def test_room_has_an_id(self):
        self.assertEqual("Room 1", self.room_1.room_number)

    def test_roon_has_a_price_set(self):
        self.assertEqual(10, self.room_1.room_price)

    def test_room_is_available(self):
        self.assertEqual(True, Room.room_available(self.room_1))

    def test_room_occupied(self):
        self.room_1.room_guests = ["group_1"]
        self.assertEqual("Room is occupied.", Room.room_available(self.room_1))
    
    def test_able_to_checkin(self):
        self.room_1.check_in(self.room_1, self.guest_1)
        self.assertEqual(True, Room.room_available(self.room_1))

    def test_room_not_affordable(self):
        self.room_1.check_in(self.room_1, self.guest_2)
        self.assertEqual("You don't have enough money to book sorry.", self.room_1.check_in(self.room_1, self.guest_2))
        self.assertEqual(5.00, self.guest_2.wallet)
        self.assertEqual(True, Room.room_available(self.room_1))

    def test_room_checkout(self):
        self.room_1.check_out()
        self.assertEqual(True, Room.room_available(self.room_1))

    def test_hire_room(self):
        self.room_1.check_in(self.room_1, self.guest_1)
        self.assertEqual(90.00, self.guest_1.wallet)
        self.assertEqual(60.00, self.room_1.room_till)

    def test_add_to_song_list(self):
        self.room_1.add_to_catalogue(self.song_1)
        self.room_1.add_to_catalogue(self.song_2)
        self.assertEqual(2, len(self.room_1.room_catalogue))

    def test_fav_song_response(self):
        self.room_1.check_in(self.room_1, self.guest_1)
        self.room_1.add_to_catalogue(self.song_1)
        self.assertEqual("Woo Hoo!!!", self.room_1.fav_song(self.guest_1))
        self.assertEqual("Rock on!!!", self.room_1.fav_song(self.guest_2))