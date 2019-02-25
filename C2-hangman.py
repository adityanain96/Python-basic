""" This is a prgram of hangman
    The user enters a word and tells the number of letters and the computer tries to guess
    the word .It also shows the location of letters in the word
"""

"""
*************pseudocode***************

ask for user input - a word
ask for user input - number of letters

letters = [a to z]

tries_left = 20

initialise two empty lists

create list from string entered by user - word_list

while(number of letters left to guess = 0 and number of tries left = 0)
    select a random alphabet from letters
         if random alphabet is in word_list
            print response
                "Your guessed the right letter "
        1. x = index of correctly guessed letter in word_list
        2. temp_list[x] = correctly guessed letter
        3. replace correctly guessed letter with whitespace from word_list
        4. decrement tries_left by one
        5. decrement number of letters left to guess by one
            print response
                "number of tries left"
        else
            print response
                "letter not in the word, try another"
        1. delete the alphabet from letters 
        2. decrement tries_left by one   

if number of letters left to guess are zero
    print response
        "You guessed the rigth word"
else
    print response
        "Just bad luck try again next time!"    
"""


import secrets

#ask for user input
word = input("Enter a word: ")
num = int(input("Pls tell me the number of letters: "))
#convert to lowercase
word = word.lower()

#verify that length is correct
while(len(word)!=num):
    num = int(input("Uh.uh you can't fool me... enter the right number of letters "))


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#guess a random alphabet from letters
guess = secrets.choice(letters)

#setting up the maximum tries
tries_left=200

#this stores the actual location of the correctly guessed letter
temp_list = []

#create a list from string
word_list = []
for i in word:
    word_list.append(i)
    temp_list.append(" ")


#loop until either tries left gets zero or all the letters have been guessed
while(num!=0 and tries_left!=0):
    #guess a random alphabet from letters
    guess = secrets.choice(letters)    
    if guess in word_list:   
        print("\n")     
        print(f"you guessed the right letter: {guess}")
        #retrieves the index of the guessed letter
        x=word_list.index(guess)        
        temp_list[x] = guess
        #replace original word_list element with whitespace so as to avoid similar letters problem
        word_list[x] = " "
        tries_left -= 1
        num -= 1
        print(temp_list)
        print(f"tries left = {tries_left}")
        print("\n")
    else:        
        print(f"{guess}: is not in the word...try another letter")
        print(f"tries left = {tries_left-1}")
        #wrong letters are removed
        letters.remove(guess)
        tries_left -= 1        
    
if(num==0):
    print(f"You guessed the rigth word {word}")
else:
    print("Just bad luck try again next time!")
