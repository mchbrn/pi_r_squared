import database
import datetime

def queryDB(data):
    one_day = datetime.timedelta(days=1)
    today = datetime.datetime.today()
    yesterday = today - one_day
    tomorrow = today + one_day

    today = today.strftime("%Y-%m-%d")
    yesterday = yesterday.strftime("%Y-%m-%d")
    tomorrow = tomorrow.strftime("%Y-%m-%d")

    if (data[0] == "['add'"):
        if (data[1] == " 'yesterday'"):
            if (data[3] == " 'incomplete']"):
                activity_formatted = data[2][2:-1]
                query = "INSERT INTO todo (date, activity, completed) VALUES('" + yesterday + "', '" + activity_formatted + "', 0);"
                database.create_query(query)
            elif (data[3] == " 'complete']"):
                activity_formatted = data[2][2:-1]
                query = "INSERT INTO todo (date, activity, completed) VALUES('" + yesterday + "', '" + activity_formatted + "', 1);"
                database.create_query(query)
        elif (data[1] == " 'today'"):
            if (data[3] == " 'incomplete']"):
                activity_formatted = data[2][2:-1]
                query = "INSERT INTO todo (date, activity, completed) VALUES('" + today + "', '" + activity_formatted + "', 0);"
                database.create_query(query)
            elif (data[3] == " 'complete']"):
                activity_formatted = data[2][2:-1]
                query = "INSERT INTO todo (date, activity, completed) VALUES('" + today + "', '" + activity_formatted + "', 0);"
                database.create_query(query)
        elif (data[1] == " 'tomorrow'"):
            if (data[3] == " 'incomplete']"):
                activity_formatted = data[2][2:-1]
                query = "INSERT INTO todo (date, activity, completed) VALUES('" + tomorrow + "', '" + activity_formatted + "', 0);"
                database.create_query(query)
            elif (data[3] == " 'complete']"):
                activity_formatted = data[2][2:-1]
                query = "INSERT INTO todo (date, activity, completed) VALUES('" + tomorrow + "', '" + activity_formatted + "', 1);"
                database.create_query(query)
    elif (data[0] == "['show'"):
        print(data[1])
        print(yesterday)
        if (data[1] == " 'yesterday']"):
            query = "SELECT * FROM todo WHERE date = '" + yesterday + "';"
            print(query)
            response = database.get(query)
            return(response)
        elif (data[1] == " 'today']"):
            query = "SELECT * FROM todo WHERE date = '" + today + "';"
            response = database.get(query)
            return(response)
        elif (data[1] == " 'tomorrow']"):
            query = "SELECT * FROM todo WHERE date = '" + tomorrow + "';"
            response = database.get(query)
            return(response)
    elif (data[0] == "['update'"):
        if (data[2] == " 'yesterday'"):
            if (data[4] == " 'incomplete']"):
                id_formatted = data[1][2:-1]
                activity_formatted = data[3][2:-1]
                query = ("UPDATE todo SET"
                        " date = '" + yesterday + "',"
                        " activity = '" + activity_formatted + "',"
                        " completed = 0"
                        " WHERE id = " + id_formatted + ";")
                database.create_query(query)
            elif (data[4] == " 'complete']"):
                id_formatted = data[1][2:-1]
                activity_formatted = data[3][2:-1]
                query = ("UPDATE todo SET"
                        " date = '" + yesterday + "',"
                        " activity = '" + activity_formatted + "',"
                        " completed = 1"
                        " WHERE id = " + id_formatted + ";")
                database.create_query(query)
        elif (data[2] == " 'today'"):
            if (data[4] == " 'incomplete']"):
                id_formatted = data[1][2:-1]
                activity_formatted = data[3][2:-1]
                query = ("UPDATE todo SET"
                        " date = '" + today + "',"
                        " activity = '" + activity_formatted + "',"
                        " completed = 0"
                        " WHERE id = " + id_formatted + ";")
                database.create_query(query)
            elif (data[4] == " 'complete']"):
                id_formatted = data[1][2:-1]
                activity_formatted = data[3][2:-1]
                query = ("UPDATE todo SET"
                        " date = '" + today + "',"
                        " activity = '" + activity_formatted + "',"
                        " completed = 1"
                        " WHERE id = " + id_formatted + ";")
                database.create_query(query)
        elif (data[2] == " 'tomorrow'"):
            if (data[4] == " 'incomplete']"):
                id_formatted = data[1][2:-1]
                activity_formatted = data[3][2:-1]
                query = ("UPDATE todo SET"
                        " date = '" + tomorrow + "',"
                        " activity = '" + activity_formatted + "',"
                        " completed = 0"
                        " WHERE id = " + id_formatted + ";")
                database.create_query(query)
            elif (data[4] == " 'complete']"):
                id_formatted = data[1][2:-1]
                activity_formatted = data[3][2:-1]
                query = ("UPDATE todo SET"
                        " date = '" + tomorrow + "',"
                        " activity = '" + activity_formatted + "',"
                        " completed = 1"
                        " WHERE id = " + id_formatted + ";")
                database.create_query(query)
    elif (data[0] == "['remove'"):
        id_formatted = data[1][2:-2]
        query = "DELETE FROM todo WHERE id = " + id_formatted + ";"
        database.create_query(query)
