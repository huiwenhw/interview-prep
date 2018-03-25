'''
https://leetcode.com/problems/maximum-swap/description/

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Inpu t: 9973
Output: 9973
Explanation: No swap.
'''

# break early if a swap happened, cause there wont be other numbers greater
def maxswap(num):
    n, newn, newk = str(num), '', 0
    for i in range(len(n)):
        maxn = -1
        for k in range(i+1, len(n)):
            if int(n[k]) >= maxn:
                maxn = int(n[k])
                newk = k
        if maxn > int(n[i]):
            newn = n[:i] + n[newk] + n[i+1:newk] + n[i] + n[newk+1:]
            break
    newn = int(newn) if newn else num
    return newn

# swap 
def max_swap(num):
    maxn = num
    n = str(num)
    for i in range(len(n)):
        for k in range(i+1, len(n)):
            newn = n[:i] + n[k] + n[i+1:k] + n[i] + n[k+1:]
            print('newn ', newn, ' n ', n, ' i ', i, ' k ', k)
            if int(newn) > maxn:
                maxn = int(newn)
    return maxn

print(maxswap(2736)) # 7236
print(maxswap(9973)) # 9973
print(maxswap(112)) # 211
print(maxswap(1012)) # 2011
print(maxswap(4973)) # 9473
print(maxswap(4579)) # 9574
print(maxswap(98368)) # 98863
print(maxswap(1993)) # 9913

print(max_swap(2736)) # 7236
print(max_swap(9973)) # 9973
print(max_swap(112)) # 211
print(max_swap(1012)) # 2011
print(max_swap(4973)) # 9473
print(max_swap(4579)) # 9574
print(max_swap(98368)) # 98863
print(max_swap(1993)) # 9913
