'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    The documentation is available at my GitHub repo:
    https://github.com/Tsuyoshi6322/pu_python-math
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

### IMPORTS ###
from test_cases import run_tests
from enduser_utils import menu_execute

### MAIN FUNCTIONALITY ###
def main():
    # Testing script execution
    test_bool = input("Wanna run the test script? (Y/n): ")
    if test_bool.lower() == 'y':
        run_tests()

    # End-user execution
    else:
        menu_execute()

if __name__ == '__main__':
    main()
