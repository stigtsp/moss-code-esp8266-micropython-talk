# Examples for talk:


# HELLO WORLD

from machine import Pin

# Pin(14) is marked D5 on NodeMCU
led = Pin(14, Pin.OUT)
led.value(1) # led on !
# led.value(0) # led off !









## WIFI connection

import network, machine

# Initialize connection
wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# Connecting to wifi
wifi.connect("my-network", "my-password")

# Waiting until we're connected
while not wifi.isconnected(): machine.idle()

# Printing the IP address
print(wifi.ifconfig())


## BUTTON



