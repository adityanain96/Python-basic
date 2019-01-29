"""
    This program prints the next n leap years

    Author: Aditya Nain
    Date: 01/23/2019
"""

"""
********pseudocode*******

get current year from system

get user input as for how many laep years he want
check for leap years
if "it is a leap year"
    increment the year by 4 , twenty times using a for loop and print to screen

if "it is not a leap year"
    use while loop to get the closest previous leap year

    while "not a leap year"
        decrement by 1
    endwhile

    increment the year by 4 , twenty times using a for loop and print to screen

"""

#import date module
from datetime import date 

#gets the current year
year = date.today().year

n_leap = int(input("Enter how many next leap years you want: "))
#if leap year then add 4 everytime in a loop to get consecutive leap years
if(year%4==0 and year%100!=0 or year%400==0):
    print(f"Next {n_leap} leap years are : ")
    for i in range (1,n_leap+1):
        #print next 20 leap years to screen
        print(year + 4)
        year += 4
else:
    #if not leap year then reduce year by 1 until it becomes a leap year
    while not(year%4==0 and year%100!=0 or year%400==0):
        year -= 1      
    print(f"Next {n_leap} leap years are : ")
    for i in range (1,n_leap+1):
        #print next 20 leap years to screen
        print(year + 4)
        year += 4
       