'''
https://leetcode.com/problems/contains-duplicate/description/

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''

def contains_duplicate(nums):
    numdict = {}  
    for num in nums:
        if num in numdict:
            return True
        numdict[num] = True
    return False

def contains_duplicate_short(nums):
    return len(nums) != len(set(nums))

print(contains_duplicate([1,2,3,4,5,5])) # True
print(contains_duplicate([1,2,3,4,5])) # False
print(contains_duplicate_short([1,2,3,4,5,5])) # True 
print(contains_duplicate([1,2,3,4,5])) # False
