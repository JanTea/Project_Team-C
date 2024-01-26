# import a specific function instead of the entire library 
from pathlib import Path 
import csv 
 
# create a file path to csv file 
# file we want to read and write on 
fp = Path.home()/"Project_Team C"/"csv_reports"/"cash on hand.csv" 
 
# read the csv file 
with fp.open(mode="r", encoding="UTF-8", newline="") as file: 
reader = csv.reader(file) 
# skip header 
next(reader) 
 
# create an empty list for cash on hand 
coh=[]  
 
# append profit and loss to the empty list 
for row in reader: 
    # get the Day and Cash on Hand 
    # and append to the empty list 
    # convert Day to integer data type 
    # convert Cash on Hand to float data type 
    coh.append([int(row[0]),int(row[1])])  
# print(coh)
# difference in Cash on Hand 
# use range() to start calculation from day 2 as there is no day 0 to compare with if we start from day 1 
# for loop used to compare Cash on Hand in the current day with the previous day and repeat for all 80 days 
for i in range(len(coh)): 
    # include a 0 for Cash on Hand difference in day 1 
    if i == 0: 
        coh[i].append(0) 
    else:  
        diff = coh[i][1] - coh[i - 1][1] 
        # append differences across all days to the csv data we already have 
        coh[i].append(diff) 
# print(coh)
# If Cash on Hand ALWAYS INCREASING 
def increasing():  
    print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY") 
    # create a function that returns the Cash on Hand difference only 
    def npd(e): 
        """ 
        - This function returns the Cash on Hand difference for each day 
        """ 
        return e[2] 
    # sort by the 2nd index, the Cash on Hand difference, for each day 
    # sort in descending order so that we will start with highest cash surplus 
    coh.sort(reverse = True, key=npd) 
    print (f"[HIGHEST CASH SURPLUS] DAY: {coh[0][0]}, AMOUNT: SGD {coh[0][2]}")
# If Cash on Hand ALWAYS DECREASING 
def decreasing():  
    print("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN PREVIOUS DAY") 
    # create a function that returns the Cash on Hand difference only 
    def npd(e): 
        """ 
        - This function returns the Cash on Hand difference for each day 
        """ 
        return e[2] 
    # sort by the 2nd index, the Cash on Hand difference, for each day 
    coh.sort(key=npd) 
    print (f"[HIGHEST CASH DEFICIT] DAY: {coh[0][0]}, AMOUNT: SGD {abs(coh[0][2])}")
