import pickle


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.cost = 0
        self.customer_record = {'Name': f"{self.first_name} {self.last_name}",
                                'Wallet': self.cost,
                                'Booking ID': {}
                                }

    def customer_data(self):
        for k, v in self.customer_record.items():
            print(f"{k} \t {v}")

    def save_customer_data(self):
        with open(r'./saved_data/user_data.pickle', 'wb') as f:
            pickle.dump(self.customer_record, f)

    @staticmethod
    def upload_customer_data():
        with open(r'./saved_data/user_data.pickle', 'rb') as f:
            data_new = pickle.load(f)
        return data_new
