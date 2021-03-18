import sys
import os
import csv_functions


file = ""

def check_commands():
    with open("validcommands.txt", "r") as file:
        for line in file:
            stripped_line = line.strip()
            print(stripped_line)

def parse_commands(raw_command):
    global file
    if raw_command == "":
        return
    command = raw_command.split()[0]
    
    if command == "exit" or command == "quit" or command == ".q":
        print("Quitting...")
        sys.exit(0)
    elif command == ".al" or command == "addlist":
        csv_functions.addlist(raw_command)
    elif command == ".o" or command == "open":
        pass
    elif command == "cls" or command == "clear":
        os.system("cls")
    else:
        print("The command \"" + command + "\" does not exist.")

