# import pandas as pd
import csv
import sys
import os
import getopt
import csv_functions
from handy import make_bold, title_text_ascii_art
from command_shell import parse_commands

def parse_args(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(f'{os.path.basename(__file__)} -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    return [inputfile, outputfile]

def main():
    print(title_text_ascii_art)
    print("Type '.help' to get command list")
    
    while True:
        print(">> ", end="")
        cmd_inputs = input()
        parse_commands(cmd_inputs)



if __name__ == "__main__":
    # csv_functions.csv_writer(parse_args(sys.argv[1:])[1], csv_functions.take_csv_inputs())
    main()