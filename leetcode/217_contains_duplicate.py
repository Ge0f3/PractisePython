#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def contains_zero_set(nums,k):
    return len(list(set(nums))) < len(nums)

def contains_duplicate(nums):
    result = False
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if(nums[i] == nums[j]):
                return True
    return result
    #return len(nums)>len(set(nums))


def main():
    print('*****************Move zeros*****************')
    nums = [int(x) for x in input('Enter the array input: ').split(',')]
    print(contains_duplicate(nums))


if __name__ == '__main__':
    main()

			