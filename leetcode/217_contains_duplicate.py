#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def contains_zero_set(nums, k):
    return len(list(set(nums))) < len(nums)


def contains_duplicate(nums):
    result = False
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return result


    # return len(nums)>len(set(nums))

def contains_duplicate_dict(nums):
    counts = dict()
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    return counts

def contains_duplicate_sort(nums):
    nums.sort()
    for i in range(0,len(nums)-1):
        if(nums[i]==nums[i+1]):
            return True
    return False
def contains_duplicate_set(nums):
    elems = set()
    for num in nums:
        if(num in elems):
            return True
        else:
            elems.add(num)
    return False


def main():
    print('*****************Move zeros*****************')
    nums = [int(x) for x in input('Enter the array input: ').split(',')]
    print(contains_duplicate_set(nums))


if __name__ == '__main__':
    main()


			