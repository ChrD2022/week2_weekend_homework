class Room:
    def __init__(self, number, price, till):
        self.room_number = number
        self.room_price = price
        self.room_till = till
        self.room_guests = []
        self.room_catalogue = []

    def room_available(self):
        if len(self.room_guests) == 0:
            return True
        else:
            return "Room is occupied."

    def check_out(self):
        self.room_guests.clear()
    
    def add_to_catalogue(self, song):
        self.room_catalogue.append(song)

    def check_in(self, room, guest):
        for guest in self.room_guests:
            if self.room_available(room) == True:
                self.room_guests.append(guest)            
        if guest.wallet >= self.room_price:
            guest.wallet -= self.room_price
            self.room_till += self.room_price
        else:
            return "You don't have enough money to book sorry."


    def fav_song(self, guest):
        for song in self.room_catalogue:
            if song.title == guest.fav_song:
                return "Woo Hoo!!!"
            else:
                return "Rock on!!!"