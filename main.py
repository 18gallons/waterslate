# Fins Awesome Plant Monitor

import time
import board
import busio
import neopixel

from board import SCL, SDA

from adafruit_seesaw.seesaw import Seesaw

from analogio import AnalogOut

i2c_bus = busio.I2C(SCL, SDA)

# This is the plant sensor
ss = Seesaw(i2c_bus, addr=0x36)

# This is our light
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 1.0

#This is our pump
motor = AnalogOut(board.A0)

# Define our functions
def turn_on_led(color):
    led.brightness = 0.5
    led[0] = color

def turn_off_led():
    led.brightness = 0.0

def turn_on_pump():
    global loops_since_last_ran
    if loops_since_last_ran > 180:
        motor.value = 65535
        time.sleep(15)
        loops_since_last_ran = 0

def turn_off_pump():
    motor.value = 0

# Declare desired moisture level- for my particular plant, this is 480
DESIRED_MOISTURE = 480

# set time_since_last_ran to 180 so that it can water whenever it wants on start
loops_since_last_ran = 180

# The loop
while True:
    # read moisture level through sensor
    moisture = ss.moisture_read()

    # Compare moisture level to desired moisture level
    if moisture < DESIRED_MOISTURE:
        turn_on_led(color=(255, 0, 0))
        print("moisture: " + str(moisture))
        turn_on_pump()
        turn_off_pump()
    else:
        print("moisture: " + str(moisture))
        turn_off_led()

    #this sleep function is so that it does not spam the output with an obscene amount of readings
    time.sleep(1)
    loops_since_last_ran += 1
    print(loops_since_last_ran)
