'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Calculate the sum of n odd numbers
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

### MAIN FUNCTIONALITY ###
def sum_of_n_odds(n: int) -> int:
    result = 0

    # Calculate and add each odd number
    for k in range(1, n + 1):
        odd_number = 2*k - 1
        result += odd_number
    
    return result
