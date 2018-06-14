#Aditya Nain
from random import randint

print("....rock....")
print("....paper....")
print("....scissors....")


p_score = 0
c_score = 0



while True:
	#First to reach a score of 3 wins
	if p_score==3 or c_score==3:
		print(f"Player score : {p_score}")
		print(f"Computer score: {c_score}\n")
		if p_score>c_score:
			print ("YOU WIN!!!\n")
		elif p_score<c_score:
			print ("YOU LOSE :(\n")
		else:
			print ("IT'S A DRAW\n")

		x = input("Want to play again? y/n: ")
		if x=="n":
			print ("THANK YOU FOR PLAYING")
			break
		else:
			p_score=0
			c_score=0
			
	else:
		print(f"Player score : {p_score}")
		print(f"Computer score: {c_score}\n")
		p = input("Enter your choice: ")

		#Computer's choice
		c =  randint(0,2)
		if(c==0):
			c = "rock"
		elif(c==1):
			c = "paper"
		else:
			c = "scissors"

			
		if p_score!=3 and c_score!=3:		
			if(p==c):
				print("Computer chose " + c +"\n")
				p_score += 1
				c_score += 1
			elif(p=="rock" and c=="paper"):
				print("Computer chose " + c +"\n")
				c_score += 1
			elif(p=="paper" and c=="scissors"):
				print("Computer chose " + c +"\n")
				c_score += 1
			elif(p=="scissors" and c=="rock"):
				print("Computer chose " + c +"\n")
				c_score += 1
			else:
				print("Computer chose " + c +"\n")
				p_score += 1

	



