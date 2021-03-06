import argparse

parser = argparse.ArgumentParser(description="add, show, update and remove items on your todo list")

group_add = parser.add_mutually_exclusive_group()
group_show = parser.add_mutually_exclusive_group()
group_update = parser.add_mutually_exclusive_group()
group_remove = parser.add_mutually_exclusive_group()

group_add.add_argument("-a", "--add", nargs=3, help="add new activity to the database")
group_show.add_argument("-s", "--show", nargs=1, help="show activities on a given day")
group_update.add_argument("-u", "--update", nargs=4, help="update an activity, date and/or status")
group_remove.add_argument("-r", "--remove", nargs=1, help="remove an activity from the database")

#parser.add_argument("add_args", nargs="3", help="")
#parser.add_argument("show_args", nargs="1", help="")
#parser.add_argument("update_args", nargs="4", help="")
#parser.add_argument("remove_args", nargs="1", help="")

args = parser.parse_args()

add = args.add
show = args.show
update = args.update
remove = args.remove

#args_add = args.add_args
#args_show = args.show_args
#args_update = args.update_args
#args_remove = args.remove_args

if add:
    if (add[0] == "yesterday"):
        if (add[2] == "complete"):
            pass
        elif (add[2] == "incomplete"):
            pass
    elif (add[0] == "today"):
        if (add[2] == "complete"):
            pass
        elif (add[2] == "incomplete"):
            pass
    elif (add[0] == "tomorrow"):
        if (add[2] == "complete"):
            pass
        elif (add[2] == "incomplete"):
            pass
if show:
    if (show[0] == "yesterday"):
        pass
    elif (show[0] == "yesterday"):
        pass
    elif (show[0] == "yesterday"):
        pass
if update:
    if (update[1] == "yesterday"):
        if (update[3] == "complete"):
            pass
        elif (update[3] == "incomplete"):
            pass
    elif (update[1] == "today"):
        if (update[3] == "complete"):
            pass
        elif (update[3] == "incomplete"):
            pass
    elif (update[1] == "tomorrow"):
        if (update[3] == "complete"):
            pass
        elif (update[3] == "incomplete"):
            pass
if remove:
    print(args.remove)
