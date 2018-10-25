#! /usr/bin/python3
from sub import sub
class main(object):
	"""docstring for main"""
	def __init__(self):
		print("Constructor from the main class")
	def main1():
		sub = sub()
		username=str(input("Enter your name : "))
		sub.greet(username)
	if __name__ == '__main__':
		main1()

		