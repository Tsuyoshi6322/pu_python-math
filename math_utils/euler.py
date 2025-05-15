'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Approximate Euler's Constant via infinite series
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''


### HELPING FUNCTIONS ###
def factorial(n: int) -> int:
    result = 1

    for i in range(2, n + 1):
        result *= i
    
    return result


### MAIN FUNCTIONALITY ###
def approx_euler(amount_samples: int) -> float:
    # Precision threshold defined by the user
    epsilon = 10 ** (-amount_samples) 

    n = 0       # Term counter
    term = 1    # Term value
    e_sum = 0   # Series value

    # Iterate through each term of the series until it passed a precision threshold
    while term > epsilon:
        term = 1 / factorial(n) # Calculate term's value: 1/n!
        e_sum += term           # Add term to series value
        n += 1                  # Raise the counter

    return e_sum, n
