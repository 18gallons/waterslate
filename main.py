# Fins Awesome Plant Monitor

import time
import board
import busio
import neopixel

from board import SCL, SDA

from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(SCL, SDA)

# This is the plant sensor
ss = Seesaw(i2c_bus, addr=0x36)

# This is our light
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 1.0

# Define our functions
def turn_on_led(color):
    led.brightness = 1.0
    led[0] = color

def turn_off_led():
    led.brightness = 0.0

# Declare desired moisture level
DESIRED_MOISTURE = 600

# Our loop
while True:
    # read moisture level through sensor
    moisture = ss.moisture_read()

    # Compare moisture level to desired moisture level
    if moisture < DESIRED_MOISTURE:
        turn_on_led(color=(255, 0, 0))
    else:
        turn_off_led()

    print("moisture: " + str(moisture))
    time.sleep(1)
