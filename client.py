# coding: utf-8

import socket
import sys

hote = input("Server : ")
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on ",port)


while True:
    test = input("What : ")
    socket.send(test.encode())

# print("Close")
# socket.close()
