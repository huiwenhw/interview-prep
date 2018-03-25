'''
https://leetcode.com/problems/degree-of-an-array/description/

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6

Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''

# 1 Find degree of array 
# Go through array once, add to dict and find max value 
# 2 Find subarray that has same elements = degree
# [1,2,2] degree = 2, [1,2,2], [2,2]
# loop through array, keep track of elements that are the same & freq 
# use another dict, as we loop through, hash the number & check value == degree
# if value == degree, shorten front pointer 
def subarray(nums):
    freq = {}
    degree = 0
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
        degree = max(degree, freq[num])
    print(freq, degree)

    counter = {}
    start = end = 0
    minn = float('inf')
    while start <= end and end < len(nums):
        print('start ', start, ' ', nums[start] , ' end ', end, ' ', nums[end])
        if nums[end] not in counter:
            counter[nums[end]] = 1
        else:
            counter[nums[end]] += 1
        value = counter[nums[end]]
        #print('counter ', counter, ' value ' , value)
        if value == degree:
            minn = min(minn, end-start+1)
            #print('minn ', minn, ' end-start+1 ', end-start+1)
            counter[nums[start]] -= 1
            counter[nums[end]] -= 1
            start += 1
            #print('start ', start, ' ', nums[start] , ' end ', end, ' ', nums[end], counter)
        else:
            end += 1
        #print('minn ', minn)
    return minn

import collections 
# Group array by value
# [1, 1, 2, 2, 2, 3, 1] => { 1: [0, 1, 6], 2: [2, 3, 4], 3: [4] }, degree: 3
# check, for the elements that have the same length as degree
# which number has the shortest dist btwn them
def subarray_short(nums):
    # collections.defaultdict(list)
    # means: create a dict with default list values
    # such that when i access them straight away, the list is already created
    nums_dict, deg, minn = collections.defaultdict(list), 0, float('inf')
    for index, num in enumerate(nums):
        nums_dict[num].append(index)
        deg = max(deg, len(nums_dict[num]))
    for num, numlist in nums_dict.items():
        if len(numlist) == deg:
            minn = min(minn, numlist[-1] - numlist[0] + 1)
    return minn

print(subarray([1,2,2,3,1,4,2])) # 6 # deg = 3, subarr = [2,2,3,1,4,2]
print(subarray([1,2,2,3,1])) # 2 # deg = 2, subarr = [2,2]
print(subarray([1,1,2,3,1,4,2,2])) # 5 # deg = 3, subarr = [1,1,2,3,1]

print(subarray_short([1,2,2,3,1,4,2])) # 6 # deg = 3, subarr = [2,2,3,1,4,2]
print(subarray_short([1,2,2,3,1])) # 2 # deg = 2, subarr = [2,2]
print(subarray_short([1,1,2,3,1,4,2,2])) # 5 # deg = 3, subarr = [1,1,2,3,1]
