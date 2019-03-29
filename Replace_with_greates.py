#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def Replcae_with_greatest(nums):
    nums[len(nums)-1]=-1
    for i in range(len(nums)-2):
        max_temp=max(nums[i+1:])
        nums[i]=max_temp
        


def main():
    print('*****************Replace the array Elements with the Greatest*****************')
    nums = [int(x) for x in input('Enter the array input: ').split(',')]
    Replcae_with_greatest(nums)
    print(nums)


if __name__ == '__main__':
    main()
