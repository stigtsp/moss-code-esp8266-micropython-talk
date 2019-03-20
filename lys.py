import network
import time
import machine
import ujson
import ubinascii
import sys

from umqtt.robust import MQTTClient
from machine import ADC

# Loads the config.json file from the devices filesystem
with open('config.json') as fp:
    config = ujson.loads(fp.read())

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(config['wifi']['ssid'],config['wifi']['psk'])

print('Connecting to wifi: %s' % config["wifi"]["ssid"])

while not station.isconnected(): machine.idle()

print("Connected to wifi")


# Disable on-board access point
ap_if = network.WLAN(network.AP_IF)
if ap_if.active(): ap_if.active(False)

CLIENT_ID = ubinascii.hexlify(machine.unique_id())


c = MQTTClient(client_id = CLIENT_ID,
               server     = config['mqtt']['server'],
               user       = config['mqtt']['user'],
               password   = config['mqtt']['password'],
               port       = config['mqtt']['port'],
               ssl        = config['mqtt']['ssl']
)



c.connect()

topic_prefix = config['mqtt']['topic_prefix']

adc = ADC(0)

def publish(c, k, v):
    c.publish(topic_prefix + k, str(v), True)

while True:
    adc_val = adc.read();

    # Mapping adc_val range 400-1024 to 0-1
    light = (adc_val - 400) / (1024 - 400);

    print('ADC: %s Light: %s' % (adc_val,light))
    publish(c,"light", light)
    time.sleep_ms(200) # Sleep for 0.2 seconds

c.disconnect()
