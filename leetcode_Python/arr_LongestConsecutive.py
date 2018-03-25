'''
https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
For example, Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
Your algorithm should run in O(n) complexity.
'''

# convert nums to a set 
# go through the set: if curr-1 is not in the set, means its the first element in a sequence 
# keep a count for every element that's larger 
# keep a max tracker 
def longest(nums):
    if not nums: return 0
    d = set(nums)
    print(d)
    maxn = count = 0
    for i in d:
        if i-1 not in d:
            y = i+1
            while y in d:
                y+=1
            maxn = max(maxn, y-i)
    return maxn

# [100, 4, 200, 1, 3, 2]
# add these to a dict 
# for every element, check if there's a elem before/after it 
# if before, add elem to set in elem-1, assign d[elem] = d[elem-1]
# if after, add d[elem+1] to d[elem]
"""
def longest(nums):
    if not nums: return 0
    d = {}
    maxn = 0
    for i in range(len(nums)):
        print('i ', i, ' nums[i] ', nums[i])
        print(d)
        if nums[i] not in d:
            d[nums[i]] = set()
        if nums[i]-1 in d and nums[i]+1 in d:
            d[nums[i]-1].add(nums[i])
            d[nums[i]].update(d[nums[i]-1])
            d[nums[i]].update(d[nums[i]+1])
            newset = d[nums[i]]
            d[nums[i]-1] = d[nums[i]]
            d[nums[i]+1] = d[nums[i]]
        elif nums[i]-1 in d:
            d[nums[i]-1].add(nums[i])
            d[nums[i]] = d[nums[i]-1]
        elif nums[i]+1 in d:
            d[nums[i]].add(nums[i])
            d[nums[i]].update(d[nums[i]+1])
            d[nums[i]+1] = d[nums[i]]
        else:
            d[nums[i]] = set({nums[i]})
        maxn = max(maxn, len(d[nums[i]]))
        print('aft ', d, maxn)
    return maxn
"""         

print(longest([100,4,200,1,3,2])) # 4
print(longest([1,2,0,1])) # 3
print(longest([1,3,5,2,4])) # 5 
print(longest([0,3,7,2,5,8,4,6,0,1])) # 9
