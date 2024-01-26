def profitloss_function():
    """
    - If net profit is always increasing, this function finds out the day and amount the highest increment occurs
    - If net profit is always decreasing, this function finds out the day and amount the highest decrement occurs
    - If net profit fluctuates, this function lists down all the days and amount when deficit occurs
    and finds out the top 3 highest deficit amount and the days it happened
    - No parameter is required
    """
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
    # print(profit_and_loss)

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


    # If net profit ALWAYS INCREASES
    def increasing(): 
        print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
        # create a function that returns the net profit difference only
        def npd(e):
            """
            - This function returns the net profit difference for each day
            """
            return e[5]
        # sort by the 5th index, the net profit difference, for each day
        # sort in descending order so that we will start with highest net profit surplus
        profit_and_loss.sort(reverse = True, key=npd)
        print (f"[HIGHEST NET PROFIT SURPLUS] DAY: {profit_and_loss[0][0]}, AMOUNT: SGD {profit_and_loss[0][5]}")


    # If net profit ALWAYS DECREASES
    def decreasing(): 
        print("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY")
        # create a function that returns the net profit difference only
        def npd(e):
            """
            - This function returns the net profit difference for each day
            """
            return e[5]
        # sort by the 5th index, the net profit difference, for each day
        profit_and_loss.sort(key=npd)
        print (f"[HIGHEST NET PROFIT DEFICIT] DAY: {profit_and_loss[0][0]}, AMOUNT: SGD {abs(profit_and_loss[0][5])}")


    # If net profit FLUCTUATES
    def fluctuates(): 
        for x in profit_and_loss:
            if x[5] < 0:
                print (f"[NET PROFIT DEFICIT] DAY: {x[0]}, AMOUNT: SGD {abs(x[5])}")

        # create a function that returns the net profit difference only
        def npd(e):
            """
            - This function returns the net profit difference for each day
            """
            return e[5]
        # sort by the 5th index, the net profit difference, for each day
        profit_and_loss.sort(key=npd)
        print (f"[HIGHEST NET PROFIT DEFICIT] DAY: {profit_and_loss[0][0]}, AMOUNT: SGD {abs(profit_and_loss[0][5])}")
        print (f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {profit_and_loss[1][0]}, AMOUNT: SGD {abs(profit_and_loss[1][5])}")
        print (f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {profit_and_loss[2][0]}, AMOUNT: SGD {abs(profit_and_loss[2][5])}")
        
    # create variable to check if net profit is always increasing, always decreasing, or fluctuates
    increase = False
    decrease = False
    for diff in profit_and_loss:
        if diff[5] < 0:
            decrease = True
        elif diff[5] > 0:
            increase = True

    if(increase and not decrease):
        increasing()
    elif (decrease and not increase):
        decreasing()
    else:
        fluctuates()
# call the function
profitloss_function()
