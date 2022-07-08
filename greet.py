# test comment
# created by jj on 7/6/22

def greet(name):
    """prints str greeting using var name """
    # name = input("What is your name?")
    print("Hello " + name + " welcome to Python3!ß")


def name_input():
    """gets input arg for greet() function """
    # split greet() into two functions
    return input("What is your name? \n")


def main():
    """main function"""
    name = name_input()
    greet(name)


if __name__ == '__main__':
    main()


