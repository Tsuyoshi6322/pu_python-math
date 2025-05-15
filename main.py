'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    The documentation is available at my GitHub repo:
    https://github.com/Tsuyoshi6322/pu_python-math
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

### IMPORTS ###
from math_utils import pi_monte_carlo, right_triangle_checker, sum_of_n_odds, approx_euler
from test_cases import run_tests

### MAIN FUNCTIONALITY ###
# TODO write input function
# For now, please input only integers

def main():
    # Testing script execution
    test_bool = input("Wanna run the test script? (Y/n): ")
    if test_bool.lower() == 'y':
        run_tests()

    # End-user execution
    else:
        ## PI APPROX ##
        samples = int(input("How many points to throw for pi?: "))
        approx_value = pi_monte_carlo(samples)
        print(f"Try 1: Approximation of pi: {approx_value} (using {samples} points)")
        approx_value = pi_monte_carlo(samples)
        print(f"Try 2: Approximation of pi: {approx_value} (using {samples} points)")
        approx_value = pi_monte_carlo(samples)
        print(f"Try 3: Approximation of pi: {approx_value} (using {samples} points)")


        ## PYTHAGOREAN TRIPLE ##
            # TODO tuple?
        a = int(input("Input a: "))
        b = int(input("Input b: "))
        c = int(input("Input c: "))

        pythagorean_triple_result = right_triangle_checker(a, b, c)
        print(f"The result of pythagorean triple: {pythagorean_triple_result}")


        ## SUM OF N ODDS ##
        number = int(input("Value of n?: "))
        sum_odds = sum_of_n_odds(number)
        print(f"The sum of {number} odd numbers = {sum_odds}")


        ## EULER APPROX ##
        approx_value, steps = approx_euler(int(input("Precision threshold? (10^(-sample)), sample: ")))
        print(f"Approximation of e: {approx_value} (using {steps} terms)")

if __name__ == '__main__':
    main()