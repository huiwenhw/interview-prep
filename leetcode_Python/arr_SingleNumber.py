'''
https://leetcode.com/problems/single-number/description/
Given an array of integers, every element appears twice except for one. Find that single one.
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

# O(n) time, O(1) space
# ^ is the xor operator in python. 
# 9 ^ 9 = 0, 9 ^ 5 ^ 9 = 5
def single_short(nums):
    res = 0
    for n in nums:
        res ^= n
    return res

# O(n) time and space
def single_number(nums):
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 0
        d[n] += 1

    ans = -1
    for k,v in d.items():
        if v == 1:
            ans = k
    return ans

nums = [9,3,9,3,9,7,9]
print(single_number(nums)) # 7
print(single_short(nums)) # 7
nums = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
print(single_number(nums)) # 16
print(single_short(nums)) # 16
