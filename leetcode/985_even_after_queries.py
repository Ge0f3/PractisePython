#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def even_number(A,queries):
    s = sum(num for num in A if num%2==0)
    even_sum = []
    for query in queries:
        if(A[query[1]]%2==0):
            s -= A[query[1]]
        A[query[1]] += query[0]
        if(A[query[1]]%2 ==0):
            s+= A[query[1]]
        even_sum.append(s)
    return even_sum



def main():
    print('*****************Even Number after queries*****************')
    A = [1,2,3,4]
    queries = [[1,0],[-3,1],[-4,0],[2,3]]
    print("The result is {}".format(even_number(A,queries)))


if __name__ == '__main__':
    main()


			