"""
    This program deletes all matching elements from a list. [a, b, c, d, a, d, f, g].
    Author: Aditya Nain
    Date: 01/23/2019
"""
"""
********pseudocode*******

define function Remove
    Remove takes a list as an argument
        initialise a new empty list 

        run a for-loop for each element in the given list
            if "an element is not in the new list "
                add it to the new list
            else 
                discard the element

        print the final list to screen

"""

# function to remove duplicate elements 
def Remove(list): 
    final_list = [] 
    for num in list: 
        #if element is already present then we don't add it to the list
        if num not in final_list: 
            final_list.append(num)
    #print final list to screen         
    return print(final_list) 
      
#example 1 
Remove(['a','b','c','d','a','d','f','g'])) 

#example 2
Remove([2, 4, 10, 20, 5, 2, 20, 4])) 