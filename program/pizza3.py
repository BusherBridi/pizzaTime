from pizzapi import *
firstName = "Busher"
lastName = "Bridi"
email = "bridibusher@gmail.com"
phone = "5598273708"
customer = Customer(firstName, lastName, email, phone)
street = "5842 W buena vista ave"
city = "visalia"
state = "CA"
zip = "93919"
address = Address(street, city, state, zip)
store = address.closest_store()
order = Order(store, customer, address)
cardNumber = "123212212"
cardExpDate = "4654"
cardSecNum = "551"
cardZip = "93291"
card = PaymentObject(cardNumber, cardExpDate, cardSecNum, cardZip)
order.add_item("W08PMANW")
order.place(card)
