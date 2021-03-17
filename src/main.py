# import pandas as pd
import csv
import sys
import os
import getopt

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

def take_csv_inputs():
    list_inputs = [input().replace(" ", "").split(",")]
    while list_inputs[-1] != "done":
        a = input()
        if a.lower() == "done":
            list_inputs.append("done")
            continue
        list_inputs.append(a.replace(" ", "").split(","))
    list_inputs.pop(-1)
    return list_inputs

def csv_writer(file, inputs):
    csvfile = open(file, "a+", newline='')
    csv_writer_init = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in inputs:
        csv_writer_init.writerow(row)
    csvfile.close() 

if __name__ == "__main__":
    csv_writer(parse_args(sys.argv[1:])[1], take_csv_inputs())