"""
    This program asks the user for a number n and prints the 
    sum of the numbers 1 to n

    Author: Aditya Nain
    Date: 01/23/2019
"""


"""
********pseudocode*******

ask for user input as num

sum = num*(num+1)//2

print sum to screen

"""

#takes input as integer and stores it in num
num = int(input("Enter a positive integer : "))

#this is the standard formula for calculating the sum of numbers upto n
sum = (num*(num+1))//2

#prints the sum to screen
print(f"Sum from 1 to {num} is {sum}")