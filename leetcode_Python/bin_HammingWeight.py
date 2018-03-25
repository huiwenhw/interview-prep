'''
https://leetcode.com/problems/number-of-1-bits/description/

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3
'''

import sys

def hamming_weight(num):
    binary = "{0:b}".format(num)
    count = 0
    for bit in binary:
       if bit == '1':
        count += 1 
    return count

def hamming_weight_short(num):
    count = 0
    while num:
        num = num & (num-1)
        count += 1
    return count

def hamming_weight_supershort(num):
    return bin(num).count('1')

def main():
    num = int(sys.argv[1])
    print hamming_weight(num)
    print hamming_weight_short(num)
    print hamming_weight_supershort(num)

if __name__ == '__main__':
    main()
