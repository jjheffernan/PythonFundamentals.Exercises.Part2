"""
test docstring
Python3 Script to rely on exponentiator.py to return 1 method .
made by jj heffernan on 7-7-2022

:parameter
integer x = base number
integer y = exponential operator

:returns
single integer
"""

# a python currying test function
import exponentiator


def raise_to_fourth_power(x):
    """calls exponentiator.py to return single value"""
    return exponentiator.exponentiate(int(x), 4)


# driver code
def main():
    print(raise_to_fourth_power(input("input number to raise to 4th power: \n")))  # attempted code


if __name__ == '__main__' :
    main()
