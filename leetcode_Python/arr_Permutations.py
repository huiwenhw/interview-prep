'''
https://leetcode.com/problems/permutations/description/
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


def permutations(nums):
    if len(nums) <= 1:
        return [nums]

    last = nums[0]
    oldlist = permutations(nums[1:])
    newlist = []

    for alist in oldlist:
        for index in range(len(alist)+1):
            nlist = list(alist)
            nlist.insert(index, last)
            newlist.append(nlist)
    return newlist

def permute_iter(nums):
    if len(nums) == 0: return [[]]

    perms = [[]]
    for num in nums:
        newperm = []
        for perm in perms:
            for i in range(len(perm)+1):
                newperm.append(perm[:i] + [num] + perm[i:])
        perms = newperm
    return perms 

print(permutations([1,2,3])) # [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
print(permute_iter([1,2,3])) # [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
