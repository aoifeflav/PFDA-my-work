# Reads in data from data.csv and outputs eachline as a list
# Author: Aoife Flavin

import csv

FILENAME = "data.csv" #the name of the csv file the script will be read from
#DATADIR = "week_1/" -> this would be used if the csv file was in a different folder to the .py file

with open (FILENAME, "rt") as fp: #rt = read text
    reader = csv.reader(fp, delimiter=",") # creates a csv.reader object, which reads the contents of the file fp
    linecount = 0
    total = 0
    for line in reader: #  loop that iterates over each row in the CSV file.
        if not linecount: #header row
            pass
        else: #all other rows
            total += int(line[1])
        linecount += 1
    print(f"average is {total/(linecount-1)}")