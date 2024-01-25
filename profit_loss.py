# import a specific function instead of the entire library
from pathlib import Path
import csv

# create a file path to csv file
# file to read and write on
fp = Path.home()/"Project_Team C"/"csv_reports"/"profit and loss.csv"

# read the csv file
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    # skip header
    next(reader)

    # create an empty list for profit and loss
    profit_and_loss=[] 

    # append profit and loss to the empty list
    for row in reader:
        # get the Day, Sales, Trading Profit, Operating Expense, Net Profit
        # and append to the profit_and_loss list
        # convert Day, Sales, Trading Profit, Operating Expense and Net Profit to integer data type
        profit_and_loss.append([int(row[0]),int(row[1]),int(row[2]),int(row[3]),int(row[4])]) 
print(profit_and_loss)