# coding: utf-8

import socket
import sys

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

while True:
	print("Server in waiting")
	socket.listen(5)
	client, address = socket.accept()
	print(address," has been connected")
	while True:
		response = client.recv(255)
		if response.decode() == "" or "Bye":
			client.close()
			print("Client ",address," disconected")
		# else:
            print(response.decode())

print("Close")
client.close()
socket.close()
