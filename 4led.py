import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define LED pins
led_pins = [11, 13, 15, 16]

# Setup LED pins as output
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

try:
    # Blink LEDs in a loop
    while True:
        for pin in led_pins:
            GPIO.output(pin, GPIO.HIGH)  # Turn on LED
            time.sleep(0.5)  # Delay for 0.5 seconds
            GPIO.output(pin, GPIO.LOW)   # Turn off LED
except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()