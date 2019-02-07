#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def maximum_profit(Stocks):
    max_profit = 0 
    for i in range(len(Stocks)):
        for j in range(i+1,len(Stocks)):
            if(Stocks[j]-Stocks[i]>max_profit):
                print("{} and {} ".format(Stocks[i],Stocks[j]))
                max_profit = Stocks[j]-Stocks[i]
    return max_profit


    



def main():
    print('*****************Best Time to Buy and sell stocks*****************')
    Stocks = [int(x) for x in input('Enter the array input: ').split(',')]
    print("The maximum Profit is {}".format(maximum_profit(Stocks)))


if __name__ == '__main__':
    main()


			