import pandas as pd
import csv
list_inputs = [input()]
while list_inputs[-1] != "done":
    list_inputs.append(input())
list_inputs.pop(-1)
with open('new.csv', "w+", newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(list_inputs)
    csvfile.close()