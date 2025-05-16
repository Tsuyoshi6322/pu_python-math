'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    END USER MENU
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

### IMPORTS ###
from math_utils import pi_monte_carlo, right_triangle_checker, sum_of_n_odds, approx_euler

### MAIN FUNCTIONALITY ###

def validate_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lstrip('-').isdigit():
            return int(user_input)
        else:
            print("Please use integers.")

def menu_choice(choice: str) -> None:
    match choice:
        case '1':
            
            samples = validate_input("How many points to throw for pi?: ")
            
            approx_value = pi_monte_carlo(samples)
            print(f"Approximation of pi: {approx_value} (using {samples} points)\n")   

        case '2':
            a = validate_input("Input a: ")
            b = validate_input("Input b: ")
            c = validate_input("Input c: ")

            pythagorean_triple_result = right_triangle_checker(a, b, c)
            print(f"The result of pythagorean triple: {pythagorean_triple_result}\n")
        
        case '3':
            number = validate_input("Value of n?: ")
            sum_odds = sum_of_n_odds(number)
            print(f"The sum of {number} odd numbers = {sum_odds}\n")

        case '4':
            approx_value, steps = approx_euler(validate_input("Precision threshold? (10^(-sample)), sample: "))
            print(f"Approximation of e: {approx_value} (using {steps} terms)\n")

        case _:
            print("Invalid choice. Please try again.")


menu_choices = ['1',    # PI approx
                '2',    # Pythagorean Triple
                '3',    # Sum of n odd numbers
                '4']    # Euler's const approx


def menu_display() -> None:
    print("\n" + "="*40)
    print("         Python: Project 2")
    print("="*40)
    print("Choose an option below:")
    print(" [1] Estimate Pi using Monte Carlo")
    print(" [2] Check Right-Angled Triangle")
    print(" [3] Sum of First N Odd Numbers")
    print(" [4] Approximate Euler's Number (e)")
    print(" [end] Exit the Program")
    print("="*40)


def menu_execute() -> None:
    while True:
        menu_display()
        choice = input("Enter your choice: ").strip().lower()
        print("\n")

        if choice == 'end':
            print("Exiting program...")
            exit()

        if choice in menu_choices:
            menu_choice(choice)

        else:
            print("Invalid choice. Please try again.")
