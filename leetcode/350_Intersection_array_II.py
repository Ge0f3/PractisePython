#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def intersection(nums1,nums2):
    intersec = []
        
    counts = dict()
    for num in nums1:
        counts[num] = counts.get(num,0)+1
        
    for num in nums2:
        if(num in counts and counts[num]>0):
            intersec.append(num)
            counts[num] -= 1
    return intersec
        
        
    



def main():
    print('*****************Plus One*****************')
    nums1 = [int(x) for x in input('Enter the array input: ').split(',')]
    nums2 = [int(x) for x in input('Enter the array input: ').split(',')]
    print("The Arry after Plus One is  :  {}".format(intersection(nums1,nums2)))


if __name__ == '__main__':
    main()


			