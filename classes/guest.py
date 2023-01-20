class Guest:
    def __init__(self, group, fav_song, wallet):
        self.group = group
        self.fav_song = fav_song
        self.wallet = wallet

    def pay_bill(self, amount):
        self.wallet -= amount