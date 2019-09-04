import random
import datetime
from classes.customer import Customer


class Bookable(object):
    def is_available(self, booking_class):
        return self.get_items(booking_class) > 0

    def make_reservation(self, customer, booking_class, date):
        if self.user_coming_data(date):
            if self.is_available(booking_class):
                self.decrement_items(booking_class)
                customer.booking_item(booking_class_name=self.get_class_name(), booking_item_name=self.get_name(),
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
    def user_coming_data(date):
        temp_date = [int(i) for i in date.split(" ")]
        date = datetime.date(*temp_date)

        if date > datetime.date.today():
            return date
        else:
            print("Invalid date, too early, sorry")
