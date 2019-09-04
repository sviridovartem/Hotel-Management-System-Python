from Classes.Customer import Customer
from Classes.Hotel import Hotel
import hotel_data
import datetime

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
input_hotel_number = int(input())

choose_name = ""
for name in hotel_for_choose:
    if input_hotel_number == name[0]:
        choose_name = name[1]

hotel = Hotel(f"{choose_name}")
print("for this hotel we have such rooms type")

booking_class = [(i, b_class) for hotel1 in hotel_list for (k, v) in hotel1.items() if k == choose_name for i, b_class
                 in v["booking_class"].items()]
print(booking_class)

print("Choose room type for booking")
input_room_type_number = int(input())
choose_room_type = ""
for name in booking_class:
    if input_room_type_number == name[0]:
        choose_room_type = name[1]

hotel.make_reservation(customer, booking_class=f'{choose_room_type}', date="2019 10 12")
customer.customer_data()
customer.save_customer_data()
print(customer.upload_customer_data())

