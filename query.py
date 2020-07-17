import datetime
import sqlite3
from sqlite3 import Error

def query_db(arg):
    query = ""
    print(type(arg))
    # INSERT
    print(arg[1])
    if arg[1] == "add":
        if len(arg) == 4:
            query = "INSERT INTO todo(date, activity) VALUES('" + arg[2] + "', '" + arg[3] + "');"
        elif len(arg) == 5:
            query = "INSERT INTO todo(date, activity, recurrence) VALUES('" + arg[2] + "', '" + arg[3] + "', '" + arg[4] + "');" 
    
    # SELECT
    elif arg[1] == "get":
        print(arg[2])
        query = "SELECT * FROM todo WHERE date='" + arg[2] + "';"
    
    # UPDATE
    elif arg[1] == "update":
        if len(arg) == 4:
            verifyDate = True
            try:
                print(arg[3])
                year, month, day = arg[3].split("-")
                datetime.datetime(int(year), int(month), int(day))
            except:
                verifyDate = False;
                print("Date not verified")
            if verifyDate:
                query = "UPDATE todo SET date='" + arg[3] + "' WHERE id='" + arg[2] + "';"
                print("Date verified")
            elif arg[3] == "daily" or arg[3] == "weekly" or arg[3] == "bimonthly" or arg[3] == "monthly" or arg[3] == "biyearly" or arg[3] == "yearly":
                query = "UPDATE todo SET recurrence='" + arg[3] + "' WHERE id='" + arg[2] + "';"
            else:
                query = "UPDATE todo SET activity='" + arg[3] + "' WHERE id='" + arg[2] + "';" 
        if len(arg) == 5:
            verifyDate = True
            try:
                year, month, day = arg[3].split("-")
                datetime.datetime(int(year), int(month), int(day))
            except:
                verifyDate = False;
            if verifyDate: 
                if arg[4] == "daily" or arg[4] == "weekly" or arg[4] == "bimonthly" or arg[4] == "monthly" or arg[4] == "biyearly" or arg[4] == "yearly":
                    query = "UPDATE todo SET date='" + arg[3] + "', recurrence='" + arg[4] + "' WHERE id='" + arg[2] + "';"
                else:
                    query = "UPDATE todo SET date='" + arg[3] + "', activity='" + arg[4] + "' WHERE id='" + arg[2] + "';"
            else:
                query = "UPDATE todo SET activity='" + arg[3] + "', recurrence='" + arg[4] + "' WHERE id='" + arg[2] + "';"
        if len(arg) == 6:
            query = "UPDATE todo SET date='" + arg[3] + "', activity='" + arg[4] + "', recurrence='" + arg[5] + "' WHERE id='" + arg[2] + "';"
  
    # DELETE
    elif arg[1] == "remove":
        query = "DELETE FROM todo WHERE id='" + arg[2] + "';"
    
    else:
        # This should probably be sent to client
        print("Error in Server logic")
    
    return query
