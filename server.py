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
Order is set
 
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

            # Check add arguments
            if arg[1] == "add":
                # add date activity [recurrence]
                if len(arg) == 4 or len(arg) == 5:
                    try:
                        year, month, day = arg[2].split("-")
                        datetime.datetime(int(year), int(month), int(day))
                    except:
                        conn.send(err.encode())
                    if len(arg) == 5:
                        if arg[4] == "daily" or arg[4] == "weekly" or arg[4] == "bimonthly" or arg[4] == "monthly" or arg[4] == "biyearly" or arg[4] == "yearly":
                            print("Insert date, activity and recurrence into database")
                        else:
                            conn.send(err.encode())
                    else:
                        print("Insert date and activity into database")
                else:
                    conn.send(err.encode())

            # Check get arguments
            elif arg[1] == "get":
                if len(arg) == 3:
                    try:
                        year, month, day = arg[2].split("-")
                        datetime.datetime(int(year), int(month), int(day))
                        print("Get id from database")
                    except:
                        conn.send(err.encode())
                else:
                    conn.send(err.encode())

            # Check update arguments
            elif arg[1] == "update":
                # update id date
                # update id activity
                # update id recurrence
                if len(arg) == 4:
                    verifyDate = True
                    try:
                        year, month, day = arg[3].split("-")
                        datetime.datetime(int(year), int(month), int(day))
                    except:
                        verifyDate = False;
                    if verifyDate:
                        print("Sending date update to database") 
                    elif arg[3] == "daily" or arg[3] == "weekly" or arg[3] == "bimonthly" or arg[3] == "monthly" or arg[3] == "biyearly" or arg[3] == "yearly":
                        print("Sending reccurence update to database") 
                    else:
                        print("Sending activity update to database")
                # update id date activity
                # update id date recurrence
                # update id activity recurrence
                elif len(arg) == 5:
                    verifyDate = True
                    try:
                        year, month, day = arg[3].split("-")
                        datetime.datetime(int(year), int(month), int(day))
                    except:
                        verifyDate = False;
                    if verifyDate: 
                        if arg[4] == "daily" or arg[4] == "weekly" or arg[4] == "bimonthly" or arg[4] == "monthly" or arg[4] == "biyearly" or arg[4] == "yearly":
                            print("Sending date and recurrence update to database")
                        else:
                            print("Sending date and activity update to database")
                    else:
                        if arg[4] == "daily" or arg[4] == "weekly" or arg[4] == "bimonthly" or arg[4] == "monthly" or arg[4] == "biyearly" or arg[4] == "yearly":
                            print("Sending activity and recurrence update to database")
                        else:
                            conn.send(err.encode())
                #update id date activity recurrence
                elif len(arg) == 6:
                    verifyDate = True
                    try:
                        year, month, day = arg[3].split("-")
                        datetime.datetime(int(year), int(month), int(day))
                    except:
                        verifyDate = False;
                    if verifyDate:
                        if arg[5] == "daily" or arg[5] == "weekly" or arg[5] == "bimonthly" or arg[5] == "monthly" or arg[5] == "biyearly" or arg[5] == "yearly":
                            print("Sending date, activity and recurrence update to database")
                    else:
                        conn.send(err.encode())
                else:
                    send.conn(err.encode())

            # Check remove arguments
            elif arg[1] == "remove":
                if len(arg) == 3:
                    print("Remove id " + str(arg[:]) + " from database")
                else:
                    conn.send(err.encode())
            else:
                conn.send(err.encode())
        else:
            conn.send(err.encode())
    conn.close()
