import pickle
import random
import json
from datetime import datetime


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

    def save_customer_data_json(self):
        booking_id = datetime.timestamp(datetime.now())
        customer_book_data_json = {
            f"Booking ID {int(booking_id)}": {
                "Name": f"{self.first_name} {self.last_name}",
                "Wallet": f"{self.total_price}",
                "Booking": self.booking
            }
        }
        with open(r"./saved_data/user_data.json", 'r') as f:
            config = json.load(f)
        config["booking"].append(customer_book_data_json)
        with open(r"./saved_data/user_data.json", 'w') as f:
            json.dump(config, f)

    @staticmethod
    def delete_customer_data_json():
        with open(r"./saved_data/user_data.json", 'r') as f:
            config = json.load(f)
            config["booking"] = []

        with open(r"./saved_data/user_data.json", 'w') as f:
            json.dump(config, f)

    def get_order_summary(self):
        ...
