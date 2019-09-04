from .bookable import Bookable


class Hotel(Bookable):
    CLASS_PENTHOUSE = 'Penthouse'
    CLASS_KING_DELUXE = 'King Deluxe Bedroom'
    CLASS_QUEEN_DELUXE = 'Queen Deluxe Bedroom'
    CLASS_KING_STANDARD = 'Kind Standard Bedroom'
    CLASS_QUEEN_STANDARD = 'Queen Standard Bedroom'

    def __init__(self, hotel_name):
        super(Hotel, self).__init__()
        self.hotel_name = hotel_name
        self.HOTEL_ROOM = {self.CLASS_PENTHOUSE: 10,
                           self.CLASS_KING_DELUXE: 20,
                           self.CLASS_QUEEN_DELUXE: 20,
                           self.CLASS_KING_STANDARD: 30,
                           self.CLASS_QUEEN_STANDARD: 50

                           }
        self.HOTEL_PRICE = {self.CLASS_PENTHOUSE: 1000,
                            self.CLASS_KING_DELUXE: 700,
                            self.CLASS_QUEEN_DELUXE: 600,
                            self.CLASS_KING_STANDARD: 450,
                            self.CLASS_QUEEN_STANDARD: 350
                            }

    def get_items(self, booking_class):
        return self.HOTEL_ROOM[booking_class]

    def get_name(self):
        return self.hotel_name

    def decrement_items(self, booking_class):
        self.HOTEL_ROOM[booking_class] -= 1

    def get_id_prefix(self):
        return 'Room'

    def get_price(self, booking_class):
        return self.HOTEL_PRICE[booking_class]
