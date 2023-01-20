import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.group_1 = Guest("group_1", "Thunderstruck", 100.00)

    def test_group_has_a_name(self):
        self.assertEqual("group_1", self.group_1.group)

    def test_group_has_favourite_song(self):
        self.assertEqual("Thunderstruck", self.group_1.fav_song)

    def test_group_wallet(self):
        self.assertEqual(100.00, self.group_1.wallet)

    def test_pay_bill_for_room(self):
        self.group_1.pay_bill(10.00)
        self.assertEqual(90.00, self.group_1.wallet)
