'''
https://leetcode.com/problems/counting-bits/description/

Given a non negative integer number num. For every numbers i in the range 0 <= i <= num calculate the number of 1's in their binary representation and return them as an array.
Example:
For num = 5 you should return [0,1,1,2,1,2]

[0]
[0, 1]
[0, 1]
[0, 1, 1, 2]
[0, 1, 1, 2]
[0, 1, 1, 2, 1, 2, 2, 3]
[0, 1, 1, 2, 1, 2, 2, 3]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
ans: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
'''

import sys

def count_bits(num):
    ans = []
    for n in range(num+1):
        count = 0
        while n:
            n &= n-1
            count += 1
        ans.append(count)
    return ans

def count_bits_short(num):
    res=[0]
    while len(res)<=num:
        print res
        res += [i+1 for i in res]
        print res
    return res[:num+1]

def main():
    num = int(sys.argv[1])
    print count_bits(num)
    print count_bits_short(num)

if __name__ == '__main__':
    main()
