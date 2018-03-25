'''
https://leetcode.com/problems/reverse-bits/description/

Reverse bits of a given 32 bits unsigned integer.
For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
'''

import sys

def reverse_bits(num):
    binary ="{0:b}".format(num)
    # pad zereos in front! 
    binary = '0' * (32-len(binary)) + binary
    # reverse string and convert to int
    reverse = binary[::-1]
    return int(reverse, 2)

# or, we could do a 32 bits format 
def reverse_bits_short(num):
    binary ="{0:032b}".format(num)
    reverse = binary[::-1]
    return int(reverse, 2)

def main():
    num = int(sys.argv[1])
    print reverse_bits(num)
    print reverse_bits_short(num)

if __name__ == '__main__':
    main()
