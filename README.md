# ESP8266 + MicroPython

Slides and examples from the Moss Code ESP8266+MicroPython Talk.

I recommend using ampy to upload code and files to the ESP, you can install it with 

`pip3 install adafruit-ampy`

To set up `lys.py` do the following:

* Create your own `config.json` (see config.json.sample for reference)
* Set up an MQTT server (with TLS/SSL)
* Set your USB serial device in `Makefile`
* Type `make` to copy the files over to the ESP

TODO: Improve this doc
