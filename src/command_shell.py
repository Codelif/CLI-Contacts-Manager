import sys
import os
from handy import get_random_string

file = ""

def check_commands():
    with open("validcommands.txt", "r") as file:
        for line in file:
            stripped_line = line.strip()
            print(stripped_line)

def parse_commands(command):
    global file
    if command == "exit" or command == "quit" or command == ".q":
        print("Quitting...")
        sys.exit(0)
    elif command == ".al" or command == "addlist":
        file = open(f"tmp/{get_random_string()}.csv")
        
    elif command == ".cls" or command == "clearscreen":
        os.system("cls")
