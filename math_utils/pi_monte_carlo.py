'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Approximate pi by using Monte Carlo's method.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

### IMPORTS ###
import random

### MAIN FUNCTIONALITY ###
def pi_monte_carlo(amount_samples: int) -> float:
    # Counter for the points inside the circle
    points_inside_circle = 0

    # Loop through each sample - each point to throw
    for _ in range(amount_samples):
        # Generate random points (x,y) within the square
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point falls inside a circle
        if (x**2 + y**2 <= 1):
            points_inside_circle += 1

    # Return the approximation of pi
    return (4 * points_inside_circle / amount_samples)
