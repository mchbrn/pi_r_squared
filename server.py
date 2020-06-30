#!/usr/bin/env python

import datetime
import socket

TCP_IP = '172.16.0.208'
TCP_PORT = 5005
BUFFER_SIZE = 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

err = """
Pi R-Squared arguments must be in one of the following forms
Arguments in [] are optional
 
add yyyy-mm-dd 'activity' [recurring] 
get yyyy-mm-dd
update id [yyyy-mm-dd/'new activity'/recurring] 
remove id

Recurring options include: daily/weekly/bimonthly/monthly/biyearly/yearly
"""

while 1:
    s.listen(1)

    conn, addr = s.accept()

    print("Connection address:", addr)

    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        args = data.decode()
        print(args)
        # Store arguments in a list
        arg = args.split("', '")
        
        # Parse out "']"
        n = len(arg) - 1
        lastArg= arg[n]
        arg[n] = lastArg[:-2]

        print(len(arg))
        
        if len(arg) >= 3:
            if arg[1] == "add":
                if len(arg) == 4 or len(arg) == 5:
                    try:
                        year, month, day = arg(2).split("-")
                        datetime.datetime(int(year), int(month), int(day))
                        print("Date okay")
                    except:
                        conn.send(err.encode())
                else:
                    conn.send(err.encode())
            elif arg[1] == "get":
                print("getting")
            elif arg[1] == "update":
                print("updating")
            elif arg[1] == "remove":
                print("removing")
            else:
                conn.send(err.encode())
        else:
            conn.send(err.encode())
    conn.close()

'''
if sys.argv[1] == "add":
    print("add")
elif sys.argv[1] == "get":
    print("get")
elif sys.argv[1] == "update":
    print("update")
elif sys.argv[1] == "remove":
    print("remove")
else:
    sys.exit(err)
'''
