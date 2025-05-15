'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    SCRIPT FOR TESTING THE PROGRAM WITH SAMPLE INPUTS
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
### IMPORTS ###
from math_utils import pi_monte_carlo, right_triangle_checker, sum_of_n_odds, approx_euler

# Assuming your functions are imported or defined in this script
# from your_module import pi_monte_carlo, right_triangle_checker, sum_of_n_odds, approx_euler

def run_tests():
    print("=== PI APPROXIMATION TESTS ===")
    test_samples = [1, 10, 100, 10000, 100000]  # edge + regular

    for i in range(6):
        print(f"Try {i}")

        for samples in test_samples:
            approx = pi_monte_carlo(samples)
            print(f"Samples: {samples} -> Approx pi: {approx}")


    print("\n=== PYTHAGOREAN TRIPLE TESTS ===")
    test_triangles = [
        (3, 4, 5),     # classic right triangle
        (5, 12, 13),   # another classic triple
        (1, 1, 1),     # equilateral, not right
        (0, 4, 5),     # zero side, invalid
        (-3, 4, 5),    # negative side, invalid
        (10, 6, 8),    # scaled triple but not sorted
        (7, 24, 25),   # right triangle
        (2, 2, 3),     # not right, valid triangle
        (1, 2, 3),     # invalid triangle (1+2 = 3, no triangle)
    ]

    for a, b, c in test_triangles:
        result = right_triangle_checker(a, b, c)
        print(f"Sides: ({a}, {b}, {c}) -> {result}")


    print("\n=== SUM OF N ODDS TESTS ===")
    test_ns = [0, 1, 5, 10, 100]

    for n in test_ns:
        sum_odds = sum_of_n_odds(n)
        print(f"Sum of first {n} odd numbers = {sum_odds}")

    print("\n=== EULER NUMBER APPROXIMATION TESTS ===")
    test_precisions = [1, 5, 10, 15, 20]

    for precision in test_precisions:
        approx, steps = approx_euler(precision)
        print(f"Precision: 10^(-{precision}) -> Approx e: {approx} (using {steps} terms)")
