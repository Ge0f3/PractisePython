numbers=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
condt=int(input("enter a number "))
newlist=[]
for num in numbers:
  if(num<condt):
    newlist.append(num)
    
print("{}".format(newlist))