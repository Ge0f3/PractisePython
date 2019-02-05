#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def longest_common_prefix(strings):
    common_prefix = ''
    if(len(strings)<1):
        return common_prefix
    min_string = min(strings)
    for i in range(1,len(min_string)+1):
        prefix = min_string[:i]
        for string in strings:
            if(prefix != string[:i]):
                return common_prefix
        common_prefix = prefix
        
        
    return common_prefix


def main():
    print('*****************Longest Common Prefix*****************')
    strings = [str(x) for x in
               input('Enter the array input of Strings: ').split(',')]
    print('The strings are {}'.format(strings))
    print("The result is {}".format(longest_common_prefix(strings)))


if __name__ == '__main__':
    main()


			