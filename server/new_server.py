#!/usr/bin/env/ python

import database
import new_query
import datetime
import socket

TCP_IP = '192.168.0.37'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

while 1:
    s.listen(1)

    conn, addr = s.accept()
    args = []

    data = conn.recv(BUFFER_SIZE).decode()
    args = data.split(",")

    if (args[0] == "['show'"):
        response = new_query.queryDB(args)
        conn.send(str(response).encode())
    else:
        new_query.queryDB(args)
