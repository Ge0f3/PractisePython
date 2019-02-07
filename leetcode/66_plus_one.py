#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def plus_one(digits):
    for i in range(len(digits)-1,-1,-1):
        if(digits[i]==9):
            digits[i]=0
        else:
            digits[i] += 1
            return digits
    
    digits.insert(0,1)
    return digits
    



def main():
    print('*****************Plus One*****************')
    digits = [int(x) for x in input('Enter the array input: ').split(',')]
    print("The Arry after Plus One is  :  {}".format(plus_one(digits)))


if __name__ == '__main__':
    main()


			