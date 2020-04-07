# pi-doorbell
Simple doorbell with sound + Web Request

# Requirements
 - Raspberry Pi (I use a Pi B+ rev 1.2)
 - Button connected to GPIO pin 26 and ground (modify script if you want to use a different pin)
 - IFTTT Webhook or other endpoint to receive the HTTP web request
 - Speaker

# Dependencies (pypi)
gpiozero
urllib

# File descriptions
**buttonpress.py**: Main Python script
**buttonpress.service**: systemd service definition
**doorbell.wav**: wav file to be played (https://freesound.org/people/tim.kahn/sounds/163730/)

# Notes
ALSA should be working, and have its default device set to whatever output you want to play the doorbell sound on.
As is, the systemd service runs the python script as root, which is not ideal from a security standpoint.
I used an old PC reset button, but basically any old button would work. Could probably even use a real doorbell button.