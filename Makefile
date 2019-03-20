export AMPY_PORT=/dev/ttyUSB0

lys:
	ampy put config.json config.json
	ampy put lys.py main.py
