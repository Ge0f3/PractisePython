#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def single_number(nums):
    elem= dict()
    for num in nums:
        try:
            elem.pop(num)
        except:
            elem[num]=1
    return elem.popitem()[0]

    



def main():
    print('*****************Single number in  Array *****************')
    nums = [int(x) for x in input('Enter the array input: ').split(',')]
    print("The Result :  {}".format(single_number(nums)))


if __name__ == '__main__':
    main()


			