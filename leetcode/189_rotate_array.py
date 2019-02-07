#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def rotate(A,K):
    return A[K+1:]+A[:K+1]
   


    



def main():
    print('*****************Rotate Array *****************')
    A = [int(x) for x in input('Enter the array input: ').split(',')]
    K = int(input("Enter the number of rotation: "))
    print("Array after {} Rotation:  {}".format(K,rotate(A,K)))


if __name__ == '__main__':
    main()


			