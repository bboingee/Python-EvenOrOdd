import string

"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

"""Function"""


def first():  # Function first is to make sure user enters the right integer for first number.
    fair = True
    while fair:  # While fair is True.
        try:
            number = int(input("Please enter an integer : "))  # User will enter a value and will be stored to number.
            if number >= 0:  # Since 0 is even number, You give condition that is greater or equal to 0.
                return number  # When user uses the first() function, they will receive value stored in number.
            else:
                raise ValueError  # If user enters a character, it will raise a value error.
        except ValueError:  # Value error message. Asking user to input the data again.
            print("You did not enter an integer. Please enter an integer again : ")


def second():  # Function second is to make sure user enters the right integer for the divisor.
    fair = True
    while fair:  # While fair is True
        try:
            divider = int(input("Please enter an integer to divide by : "))  # User will enter a value and
            # will be stored to divider.
            if divider >= 1:  # Since you can't divide by 0, therefore greater or equal to 1.
                return divider  # When user uses second() function, they will receive value stored in divider.
            else:
                raise ValueError  # If user enters a character, it will raise a value error.
        except ValueError:  # Value error message. Asking user to input the data again.
            print("You did not enter an integer")


def od(y):  # Function that will calculate if number is odd or even.
    if y % 2 == 0:  # % = modulus. Any value that is used on function will be put into modulus operation.
        print("Your number ", y, "is an even number.")  # Result 0 means it's even.
    else:
        print("Your number ", y, "Is an odd number.")  # Other than 0 means it's odd.


def four(z):  # Function that will calculate if number is multiple of 4.
    if z % 4 == 0:  # Any value that is used on function will be put into modulus operation.
        print("Your number ", z, "is multiple of 4")  # Result 0 means it's multiple of 4.
    else:
        print("Your number ", z, "is not a multiple of 4")  # Other than 0 means it's not multiple of 4.


def div(a, b):  # Function that will calculate if number can be divide evenly by given number.
    if a % b == 0:  # 2 values will be used on function and will be put into modulus operation.
        print("Your number ", a, "divide evenly by ", b)  # Result 0 means that it divide evenly.
    else:
        print("Your number ", a, "does not divide evenly by ", b)  # Other than 0 means it's doesn't divide evenly.


"""Main"""


def main():  # Function that will run all other functions.
    numb = first()  # User function first() to assign value to variable numb.
    od(numb)  # Use variable numb, which is currently holding value from first() function to use od() function.
    four(numb)  # Use variable numb, to use four() function.
    divider = second()  # Use function second() to assign value to variable divider.
    div(numb, divider)  # Use 2 variables (numb and divider) to user div() function.


"""Only main() after this line"""
main()  # Running main() Function
