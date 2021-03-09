import argparse
import client
import collections

class ValidateAdd(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        valid_dates = ("yesterday", "today", "tomorrow")
        valid_status = ("incomplete", "complete")
        date, activity, status = values
        if date not in valid_dates:
            raise ValueError("invalid date {s!r}, must be 'yesterday', 'today' or 'tomorrow'".format(s=date))
        if status not in valid_status:
            raise ValueError("invalid status {s!r}, must be 'complete' or 'incomplete'".format(s=status))
        setattr(namespace, self.dest, values)

class ValidateShow(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        valid_dates = ("yesterday", "today", "tomorrow")
        date = values
        if date not in valid_dates:
            raise ValueError("invalid date {s!r}, must be 'yesterday', 'today' or 'tomorrow'".format(s=date))
        setattr(namespace, self.dest, values)

class ValidateUpdate(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        valid_dates = ("yesterday", "today", "tomorrow")
        valid_status = ("incomplete", "complete")
        ID, date, activity, status = values
        if date not in valid_dates:
            raise ValueError("invalid date {s!r}, must be 'yesterday', 'today' or 'tomorrow'".format(s=date))
        if status not in valid_status:
            raise ValueError("invalid status {s!r}, must be 'complete' or 'incomplete'".format(s=status))
        ID = int(ID)
        setattr(namespace, self.dest, values)

class ValidateRemove(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        valid_dates = ("yesterday", "today", "tomorrow")
        valid_status = ("incomplete", "complete")
        ID = values
        ID = int(ID)
        setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser(description="add, show, update and remove items on your todo list")

group_add = parser.add_mutually_exclusive_group()
group_show = parser.add_mutually_exclusive_group()
group_update = parser.add_mutually_exclusive_group()
group_remove = parser.add_mutually_exclusive_group()

group_add.add_argument("-a", "--add", nargs=3, action=ValidateAdd, help="add new activity to the database", metavar=("DATE", "ACTIVITY", "STATUS"))
group_show.add_argument("-s", "--show", nargs=1, action=ValidateShow, help="show activities on a given day", metavar=("DATE"))
group_update.add_argument("-u", "--update", nargs=4, action=ValidateUpdate, help="update an activity, date and/or status", metavar=("ID", "DATE", "ACTIVITY", "STATUS"))
group_remove.add_argument("-r", "--remove", nargs=1, action=ValidateRemove, help="remove an activity from the database", metavar=("ID"))

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
