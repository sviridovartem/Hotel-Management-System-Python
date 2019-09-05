from classes.customer import Customer
from classes.hotel import Hotel
import hotel_data


class InputExeptionError(Exception):
    def __init__(self, text, num):
        self.txt = text
        self.n = num


hotel_list = hotel_data.upload_hotel_data()

hotel_for_choose = []
i = 1
for hotel in hotel_list:
    for (k, v) in hotel.items():
        hotel_for_choose.append((i, k))
        i += 1

# user dialog

# print("Enter your first and last name")
# input_names = input().split(" ")

input_names = ["Artem", "Sviridov"]
customer = Customer(f"{input_names[0]}", f"{input_names[1]}")
print("Choose hotel for booking")
print(hotel_for_choose)

while True:
    try:
        input_hotel_number = int(input())
        if input_hotel_number > len(hotel_for_choose) or input_hotel_number <= 0:
            raise InputExeptionError("We dont have such hotel", input_hotel_number)

    except ValueError:
        print('Not a number')
    except InputExeptionError as mr:
        print(f"{mr.args[0]}, {mr.args[1]}")

    else:
        choose_name = ""
        for name in hotel_for_choose:
            if input_hotel_number == name[0]:
                choose_name = name[1]
        break
hotel = Hotel(f"{choose_name}")
print("For this hotel we have such rooms type")
booking_class = [(i, b_class) for hotel1 in hotel_list for (k, v) in hotel1.items() if k == choose_name for i, b_class
                 in v["booking_class"].items()]
print(booking_class)

print("Choose room type for booking")
while True:
    try:
        input_room_type_number = int(input())
        if input_room_type_number > len(booking_class) or input_room_type_number <= 0:
            raise InputExeptionError("We dont have such room type", input_room_type_number)

    except ValueError:
        print('Not a number')
    except InputExeptionError as mr:
        print(f"{mr.args[0]}, {mr.args[1]}")

    else:
        choose_room_type = ""
        for name in booking_class:
            if input_room_type_number == name[0]:
                choose_room_type = name[1]
        break

print("Enter user coming data in format 'YYYY MM DD' ")
while True:
    try:
        user_coming_data = input()
        if len(user_coming_data) != 10:
            raise InputExeptionError("Wrong data format", user_coming_data)
        temp_data = [int(i) for i in user_coming_data.split(" ")]

        if temp_data[0] < 2019 or temp_data[0] > 2100:
            raise InputExeptionError("Wrong data format", user_coming_data)
        if temp_data[1] < 0 or temp_data[1] > 12:
            raise InputExeptionError("Wrong data format", user_coming_data)
        if temp_data[2] < 0 or temp_data[2] > 12:
            raise InputExeptionError("Wrong data format", user_coming_data)
    except ValueError:
        print("Not a data")
    except InputExeptionError as mr:
        print(f"{mr.args[0]}, {mr.args[1]}")
    else:
        break

hotel.make_reservation(customer, booking_class=f'{choose_room_type}', date=f"{user_coming_data}")
customer.show_customer_booked_item()
customer.save_customer_data()
print(customer.upload_customer_data())
