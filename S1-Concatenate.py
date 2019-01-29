"""
    This program concatenates two lists together

    Author: Aditya Nain
    Date: 01/23/2019
"""


"""
********pseudocode*******

define function concatenate
    concatenate takes two arguments as lists for input
    
        add the two lists    
        print the new list to the screen

"""

#function to add list
def concatenate(list1,list2):
    
    #adding lists together
    list3 = list1 + list2

    #print new list to screen
    return print(list3)


#example
concatenate(['a','b','c'],[1,2,3])