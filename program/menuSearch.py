#Script to search for pizza codes to be used for pizzaTime.py
#uses pizzapi by Grant Gordon (https://github.com/gamagori)
#This code is open source and free to use with no restrictions.
#by Busher Bridi (https://github.com/busherbridi)
#5/3/2019
from pizzapi import *

print("Pizza Time!")
#Ask user for adress info
street = raw_input("Enter street: ")
city = raw_input("Enter city: ")
state = raw_input("Enter state (ABV): ")
zip = raw_input("Enter zip code: ")
#print what info is used to create adress class the create the class
print("using adress: " + street + ", " + city + ", " + state + ", " + zip)
address = Address(street, city, state, zip)
#get the closest store for the adress and store it in variable store
store = address.closest_store()
#get the menu of the closest store and store it variable menu
menu = store.get_menu()

#while the user doesnt exit the loop, run the search method
loopChoice = 'y'
while loopChoice == 'y':
    print("Capitalize the first letter of the search...")
    #get the user input to query the search
    search = raw_input("Enter query to search menu: ")
    #use that query to search the menu of the closest store
    #print the output of the function
    print(menu.search(Name=search))
    print("-----------------")
    loopChoice = raw_input("search again? (y/n) ")

