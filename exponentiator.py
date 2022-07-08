"""
test docstring
Python3 Script to abstract the ** operator.
made by jjheffernan on 7-7-2022

:parameter
integer x = base number
integer y = exponential operator

:returns
single integer
"""


# a simple python function
import raise_to_fourth_power


def exponentiate(x, y):
    """returns var x to the y power"""
    return int(x**y) # attempted single line function


def get_input():
    x, y = int(input("give base number: \n")), int(input("give exponent operator: \n"))
    return x, y


# driver code
def main():
    """main code, includes input section"""
    #  x = int(input())
    #  y = int(input())
    #  print(get_input()[0])
    print(exponentiate(*get_input()))  # attempted code
    print(" ---- part b ----")
    test_number = 2
    square = lambda a: exponentiate(a, 2)
    cube = lambda a: exponentiate(a, 3)
    print(square(int(test_number)))
    print(cube(int(test_number)))
    print(raise_to_fourth_power.raise_to_fourth_power(test_number))



if __name__ == '__main__' :
    main()

