def findjewels(J,S):
	j= list()
	for i in J:
		j.append(i)

	total_jewel = 0

	for i in j:
		total_jewel = total_jewel + S.count(i)

	return total_jewel
if __name__ == '__main__':
	J = str(input("Enter J value : "))
	S = str(input("Enter S value : "))
	total = findjewels(J, S)
	print("The total value is {}".format(total))