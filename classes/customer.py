import pickle
import random


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.total_price = 0
        self.booking = []

    def show_customer_booked_item(self):
        print(f"Customer: {self.first_name} {self.last_name}")
        print(f"Price: \t {self.total_price}")
        print("Booking")
        for k, v in self.booking:
            print(f"{k} : {v}")

    def save_customer_data(self):
        customer_book_data = {'Name': f"{self.first_name} {self.last_name}",
                              'Wallet': self.total_price,
                              "Booking": self.booking
                              }
        with open(r'./saved_data/user_data.pickle', 'wb') as f:
            pickle.dump(customer_book_data, f)

    @staticmethod
    def upload_customer_data():
        with open(r'./saved_data/user_data.pickle', 'rb') as f:
            data_new = pickle.load(f)
        return data_new

    def book_item(self, booking_class_name, booking_item_name, booking_prefix, price, booking_class, date):
        self.total_price += price
        self.booking.extend([(booking_class_name, booking_item_name), (booking_prefix, f"{random.randrange(10, 1000)}"),
                             ("Room class", booking_class), ("Reservation data", date)])
