#!/bin/python3
import sys #allows us to enter command line arguments, among other things
import socket
from datetime import datetime

# Define our target
#python3 scanner.py <ip>
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate a host name IPV4
else:
	print("Error")
	print("syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) # is a float
		result = s.connect_ex((target, port)) # returns error indicator
		print(f"Checking port {port}")
		if result == 0:
			print(f"Port {port} is open")
		s.close()
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
