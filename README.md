#Python-EvenOrOdd

Python program that will determine if the integer is even or odd, multiple of 4, or divide evenly by given number.

##Instruction

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. If the number is a multiple of 4, print out a different message. Ask the user for two numbers: one number to check and one number to divide by. If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
Practice Python

The exercise was obtained from this website. http://www.practicepython.org/

##About

Programmed by Bentley Kang

This exercise was done by using define functions, while loops with errors and exceptions, if and else statement, and passing by reference or by value. There are total 5 functions. first, second, od, four, div, and main. The function called first will ask the user for a number and will go through while loop with errors and exceptions. In this case only, the error will be value error where the user inputs character. If the user inputs valid integer, it will return the value.

The function called second will also go through while loop with errors and exceptions. Since the purpose of this function is to ask the user for divisor, it must not be zero and should reject any character inputs. if a valid input is valid, it will return the value.

The function called od, will calculate if the value returned from the first function is even or odd. This is done simply by using modulus operation. If and else statement is used, if the returned value mod 2 is equal to 0 then use print function to tell the user that it even otherwise tells user it's odd.

The function four will calculate if the value returned from the first function is multiple of 4. If and else statement is used, the condition is that if returned value mod 4 is equal to 0 then use print function to tell the user that it is multiple or 4, otherwise tell the user it is not multiple of 4.

The function div has 2 placeholders for to take 2 values from a first function and the second function. A number and divisor. If and else statement is used with the condition that if number mod divisor is equal to 0 then use print function to tell the user that number divides evenly by divisor. else tell the user it is not.

The main function has 2 variable called numb and divider. numb = first() means that numb will store a value that is returned from a function called first. The same goes to the variable called divider. Then I called the function with a variable that I created which currently holds the valid entry. The value will pass to the function and will run through the function. So in the main function, it only contains 5 lines of code. 2 lines to assign variables. 3 lines to call the function.

Lastly, call the function called main.
