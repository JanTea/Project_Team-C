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
    