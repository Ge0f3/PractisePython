from random import randint
def Guess():
	guess_count = 0
	min_limit=1
	max_limit=100
	while(True):
		guess = randint(min_limit,max_limit)
		print("The Guess is  -->{}".format(guess))
		user_input = str(input("Is the Guess correct: "))
		if(user_input.lower()=='yes'):
			return guess_count
		elif(user_input.lower()=='no'):
			guess_count +=1
			user_input =str(input("Is the Number higher than the guess ? "))
			if(user_input.lower() =='yes'):
				min_limit=guess+1
			if(user_input.lower()=='no'):
				max_limit=guess-1
if __name__ == '__main__':
	guess_count = Guess()
	if(guess_count<4):
		print("Thats pretty good {} tries".format(guess_count))
	elif(guess_count<4 and guess_count <10):
		print("Pretty well {} tries".format(guess_count))
	else:
		print("Thats bad {} tries".format(guess_count))


