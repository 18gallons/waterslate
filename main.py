# Fins Awesome Plant Monitor

import time
import board
import busio
import neopixel

from board import SCL, SDA

from adafruit_seesaw.seesaw import Seesaw

from digitalio import DigitalInOut, Direction, Pull

i2c_bus = busio.I2C(SCL, SDA)

# This is the plant sensor
ss = Seesaw(i2c_bus, addr=0x36)

# This is our light
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 1.0

#This is our pump
motor = DigitalInOut(board.A0)
motor.direction = Direction.OUTPUT

# Define our functions
def turn_on_led(color):
    led.brightness = 1.0
    led[0] = color

def turn_off_led():
    led.brightness = 0.0

def turn_on_pump():
    print("pump on")

def turn_off_pump():
    print("pump off")

def delay():
    time.sleep(5)
# Declare desired moisture level
DESIRED_MOISTURE = 500

# The loop
while True:
    # read moisture level through sensor
    moisture = ss.moisture_read()

    # Compare moisture level to desired moisture level
    if moisture < DESIRED_MOISTURE:
        turn_on_led(color=(255, 0, 0))
        print("moisture: " + str(moisture))
        turn_on_pump()
        time.sleep(5)
        turn_off_pump()
        delay()
    else:
        print("moisture: " + str(moisture))
        turn_off_led()

    #this sleep function is so that it does not spam the output with an obscene amount of readings
    time.sleep(1)
