#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def valid_parantheses(string):
    dic = {'(':')','[':']','{':'}'}
    stack = []
    for char in string:
        if char in dic.values():
            if(len(stack)==0):
                return False
            else:
                top_element = stack.pop()
            
            if char != dic[top_element]:
                return False
        else:
            stack.append(char)

    return len(stack)==0



def main():
    print('*****************Valid Parntheses*****************')
    string = str(input("Enter the parantheses String : "))
    print('The strings are {}'.format(string))
    print("The result is {}".format(valid_parantheses(string)))


if __name__ == '__main__':
    main()


			