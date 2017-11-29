'''
https://leetcode.com/problems/subsets/description/
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
'''

# [1,2,3] 
# make a copy and append the elements 
# [ , 3, 32, 2, 13, 321, 21, 1]
def subsets(nums):
    if len(nums) == 0: return [[]]

    newlist = []
    if len(nums) > 0:
        num = nums[0]
        oldlist = subsets(nums[1:])
        if oldlist is None:
            newlist = [[num]]
        else:
            for li in oldlist:
                newlist.append(li)
                combined = li + [num]
                newlist.append(combined)
    return newlist

# start from [[]], loop through nums 
# add [num] to everything in newlist
def subsets_short(nums):
    ans = [[]]
    for num in nums:
        ans += [item + [num] for item in ans]
        print('ans ', ans)
    return ans

print(subsets([1,2,3])) # [[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]
print(subsets_short([1,2,3])) # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
print(subsets_short([1,2,2,1])) # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

