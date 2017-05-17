import getpass
option=str(input("Do you want to Start a new Game: "))
while (option!='no'):
	player1=str(getpass.getpass("Player 1 - Rock / paper or scissor ?"))
	player2=str(getpass.getpass("Player 2 - Rock / paper or scissor ?"))
	if(player1 == player2):
		print("It's a Tie")
	elif(player1 == 'rock'):
		if(player2 == 'scissor'):
			print("Player 1 wins")
		elif(player2 == 'paper'):
			print("Player 2 wins")
	elif(player1 =='scissor'):
		if(player2=='paper'):
			print("player 1 wins")
		elif(player2=='rock'):
			print("player 2 wins")
	elif(player1=='paper'):
		if(player2=='rock'):
			print("player 1 wins")
		elif(player2=='scissor'):
			print("Player 2 wins")
	option=str(input("Do you want to Start a new Game: "))
