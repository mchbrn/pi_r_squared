#!/usr/bin/env python

import socket
import sys

TCP_IP = '192.168.0.37'
TCP_PORT = 5005 
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(str(sys.argv).encode())
data = s.recv(BUFFER_SIZE)
#if sys.argv[1] == "get":
#    get = s.recv(BUFFER_SIZE)
s.close()

print(data.decode())
