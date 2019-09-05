import random
import datetime


class Bookable:
    def is_available(self, booking_class):
        return self.get_items(booking_class) > 0

    def make_reservation(self, customer, booking_class, date):
        if self.checking_user_coming_data(date):
            if self.is_available(booking_class):
                self.decrement_items(booking_class)
                customer.book_item(booking_class_name=self.get_class_name(), booking_item_name=self.get_name(),
                                   booking_prefix=self.get_id_prefix(), price=self.get_price(booking_class),
                                   booking_class=booking_class, date=date)

    def get_class_name(self):
        return self.__class__.__name__

    def get_name(self):
        raise NotImplementedError

    def get_items(self, booking_class):
        raise NotImplementedError

    def get_price(self, booking_class):
        raise NotImplementedError

    def decrement_items(self, booking_class):
        raise NotImplementedError

    def get_id_prefix(self):
        raise NotImplementedError

    @staticmethod
    def checking_user_coming_data(date):
        if datetime.date(*[int(i) for i in date.split(" ")]) > datetime.date.today():
            return date
        else:
            print("Invalid date, too early, sorry")
