import random

def guess():
	ran=random.randint(1000,9999)
	print(ran)
	return ran 

def play(ran):
	cow =2 
	bull=0 
	print("lets play cow and bull game !!")
	game_over=0
	while  game_over <= 7 :
		guess=input("Enter your guess: ")
		if(guess == ran):
			print("you win")
			break
		else:
			guess=str(guess)
			ran=str(ran)
			guess=list(guess)
			ran=list(ran)
			match=set(guess)&set(ran)
			exact = [i for i, j in zip(guess, ran) if i == j]
			print("Number of match = {} Exact = {} ".format(len(match),len(exact)))
			game_over += 1 
def main():
	ran = guess()
	play(ran)

if __name__ == '__main__':
	main()
