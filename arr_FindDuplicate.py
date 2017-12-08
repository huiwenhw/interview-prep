'''
https://leetcode.com/problems/find-the-duplicate-number/description/

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
'''

# similar to linkedlist II
# find where slow and fast meet == cycle means got dup 
# dist from start to cycle == dist from X to entry point
# entry point == duplicate number
def dup_short(nums):
    slow = nums[0]
    fast = nums[nums[0]]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

# O(n) time and space
def dup(nums):
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1

    for k,v in d.items():
        if v > 1:
            return k
    return None

# Modifying array
def dup_shorter(nums):
    n = len(nums)
    
    for i in range(n):
        nums[abs(nums[i])-1] *= -1
        if nums[abs(nums[i])-1] > 0:
            return abs(nums[i])
    return None

print(dup([1,2,4,5,6,7,8,9,2])) # 2
print(dup_short([1,2,4,5,6,7,8,9,2])) # 2
print(dup_shorter([1,2,4,5,6,7,8,9,2])) # 2
