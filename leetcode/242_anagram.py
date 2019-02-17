

#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def is_anagram(s,t):
    s_dict = {}
    t_dict = {}
    if s == t:
        return True
    for i in s:
        try:
            s_dict[i] += 1
        except:
            s_dict[i] = 1
    for j in t:
        try:
            t_dict[j] += 1
        except:
            t_dict[j] = 1
    print(s_dict)
    print(t_dict)
    if len(s_dict) != len(t_dict):
        return False
    return t_dict == s_dict

    



def main():
    print('*****************Single number in  Array *****************')
    s = str(input("Enter the first String: "))
    t = str(input("Enter the second String: "))
    print("The Result :  {}".format(is_anagram(s,t)))


if __name__ == '__main__':
    main()


			
			

