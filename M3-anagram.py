"""
    This program checks whether two given strings are anagram of each other
    or not

    Author: Aditya Nain
    Date: 01/23/2019
"""


"""
********pseudocode*******

Take user input as two words separated by commas

Remove all whitespaces using split and join

Create a new list with split by checking for commas

Compare the length of two words

if "length is not same"
    print response
        " the entered words are not anagrams "

if "length is same"
    convert characters to lowercase for easy comparison
    sort the words alphabetically
    
    if "words are same"
    print response 
        "they are anagrams"

    if "words are not same"
    print response
        "they are not anagrams"
"""

x = input("Enter two words separated by commas : ")
#removes all the whitespaces
x = ''.join(x.split())

#makes a list of two words
wordlist = x.split(",")

#check for length of the words as a first check
if len(wordlist[0]) != len(wordlist[1]):
    print(f"{wordlist[0]} and {wordlist[1]} are not anagrams")
else:
    #converts every char to lowercase
    word1 = wordlist[0].lower()
    word2 = wordlist[1].lower()

    #sorts alphabetically , since sorted() creates a list
    word1 = ''.join(sorted(word1))
    word2 = ''.join(sorted(word2))
    
    #checks theif the sorted words are same or not
    if word1 == word2:
        print(f"{wordlist[0]} and {wordlist[1]} are anagrams")

    else:
         print(f"{wordlist[0]} and {wordlist[1]} are not anagrams")
   