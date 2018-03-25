'''
https://leetcode.com/problems/subsets-ii/description/

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set). Note: The solution set must not contain duplicate subsets.
If nums = [1,2,2], a solution is: [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
'''

# start from [[]], loop through nums 
# add [num] to everything in newlist
def subsets(nums):
    ans = set()
    ans.add(())
    for num in sorted(nums):
        newset = set()
        for item in ans:
            t = item + (num,)
            newset.add(t)
        ans.update(newset)
    return list(map(list, ans))

# will go from [[0], [1], [2], [1,2]] 
# will only take last 2 to add: [[0], [1], [2], [1,2], [2,2], [1,2,2]]
def subsets_2(nums):
    res = [[]]
    nums.sort()

    for i in range(len(nums)):
        # if its first elem, or curr != prev, 
        # keep track of how many elem was in result
        if i == 0 or nums[i] != nums[i-1]:
            prevlen = len(res)
        # if its duplicate, only want to add current
        # to recently added elements 
        for j in range(len(res) - prevlen, len(res)):
            res.append(res[j] + [nums[i]])
    return res

print(subsets([1,2,2]))
print(subsets_2([1,2,2]))
