import csv

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