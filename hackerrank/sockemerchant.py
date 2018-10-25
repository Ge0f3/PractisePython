import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
# def sockMerchant(n, ar):
#     return ar
def sockMerchant(ar):
    socks = {}
    pairs = 0

    #creating a dict to have a count of number of sock of each items
    for elem in ar:
        socks[elem]=socks.get(elem,0)+1
    # finding out number of pairs 
    for keys,value in socks.items():
        pairs = pairs + int(value/2)
        print("The value is {} - pair is {}".format(value,pairs))
    return int(pairs)
if __name__ == '__main__':
    arr = [int(x) for x in input("Enter the array elements\nSplited by comma , : ").split()]
    result = sockMerchant(arr)

    print("The result is {}".format(result))