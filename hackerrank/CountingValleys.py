import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
# def sockMerchant(n, ar):
#     return ar
def CountingValleys(ar):
    valleys = 0
    sea_level=0
    #creating a dict to have a count of ups and downs
    for elem in ar:
        if(elem=='U'):
            sea_level +=1
        elif(elem=='D'):
            sea_level -=1
        if(sea_level==0 and elem=='U'):
            valleys +=1
    # finding out number of pairs 
    return valleys
    
if __name__ == '__main__':
    arr = str(input("Enter the input: "))
    result = CountingValleys(list(arr))

    print("No of valley's crossed is {}".format(result))