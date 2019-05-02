from pizzapi import * 
from gpiozero import LightSensor
from gpiozero import Button
from gpiozero import LED
import pizza1
import pizza2.py
import pizza3.py

led1 = LED(21)
led2 = LED(20)
led3 = LED(16)
sensor1 = LightSensor(14)
sensor2 = LightSensor(15)
sensor3 = LightSensor(18)
button = Button(23)

choiceIndex = 0
#add and for if choice index == 0 so it can loop if you dont order anython?
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

print(choiceIndex)
if(choiceIndex == 1):
    execfile("pizza1.py")
    print("ordering pizza 1!!!")
if(choiceIndex == 2):
    execfile("pizza2.py")
    print("ordering pizza 2!!!")
if(choiceIndex == 3):
    execfile("pizza3.py")
    print("ordering pizza 3!!")

