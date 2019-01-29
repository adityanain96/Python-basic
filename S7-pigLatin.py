"""
    This program takes the first letter of every word,
    move it to the end of the word and add ‘ay’

    Author: Aditya Nain
    Date: 01/23/2019
"""

"""
************pseudocode***********

take user input as string

convert string to lower case

create a list "ls" of words using split by whitespaces

initialise ls_letter[]....this will store letters

initialise ls_new[]

for words in ls..................loop through individual words
    for letters in words.........loop through individual letters in those words
        add letters to ls_letter

    retrieve first letter using slice and add it to a new list "y"
    delete the first letter from ls_letter
    append y[0] to ls_letter
    append "ay" to ls_letter

    join letters to create word using join()
    append newly created words to ls_new

    clear ls_letter tp process the next word

join the words seperated by space to form a new sentence using join()
print the sentence to screen
        

"""

#take user input
st = input("Type a statement and press enter to translate to piglatin : \n")
#convert to lowercase
st = st.lower()
#create a list
ls = st.split(" ")

#initialise empty lists
ls_letter = []
ls_new = []

#loop through every word
for word in ls:
    #loop through every letter in each word one by one
    for letter in word:
        #add letter to a list
        ls_letter.append(letter) 
    #retrieve the first letter and store it in list y       
    x = slice(1)    
    y= ls_letter[x]
    #delete the first letter 
    del ls_letter[0]
    #add the first letter taken out at the last of ls_letter
    ls_letter.append(y[0])
    #add "ay" to the end of ls_letter
    ls_letter.append("ay")
    #join letters to form words and create a list
    z = "".join(ls_letter)
    ls_new.append(z)
    #empty ls_letter for processing of the next word    
    ls_letter.clear()

#join words to create sentence    
pig_latin = " ".join(ls_new)
#print sentence to screen
print(pig_latin)