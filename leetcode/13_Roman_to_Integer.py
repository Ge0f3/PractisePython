
import sys
from collections import OrderedDict 
roman = {
	'I':1,
	'V':5,
	'X':10,
	'L':50,
	'C':100,
	'D':500,
	'M':1000
}

roman = OrderedDict()
roman[1000] = "M"
roman[900] = "CM"
roman[500] = "D"
roman[400] = "CD"
roman[100] = "C"
roman[90] = "XC"
roman[50] = "L"
roman[40] = "XL"
roman[10] = "X"
roman[9] = "IX"
roman[5] = "V"
roman[4] = "IV"
roman[1] = "I"
def roman_to_integer(roman_letter):
	integer=0
	i=0
	while (i < len(roman_letter)): 
		if (i+1 < len(roman_letter)):
			if(roman[roman_letter[i]] >= roman[roman_letter[i+1]]):
				integer = integer + roman[roman_letter[i]]
				i +=1
			else:
				integer = integer + roman[roman_letter[i+1]] -roman[roman_letter[i]]
				i +=2
		else:
			integer = integer + roman[roman_letter[i]]
			i +=1
	return integer

def main():
	while True:
		print("*****************Input Exit to exit Anytime*****************")
		roman_letter= input("Enter the Roman Letter: ")
		if(roman_letter.lower()=='exit'):
			print("Exiting !!!")
			sys.exit(0)
		else:
			print("The equivalent integer of {} is {}".format(roman_letter,roman_to_integer(roman_letter)))

if __name__ == '__main__':
	main()