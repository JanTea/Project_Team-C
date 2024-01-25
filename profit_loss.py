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


# difference in net profit column
# use range() to start calculation from day 2 as there is no day 0 to compare with if we start from day 1
# for loop used to compare net profit in the current day with the previous day and repeat for all days
for i in range(len(profit_and_loss)):
    # include a 0 for net profit difference in day 1
    if i == 0:
        profit_and_loss[i].append(0)
    else:
        difference = profit_and_loss[i][4] - profit_and_loss[i - 1][4]
        # append differences across all days to the csv data we already have
        profit_and_loss[i].append(difference)
# print(profit_and_loss)