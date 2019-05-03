#Script to interface Raspberry Pi microprocessor with pizzapi, a python wrapper for Domino's pizza application programing interface
#uses pizzapi by Grant Gordon (https://github.com/gamagori)
#This code is open source and free to use with no restrictions.
#by Busher Bridi (https://github.com/busherbridi)
#5/3/2019

from pizzapi import *
from gpiozero import LightSensor
from gpiozero import Button
from gpiozero import LED

#Fill out these variables with customer information
firstName = "Sherlock"
lastName = "Holmes"
email = "crimesolver@shh.com"
phone = "123456789"
#create customer class with customer information to be used in the API
customer = Customer(firstName, lastName, email, phone)
#Fill out these variables with where you want the pizza to be delivered, this will be also called to the nearest store locator to grab menu selections.
street = "221B Baker Street"
city = "London"
state = "UK"
zip = "93919"
#create address class with adress information to be used in the API
address = Address(street, city, state, zip)
#call closest store locator from adress class and store it in variable named store
store = address.closest_store()
#create order class with variable store, customer and address class.
order = Order(store, customer, address)
#Fill out payment information, this will only be sent to Domino's Pizza via the API
cardNumber = "123212212"
cardExpDate = "4654"
cardSecNum = "551"
cardZip = "93291"
#Create payment object named card with payment information
card = PaymentObject(cardNumber, cardExpDate, cardSecNum, cardZip)
#Declare some pin variables, from gpiozero lib, these pins are for the Raspberry Pi 3 B+. Typing "pinout" in the NOOBS terminal prints out a graphic with the pinout for the microprocessor board. 

led1 = LED(21)
led2 = LED(20)
led3 = LED(16)
sensor1 = LightSensor(14)
sensor2 = LightSensor(15)
sensor3 = LightSensor(18)
button = Button(23)
#Declare a variable named choiceIndex will hold which light sensor was last selected and later order a specfic type of pizza based on this variable. Set it to zero as default so pressing the button before selecting wont do anything.
choiceIndex = 0
#while the button is not pressed, loop the selection process and allow the user to change selection and turn on corresponding LED to indicate what selection is currently selected. Also print the sensor states real time
while (not button.is_pressed):
    if(sensor1.light_detected):
        print("sensor 1 on")
        choiceIndex = 1
        led1.on()
        led2.off()
        led3.off()
    elif(not sensor1.light_detected):
        print("sensor 1 off")
    if(sensor2.light_detected):
        print("sensor 2 on")
        choiceIndex = 2
        led1.off()
        led2.on()
        led3.off()
    elif(not sensor2.light_detected):
        print("sensor 2 off")
    if(sensor3.light_detected):
        print("sensor 3 on")
        choiceIndex = 3
        led1.off()
        led2.off()
        led3.on()
    elif(not sensor3.light_detected):
        print("sensor 3 off")

#This will run after the loop exits, indicating that the button has been pressed
#print the variable choiceIndex and order which pizza is assosiated with each index. The codes for the pizzas can be found by using menuSearch.py which is included in this repository.
print(choiceIndex)
if(choiceIndex == 1):
    order.add_item("P10IREPV")
    order.place(card)
    print("ordering pizza 1!!!")
if(choiceIndex == 2):
    order.add_item("20BDCOKE")
    order.place(card)
    print("ordering pizza 2!!!")
if(choiceIndex == 3):
    order.add_item("W08PMANW")
    order.place(card)
    print("ordering pizza 3!!")
