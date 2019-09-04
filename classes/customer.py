import pickle
import random


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.cost = 0
        self.booking = {'Booking': {}}

    def customer_data(self):
        print(f"Customer: {self.first_name} {self.last_name}")
        print(f"Price: \t {self.cost}")

        for k, v in self.booking.items():
            print(f"{k}\n")
            for i, j in v.items():
                print(f"{i} : {j}")

    def save_customer_data(self):
        customer_record_data = {'Name': f"{self.first_name} {self.last_name}",
                                'Wallet': self.cost,
                                "Booking": self.booking["Booking"]
                                }
        with open(r'./saved_data/user_data.pickle', 'wb') as f:
            pickle.dump(customer_record_data, f)

    @staticmethod
    def upload_customer_data():
        with open(r'./saved_data/user_data.pickle', 'rb') as f:
            data_new = pickle.load(f)
        return data_new

    def booking_item(self, booking_class_name, booking_item_name, booking_prefix, price, booking_class, date):
        self.cost += price
        self.booking['Booking'][
            booking_class_name] = booking_item_name
        self.booking['Booking'][
            booking_prefix] = f"{random.randrange(10, 1000)}"
        self.booking['Booking'][
            "Room class"] = booking_class
        self.booking['Booking'][
            "Reservation data"] = date
