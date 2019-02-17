

#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def strstr(haystack,neddle):

    for i in range(0,len(haystack),len(neddle)-1):
         print("The hay stack now is {}".format(haystack[i:]))
    return -1

    



def main():
    print('*****************Single number in  Array *****************')
    haystack = str(input("Enter the Haystack : "))
    neddle= str(input("Enter the Neddle : "))
    print("The Result :  {}".format(strstr(haystack,neddle)))


if __name__ == '__main__':
    main()


			
			

