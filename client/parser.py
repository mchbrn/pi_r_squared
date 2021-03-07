import argparse
import client

parser = argparse.ArgumentParser(description="add, show, update and remove items on your todo list")

group_add = parser.add_mutually_exclusive_group()
group_show = parser.add_mutually_exclusive_group()
group_update = parser.add_mutually_exclusive_group()
group_remove = parser.add_mutually_exclusive_group()

group_add.add_argument("-a", "--add", nargs=3, help="add new activity to the database")
group_show.add_argument("-s", "--show", nargs=1, help="show activities on a given day")
group_update.add_argument("-u", "--update", nargs=4, help="update an activity, date and/or status")
group_remove.add_argument("-r", "--remove", nargs=1, help="remove an activity from the database")

args = parser.parse_args()

add = args.add
show = args.show
update = args.update
remove = args.remove

if add:
    data = []
    data.append("add")

    for arg in add:
        data.append(arg)

    if (data[1] == "yesterday" or data[1] == "today" or data[1] == "tomorrow"):
        if (data[3] == "complete" or data[3] == "incomplete"):
            client.sendRequest(data)
if show:
    data = []
    data.append("show")

    for arg in show:
        data.append(arg)

    if (data[1] == "yesterday" or data[1] == "today" or data[1] == "tomorrow"):
        client.sendRequest(data)
if update:
    data = []
    data.append("update")

    for arg in update:
        data.append(arg)
    

    if (data[2] == "yesterday" or data[2] == "today" or data[2] == "tomorrow"):
        if (data[4] == "complete" or data[4] == "incomplete"):
            client.sendRequest(data)
if remove:
    data = []
    data.append("remove")

    for arg in remove:
        data.append(arg)

    client.sendRequest(data)
