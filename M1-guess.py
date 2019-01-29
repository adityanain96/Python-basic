"""
    This program asks the user to guess a secret number and after every guess the
    program tells the user whether their guess was too large or too small.

    It also displays the number of tries required to guess the secret number

    Author: Aditya Nain
    Date: 01/23/2019
"""

"""
********pseudocode*******

Generate a random number

Ask for user input 

set counter to zero

while user input is not equal to the random number

    check if "user input is greater than or less than the random number"

        if "user input is greater than random number"
            print response 
                "Number is too small, enter a larger number"
            increment counter by one

        if "user input is less than random number"
            print response
                "Number is too large, enter a smaller number"
            increment counter by one
endwhile

print response 
    "Congrats!! You guessed the secret number"
    "number of tries required to guess the number"
"""

#imports random module 
import random

#generates a random number from 1 to 1000
x = random.randint(1,1001)

#asks user to guess a number
guess = int(input("Enter a number from 1 to 1000 : "))

#sets tries counter to 0
tries = 0

#check if user input is equal to random number or not....loop ends if user input equals random number
while guess != x:
    if guess < x:
        guess = int(input("Number is too small, enter a larger number : "))
        #increment counter by one
        tries += 1
    else:
        guess = int(input("Number is too large, enter a smaller number : "))
        #increment counter by one
        tries += 1

print(f"Congrats!! You guessed the secret number {x}")

print(f"Number of tries required = {tries}")   


