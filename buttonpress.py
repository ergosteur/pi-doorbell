#!/usr/bin/env python3
from gpiozero import Button
from time import sleep
import urllib.request
import os

# Set button to GPIO pin 26
button = Button(26)

# function for when button pressed
def onpress():
    print("Pressed")
	# make the web request. Be sure to modify with your own URL.
    with urllib.request.urlopen('https://maker.ifttt.com/trigger/TRIGGER_NAME/with/key/YOUR_KEY_HERE') as response:
        html = response.read()
    print(html)
	# play sound using aplay. Requires ALSA to be configured with working default card.
    os.system('aplay /home/matt/doorbell.wav')
# forever loop to listen for button press
while True:
    button.wait_for_press()
    onpress()
	# sleep to add 5 second cooldown between actions being triggered to prevent people from spamming the button
    sleep(5)