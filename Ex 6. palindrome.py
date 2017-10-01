name=str(input("Enter a string to check whether it is a Palindrome or not:"))
reverse=name[::-1]
if(name==reverse):
  print("{} is Palindrome".format(name))
else:
  print("{} is not a Palindrome".format(name))