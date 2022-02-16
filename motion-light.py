import board
import neopixel
import RPi.GPIO as GPIO
import time

MAX_PIXELS = 55
SHINE_LIGHT_INTERVAL = 120
MOTION_DETECTED_PIN = 21
LED_STRIP_PIN = board.D18
WHITE = (255,255,255)
OFF = (0,0,0)

pixels = neopixel.NeoPixel(LED_STRIP_PIN, MAX_PIXELS, brightness=1.0)

GPIO.setwarnings(False)

# Refer pins by their sequence number on the board
GPIO.setmode(GPIO.BCM)

# Read output from PIR motion sensor
GPIO.setup(MOTION_DETECTED_PIN, GPIO.IN)

while True:
    try:
        if GPIO.input(MOTION_DETECTED_PIN):
            pixels.fill(WHITE)
            time.sleep(SHINE_LIGHT_INTERVAL)
            pixels.fill(OFF)
    except KeyboardInterrupt:
        pixels.fill(OFF)
        exit()
