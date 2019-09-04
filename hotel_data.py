import pickle

hotel_list = [{'Spa resort1': {"booking_class": {
    1: 'Penthouse',
    2: 'King Deluxe Bedroom',
    3: 'Queen Deluxe Bedroom1',
    4: 'Kind Standard Bedroom',
    5: 'Queen Standard Bedroom'}}},
    {'Spa resort2': {"booking_class": {
        1: 'Penthouse',
        2: 'King Deluxe Bedroom',
        3: 'Queen Deluxe Bedroom',
        4: 'Kind Standard Bedroom',
        5: 'Queen Standard Bedroom'}}},
    {'Spa resort3': {"booking_class": {
        1: 'Penthouse',
        2: 'King Deluxe Bedroom',
        3: 'Queen Deluxe Bedroom',
        4: 'Kind Standard Bedroom',
        5: 'Queen Standard Bedroom'}}},
    {'Spa resort4': {"booking_class": {
        1: 'Penthouse',
        2: 'King Deluxe Bedroom',
        3: 'Queen Deluxe Bedroom',
        4: 'Kind Standard Bedroom',
        5: 'Queen Standard Bedroom'}}},
    {'Spa resort5': {"booking_class": {
        1: 'Penthouse',
        2: 'King Deluxe Bedroom',
        3: 'Queen Deluxe Bedroom',
        4: 'Kind Standard Bedroom',
        5: 'Queen Standard Bedroom'}}}
]


def save_hotel_data():
    with open(r'./saved_data/hotel_data.pickle', 'wb') as f:
        pickle.dump(hotel_list, f)


def upload_hotel_data():
    with open(r'./saved_data/hotel_data.pickle', 'rb') as f:
        data_new = pickle.load(f)
    return data_new


save_hotel_data()
