#!/usr/bin/env python

import database
import query
import datetime
import socket

TCP_IP = '192.168.0.37'
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

myquery = ""

while 1:
    s.listen(1)

    conn, addr = s.accept()

    print("Connection address:", addr)

    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        args = data.decode()
        
        # Store arguments in a list
        arg = args.split("', '")
        
        # Parse out "['"
        firstArg = arg[0]
        arg[0] = firstArg[2:]

        # Parse out "']"
        n = len(arg) - 1
        lastArg = arg[n]
        arg[n] = lastArg[:-2]
        print(arg)
        print(arg[1])
        print(type(arg))
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
                            conn.send("Adding date, activity and recurrence to database".encode())
                            myquery = arg
                        else:
                            conn.send(err.encode())
                    else:
                        conn.send("Adding date and activity to database".encode())
                        myquery = arg
                else:
                    conn.send(err.encode())

            # Check get arguments
            elif arg[1] == "get":
                if len(arg) == 3:
                    try:
                        year, month, day = arg[2].split("-")
                        datetime.datetime(int(year), int(month), int(day))
                        conn.send("Retrieving activities".encode())
                        myquery = arg
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
                        conn.send("Sending date update to database".encode())
                        myquery = arg
                    elif arg[3] == "daily" or arg[3] == "weekly" or arg[3] == "bimonthly" or arg[3] == "monthly" or arg[3] == "biyearly" or arg[3] == "yearly":
                        conn.send("Sending reccurence update to database".encode())
                        myquery = arg
                    else:
                        print("Did we get here?")
                        conn.send("Sending activity update to database".encode())
                        myquery = arg
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
                            conn.send("Sending date and recurrence update to database".encode())
                            myquery = arg
                        else:
                            conn.send("Sending date and activity update to database".encode())
                            myquery = arg
                    else:
                        if arg[4] == "daily" or arg[4] == "weekly" or arg[4] == "bimonthly" or arg[4] == "monthly" or arg[4] == "biyearly" or arg[4] == "yearly":
                            conn.send("Sending activity and recurrence update to database".encode())
                            myquery = arg
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
                            conn.send("Sending date, activity and recurrence update to database".encode())
                            myquery = arg
                    else:
                        conn.send(err.encode())
                else:
                    conn.send(err.encode())

            # Check remove arguments
            elif arg[1] == "remove":
                if len(arg) == 3:
                    conn.send("Removing item " + str(arg[:]) + " from database".encode())
                    myquery = arg
                else:
                    conn.send(err.encode())
            else:
                conn.send(err.encode())
        else:
            conn.send(err.encode())
    
    if __name__ == "__main__":
        print("myquery is type " + str(type(myquery)))
        sql = query.query_db(myquery)
        if arg[1] == "get":
            get = database.get(sql)
            rows = ""
            for row in get:
                rows += str(row) + " "
            print(rows)
            conn.send(rows.encode())
        else:
            database.create_query(sql)
     
    conn.close()
