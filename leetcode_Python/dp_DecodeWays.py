'''
https://leetcode.com/problems/decode-ways/description/

A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1, 'B' -> 2, ..., 'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example, Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12). The number of ways decoding "12" is 2.
'''

def num_decodings(s):
    if len(s) == 0: return 0
    if s[0] == "0": return 0
    ways = 1
    for i in range(1, len(s)):
        if s[i-1:i+1] == "00": return 0
        elif s[i-1] == "0" or s[i] == "0": continue
        elif int(s[i-1:i+1]) <= 26:
            ways += 1
    return ways

# use int(s>'') to assign 1 / 0 to ways 
# if we reach a '0', discard prev ways, find if [i-1,i] is btwn 9 and 27
# if it is, means its 10/20 and we're discarding all the '02, 03 ..' at this check
# and we multiply that to prev num of ways to ensure that we can cont decoding
def decodings(s):
    pways, ways, pdigit = 0, int(s>''), ''
    for d in s:
        pways, ways, pdigit = ways, (d>'0')*ways + (9<int(pdigit+d)<27)*pways, d
        print('d ', d, ' pways ', pways, ' ways ', ways, ' pdigit ', pdigit)
    return ways

print(decodings("1234")) # 3
print(decodings("10")) # 1
print(decodings("100")) # 0
print(decodings("0")) # 0
print(decodings("01")) # 0
print(decodings("101")) # 1
print(decodings("11")) # 2
print(decodings("110")) # 1
print(decodings("11011")) # 2
