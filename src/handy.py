import random
import string
import sys, getpass

title_text_ascii_art = """

  ___  _     ___     ___            _              _          __  __                                   
 / __|| |   |_ _|   / __| ___  _ _ | |_  __ _  __ | |_  ___  |  \/  | __ _  _ _   __ _  __ _  ___  _ _ 
| (__ | |__  | |   | (__ / _ \| ' \|  _|/ _` |/ _||  _|(_-<  | |\/| |/ _` || ' \ / _` |/ _` |/ -_)| '_|
 \___||____||___|   \___|\___/|_||_|\__|\__,_|\__| \__|/__/  |_|  |_|\__,_||_||_|\__,_|\__, |\___||_|  
                                                                                      |___/           

"""

def make_bold(raw_str):
    return "\u001b[1m" + raw_str +"\u001b[0m" 

def get_random_string(length=30):
    return "".join([random.choice(string.ascii_lowercase + string.digits) for i in range(length)])

def number_args(raw, args_no):
    command_list = raw.split()
    if len(command_list) != args_no-1:
        print(f"The command {command_list[0]} needs {args_no-1} argument{"s" if args_no-1 > 1 else ""} {len(command_list)-1} were given")
        return
