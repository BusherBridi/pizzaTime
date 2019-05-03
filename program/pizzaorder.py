#Script to order pizza from desktop
#uses pizzapi by Grant Gordon (https://github.com/gamagori)
#This code is open source and free to use with no restrictions.
#by Busher Bridi (https://github.com/busherbridi)
#5/3/2019

from pizzapi import *

print("Pizza Time!")
firstName = raw_input("Enter first name: ")
lastName = raw_input("Enter last name: ")
email = raw_input("Enter email: ")
phone = raw_input("Enter phone number: ")
print("Creating customer with " + firstName +
      ", " + lastName + ", " + email + ", " + phone)
customer = Customer(firstName, lastName, email, phone)
street = raw_input("Enter street: ")
city = raw_input("Enter city: ")
state = raw_input("Enter state (ABV): ")
zip = raw_input("Enter zip code: ")
print("using adress: " + street + ", " + city + ", " + state + ", " + zip)
address = Address(street, city, state, zip)
store = address.closest_store()
menu = store.get_menu()
order = Order(store, customer, address)
loopChoice = 'y'
while loopChoice == 'y':
    search = raw_input("Enter query to search menu: ")
    print(menu.search(Name=search))
    print("-----------------")
    orderchoice = raw_input("would you like to add an item to order? (y/n) ")
    while orderchoice == 'y':
        orderItem = raw_input("Input item to place on order: ")
        order = Order(store, customer, address)
        order.add_item(orderItem)
        orderchoice = raw_input("Add another item? (y/n) ")
    loopChoice = raw_input("search again? (y/n) ")
cardNumber = raw_input("Enter credit card number: ")
cardExpDate = raw_input("Enter credit card exp date (ex: 0115): ")
cardSecNum =  raw_input("Enter credit card security number: ")
cardZip = raw_input("Enter credit card billing zip code: ")
card = PaymentObject(cardNumber, cardExpDate, cardSecNum, cardZip)
order.place(card)
