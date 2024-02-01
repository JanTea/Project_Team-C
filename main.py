from pathlib import Path
import cash_on_hand, overheads, profit_loss

def main(): 
    """  
    - This function returns the output of all 3 financial analysis functions 
    - Writes the results on a summary report file 
    - No parameter required 
    """ 
    # assign variables to the output of the various functions 
    overhead_result = overheads.overhead_function() 
    coh_result = cash_on_hand.coh_function() 
    profitloss_result = profit_loss.profitloss_function() 
    # instantiate file path object to home directory 
    file_path = Path.home()/"Project_Team C"/"summary_report.txt" 
    # create a new file 
    file_path.touch()

    # write calculated values in the txt file 
    with file_path.open(mode="w", encoding="UTF-8") as file: 
        # write the results of each function to the file 
        # write every line of result on a new line 
        file.write(overhead_result + "\n") 
        for coh in coh_result: 
            file.write(coh + "\n") 
        for profitloss in profitloss_result: 
            file.write(profitloss + "\n")
# call the main function 
main() 
print("Successfully uploaded into summary report")