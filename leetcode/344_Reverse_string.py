import sys

def reverse(string):
    i = 0
    j = len(string) - 1
    while (i < j):
      string[i], string[j] = string[j], string[i]
      print("swapped")
      i += 1
      j -= 1
      print(string)


def main():
    print("*****************Reverse String*****************")
    string = [str(x) for x in input("Enter the array of input: ").split(',')]
    reverse(string)
    print("The array after Reverse {}".format(string))


if __name__ == '__main__':
    main()