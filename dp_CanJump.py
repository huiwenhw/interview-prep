'''
https://leetcode.com/problems/jump-game/description/
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
'''

# O(n) time, O(1) space
# traverse from the front, track max index we can jump to
# if curr index is > max index we can jump to, return False
def canjump_front(nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i+n)
    return True

# O(n) time, O(1) space
# traverse from the back, keeping a need var
# need var tells us how many steps we need to be able to reach the end
def canjump_short(nums):
    if not nums: return False
    need = 1
    for i in range(len(nums)-2, -1, -1):
        if nums[i] >= need:
            need = 1
            continue
        else:
            need += 1
    if nums[0] < need-1:
        return False
    return True

# O(n^2) time worse, O(n) space
# for each elem, set a 1 to where it can jump to
# if end is 0, means cant jump to the end
def canjump(nums):
    if not nums: return False
    n = len(nums)
    arr = [0 for _ in range(n)]
    arr[0] = [1,0][nums[0] == 0]

    for i in range(n-1):
        if arr[i] == 1:
            if i+1+nums[i] > n-1:
                return True
            start, end = i+1, i+1+nums[i]
            for k in range(start, end):
                arr[k] = 1

    print(arr)
    if arr[-1] == 1:
        return True
    return False

nums = [2,3,1,1,4]
print(canjump(nums)) # True
print(canjump_short(nums)) # True
print(canjump_front(nums)) # True
nums = [3,2,1,0,4]
print(canjump(nums)) # False
print(canjump_short(nums)) # False
print(canjump_front(nums)) # False
nums = [2,0]
print(canjump(nums)) # True
print(canjump_short(nums)) # True
print(canjump_front(nums)) # False
nums = [0,2,3]
print(canjump(nums)) # False
print(canjump_short(nums)) # False
print(canjump_front(nums)) # False
nums = [1,2,0,1]
print(canjump(nums)) # True
print(canjump_short(nums)) # True
print(canjump_front(nums)) # True
