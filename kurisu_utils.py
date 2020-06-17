#!/usr/bin/python3

import json
import bluetooth
import subprocess
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'russian') 

def get_words(record):
	res = json.loads(record.Result())
	return res['text']

def get_near_devices():
	nearby_devices = bluetooth.discover_devices(lookup_names = True)
	print("found %d devices" % len(nearby_devices))
	addreses = []
	names = []
	for name, addr in nearby_devices:
		print(" %s - %s" % (addr, name))
		addreses.append(addr)
		names.append(name)
		
	return names, addreses
		
def connect_to_device(name, addr):
	name = name      # Device name
	addr = addr      # Device Address
	port = 1         # RFCOMM port
	passkey = "1111" # passkey of the device you want to connect

	# kill any "bluetooth-agent" process that is already running
	#subprocess.call("kill -9 `pidof bluetooth-agent`",shell=True)

	# Start a new "bluetooth-agent" process where XXXX is the passkey
	#status = subprocess.call("bluetooth-agent " + passkey + " &",shell=True)
	status = subprocess.call("bluetoothctl connect" + addr,shell=True)

	# Now, connect in the same way as always with PyBlueZ
	try:
		s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
		s.connect((addr,port))
		
		# test
		s.recv(1024) # Buffer size
		s.send("Hello World!")
	except bluetooth.btcommon.BluetoothError as err:
		# Error handler
		pass
	