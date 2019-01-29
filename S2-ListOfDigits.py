"""
    This program takes a number and returns a list of digits

    Author: Aditya Nain
    Date: 01/23/2019
"""

"""
********pseudocode*******

define function listOfDigits
    listOfDigits takes a number as an argument

        initialise an empty list
        use for-loop to loop through all the digits
            convert them to integer and add to the empty list one by one
        print the list of digits to screen

"""


#function to get a list of digits in a number
def listOfDigits(number):
    #initialising an empty list    
    listOfDigits = []
    #looping through all the digits in number
    for i in number:
        #coverts digits to int and adds it to the empty list "listOfDigits"
        listOfDigits.append(int(i))
        #print list of digits to screen
    return print(f"List of Digits : {listOfDigits}")


#asks for user input
number = input("Enter a positive integer : ")
#calls the function listOfDigits
listOfDigits(number)


