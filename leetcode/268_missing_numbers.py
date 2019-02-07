#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def single_number(nums):
    for i in range(0,len(nums)+1):
            if(i not in nums):
                return i

    



def main():
    print('*****************Missing number in  Array *****************')
    nums = [int(x) for x in input('Enter the array input: ').split(',')]
    print("The Missing Number is  :  {}".format(single_number(nums)))


if __name__ == '__main__':
    main()


			