#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def contains_zero_set(nums,k):
    return len(list(set(nums))) < len(nums)

def contains_zero(nums,k):
    result = False
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if(nums[i] == nums[j] and (j-i <= k)):
                print('The location is {} and {}'.format(i, j))
                return True
    return result


def main():
    print('*****************Move zeros*****************')
    nums = [int(x) for x in input('Enter the array input: ').split(',')]
    k = int(input('Enter the value for K : '))
    print(contains_zero(nums,k))


if __name__ == '__main__':
    main()

			