# Python-EvenOrOdd
Python program that will determine if integer is even or odd, multiple of 4, or divide evenly by given number.

## Instruction

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check and one number to divide by.
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

## Practice Python 
The excersie was obtained from this website.
http://www.practicepython.org/

## About
Programmed by Bentley Kang

This excersie was done by using define functions, while loops with errors and exceptions, if and else statement, and passing by reference or by value.
There are total 5 functions. first, second, od, four, div, and main.
The function called first will ask user for a number and will go through while loop with errors and exceptions. In this case only error will be value error where user inputs character. If user inputs valid integer, it will return the value.

The function called second will also go through while loop with errors and exceptions. Since the purpose of this function is to ask user for divisor, it must not be zero and should reject any character inputs. if valid input is valid, it will return the value.

The fucntion called od, will calculate if value returned from the first function is even or odd. This is done simply by using modulus operation. If and else statment is used, if the returned value mod 2 is equal to 0 then use print function to tell user that it's even otherwise tell user it's odd.

The fuction four will calculate if value returned from the first function is multiple of 4. If and else statement is used, condition is that if returned value mod 4 is equal to 0 then use print function to tell user that it is multiple or 4, otherwise tell user it is not multiple of 4.

The function div have 2 placeholder for to take 2 values from first function and second function. A number and divisor. If and else statment is used with condition that if number mod divisor is equal to 0 then use print function to tell user that number divides evenly by divisor. else tell user it is not. 

The main function have 2 variable called numb and divider. numb = first() means that numb will store a value that is returned from function called first. The same goes to variable called divider. Then i called the function with variable that i created which currently holds the valid entry. The value will pass to the function and will run through the function. So in main function, it only contains 5 lines of code. 2 lines to assign variables. 3 lines to call the function. 

Lastly call the function called main.

