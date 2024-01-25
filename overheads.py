# import a specific function instead of the entire library
from pathlib import Path
import csv

# create a file path to csv file
# file we want to read and write on
fp = Path.home()/"Project_Team C"/"csv_reports"/"overheads.csv"

# read the csv file
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    # skip header
    next(reader)

    # create an empty list for cash on hand
    overheads=[]

    # append profit and loss to the empty list
    for row in reader:
        # get the Category and Overheads and append to the empty list
        # convert Overheads to float data type
        overheads.append([row[0],float(row[1])]) 
# print(overheads)