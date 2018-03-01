from random import randrange
import string
import random

def generatepwd():
	num=randrange(0,100)
	char=random.choice(string.ascii_letters).lower()
	uchar=(random.choice(string.ascii_letters)).upper()
	lis=[num,char,uchar]
	password = "".join(map(str, lis))
	print("The password is {}".format(password))

def main():
	option=True
	while(option):
		generatepwd()
		opt = input("Enter your option \n Do you want to generate a password: ").lower()
		if(opt=='yes' or opt== 'y'):
			option = True
		else:
			option = False
if __name__ == '__main__':
	main()
