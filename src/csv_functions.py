import csv
import handy


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

def addlist(raw):
    command_list = raw.split()
    if len(command_list) != 2:
        print(f"The command {command_list[0]} needs 1 argument {len(command_list)-1} were given")
        return
    f = open("tmp/{}".format())
    








