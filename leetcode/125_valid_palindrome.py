#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def is_palindrome(string):
    i = 0
    j = len(string) - 1
    while (i < j):
        while(i<j and not string[i].isalnum()):
            i += 1
        while(i<j and not string[j].isalnum()):
            j -=1
        if(string[i].lower() != string[j].lower()):
            print("The unmatched word {} - {}".format(string[i],string[j]))
            return False
        i+= 1;j-=1
    return True

    



def main():
    print('*****************Single number in  Array *****************')
    string = str(input("Enter the String: "))
    print("The Result :  {}".format(is_palindrome(string)))


if __name__ == '__main__':
    main()


			
			