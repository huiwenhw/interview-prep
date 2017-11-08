## arr_ColumnNum.py:
'''
'''

import sys 

def get_column_num(string):
    base_ascii = ord('A')-1 # 65-1
    alphabets = 26 # 26-1
    col = 0
    rstr = string[::-1]
    for i in range(len(rstr)):
        curr_ascii = ord(rstr[i])
        diff = curr_ascii - base_ascii
        if i == 0:
            col = col + diff
        else:
            col = col + alphabets * diff * i
        #print('i ', i, ' str[i] ', rstr[i], ' currascii ', curr_ascii, ' diff ', diff, ' col ', col)
    return col

def main():
    # args = sys.argv[1:]
    # nums = [int(i) for i in args[0].split(",")]
    # target = int(args[1])
    print(get_column_num('A'))
    print(get_column_num('ZZ'))
    print(get_column_num('AAA'))

if __name__ == '__main__':
    main()

## arr_ConsecutiveSum.py:
'''
https://leetcode.com/problems/minimum-size-subarray-sum/description/

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''

import sys 

def subarr_sum(s, nums):
    # start from first element, let sum be first elem
    # if sum is smaller than s, continue expanding end 
    # if sum is >= s, keep track of # elem, move start to right
    if len(nums) == 0: return 0
    start = end = 0
    sumn  = nums[0]
    el = float('inf')
    while start <= end and end < len(nums):
        if sumn >= s:
            el = min(el, end-start+1)
            sumn -= nums[start]
            start += 1
        else:
            end += 1
            if end < len(nums):
                sumn += nums[end]
    if el == float('inf'):
        el = 0
    return el

    '''
    tracing:
    start = 0, 1, 2, 3
    end = 0, 1, 2, 3, 4, 5
    sumn = 2, 5, 6, 8, 6, 10, 7, 6, 
    el = inf, 4, 4, 3, 
    '''
def main():
    print(subarr_sum(7, [2,3,1,2,4,3])) # 2

if __name__ == '__main__':
    main()

## arr_ContainerWater.py:
'''
https://leetcode.com/problems/container-with-most-water/description/

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''

# want to find container with max height and max width btwn them 
# start from ends of array 
# shift shorter one in 
# keep checking the max 
# stop when we reach the middle 
def max_area(height):
    start, end = 0, len(height)-1
    m = -1
    # not <= cause dont have to check with itself, area will be 0
    while start < end:
        area = (end - start) * min(height[start], height[end])
        m = max(m, area)
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return m

print(max_area([4, 1, 3, 4])) # 12

## arr_ContainsDuplicate.py:
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

## arr_Degree.py:
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

## arr_FindMin.py:
'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
You may assume no duplicate exists in the array.

# Use binary search
'''

import sys

def findMin(nums):
    start, end = 0, len(nums)-1
    while start < end:
        mid = (start + end) / 2
        if nums[end] < nums[mid]:
            start = mid+1
        else:
            end = mid
    return nums[start]

def main():
    nums = sys.argv[1].split(",")
    nums = [int(i) for i in nums]
    print findMin(nums)

if __name__ == '__main__':
    main()

## arr_FindRotated.py:
'''
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

[1,3], 1 = 0
[3,1], 1 = 1
[4,5,6,7,8,1,2,3], 8 = 4
[1], 0 = -1
'''

import sys

# start <= end so i include the last element for checking
# for [3,1] 1 test case

# nums[start] <= nums[mid] to include  
# for [3,1] 1 test case
# with no = it'll be end=mid-1 but we want start=mid+1
def findRotated(nums, target):
    if len(nums) <= 0: return -1 
    start, end = 0, len(nums)-1
    while start <= end:
        mid = int((start + end) / 2)
        if nums[mid] == target: 
            return mid
        # ascending
        if nums[start] <= nums[mid]:
            if nums[start] <= target <= nums[mid]:
                end = mid-1
            else:
                start = mid+1
        # not ascending
        else:
            if nums[mid] <= target <= nums[end]:
                start = mid+1
            else:
                end = mid-1
    return -1
    
print(findRotated([4,5,6,7,8,1,2,3], 8)) # 4

## arr_MaxProductSubarray.py:
'''
https://leetcode.com/problems/maximum-product-subarray/description/

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
[-2,3,-4] = 24
'''

import sys

# Keep big and small product at each element
# cause we never know when a negative can become positive 
# check maxnum at the end 
def max_subarray_short(nums):
    if len(nums) <= 1: return nums[0]
    maxnum = big = small = nums[0]
    for num in nums[1:]:
        big, small = max(num, num*big, num*small), min(num, num*big, num*small)
        maxnum = max(maxnum, big)
    return maxnum

def main():
    nums = sys.argv[1].split(",")
    nums = [int(i) for i in nums]
    print max_subarray_short(nums)

if __name__ == '__main__':
    main()

## arr_MaxProfit.py:
'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Examples:
Input: [7, 1, 5, 3, 6, 4]
Output: 5
max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Input: [7, 6, 4, 3, 1]
Output: 0
In this case, no transaction is done, i.e. max profit = 0.
'''

import sys 

def max_profit(prices):
    length = len(prices)
    if length <= 1: return 0

    minp = prices[0]
    maxp = 0 
    diff = 0
    for i in range(length):
        if prices[i] < minp: 
            minp = prices[i]
        else: 
            curr_diff = prices[i] - minp
            if curr_diff > diff:
                diff = curr_diff
                maxp = prices[i]
    return diff

def max_profit_short(prices):
    maxp, minp = 0, float('inf')
    for price in prices:
        minp = min(minp, price)
        profit = price - minp
        maxp = max(maxp, profit) 
    return maxp 

def main():
    args = sys.argv[1:]
    prices = [int(i) for i in args[0].split(",")]
    print max_profit(prices)
    print max_profit_short(prices)

if __name__ == '__main__':
    main()

## arr_MaxSumSubarray.py:
'''
https://leetcode.com/problems/maximum-subarray/description/

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''

import sys

# maxind is to keep track of negative numbers
def max_subarray(nums):
    curr, maxnum, maxind = 0, 0, float('-inf')
    summed = False
    for num in nums:
        maxind = max(maxind, num)
        if curr + num < 0:
            curr = 0
        else: 
            curr = curr + num
        if curr > maxnum:
            summed = True
            maxnum = curr
    if summed: return maxnum
    return maxind

def max_subarray_short(nums):
    curr_sum = max_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)
        print num, curr_sum, max_sum
    return max_sum

def main():
    nums = sys.argv[1].split(",")
    nums = [int(i) for i in nums]
    print max_subarray(nums)
    print max_subarray_short(nums)

if __name__ == '__main__':
    main()

## arr_MinPathTree.py:
'''
https://leetcode.com/problems/triangle/description/
'''

def min_total(triangle):
    if len(triangle) == 0: return 0

    for 

## arr_MissingNumber.py:
'''
https://leetcode.com/problems/missing-number/

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
For example, 
Given nums = [0, 1, 3] return 2.
n = 3
'''

import sys

'''
def missing_number(nums):
    if len(nums) == 1:
        if nums[0] == 0:
            return 1
        return nums[0]-1
    mask = 1
    for num in nums:
        mask = mask | (1 << num)
        print num, mask
    print mask
    for i in range(len(nums)+1):
        if mask & (1 << i) == 0:
            return i
    return len(nums)
'''

def missing_number(nums):
    n = len(nums)
    return n*(n+1)/2 - sum(nums)

def main():
    nums = sys.argv[1].split(",")
    nums = [int(i) for i in nums]
    print missing_number(nums)

if __name__ == '__main__':
    main()

## arr_ProductExceptSelf.py:
'''
https://leetcode.com/problems/product-of-array-except-self/description/

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
'''

import sys

def productExceptSelf(nums):
    arr = []
    curr = 1
    for i in range(len(nums)):
        arr.append(curr)
        curr = curr * nums[i]
        print curr, nums[i]
    print arr
    curr = 1
    for i in range(len(nums)-1, -1, -1):
       arr[i] = arr[i] * curr
       curr = curr * nums[i]
    print arr
    return arr

def main():
    nums = sys.argv[1].split(",")
    nums = [int(i) for i in nums]
    print productExceptSelf(nums)

if __name__ == '__main__':
    main()

## arr_RectOverlap.py:
'''
'''

import sys 

def overlap(l1, r1, l2, r2):
    if (l1[0] > l2[0] and l1[0] > r2[0]) or (r1[0] < l2[0] and r1[0] < r2[0]):
        return False
    if (l1[1] < l2[1] and l1[1] < r2[1]) or (r1[1] > l2[1] and r1[1] > r2[1]):
        return False
    return True

def main():
    # args = sys.argv[1:]
    # nums = [int(i) for i in args[0].split(",")]
    # target = int(args[1])
    print(overlap([0,5], [5,0], [6, 3], [8,0]))
    print(overlap([0,5], [5,0], [3, 3], [8,0]))

if __name__ == '__main__':
    main()

## arr_ThreeSum.py:
"""
https://leetcode.com/problems/3sum/description/

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
    [-1, 0, 1],
    [-1, -1, 2]
]

run: python ThreeSum.py -1,0,1,2,-1,-4

Output:
[-4, -1, -1, 0, 1, 2]
enumerate:  0 -4
x  -1
x  -1
x  0
x  1
x  2
enumerate:  1 -1
x  -1
x  0
x  1
x  2
enumerate:  2 -1
enumerate:  3 0
x  1
x  2
[[-1, -1, 2], [-1, 0, 1]]
"""

import sys 

"""
def three_sum(nums):
    length = len(nums)
    if length < 3: return []
    pairs = {}
    for i in range(length):
        for k in range(i+1, length):
            pair_sum = nums[i] + nums[k]
            if pair_sum in pairs:
                pairs[pair_sum].append((i, k, nums[i], nums[k]))
            else: 
                pairs[pair_sum] = [(i, k, nums[i], nums[k])]
    print pairs
    ans = []
    ans_set = set()
    for i in range(length):
        diff = 0 - nums[i]
        print 'diff: ' + str(diff)
        if diff in pairs:
            pair_list = pairs[diff]
            print 'pairs: ' , pair_list
            for k in range(len(pair_list)):
                if i != pair_list[k][0] and i != pair_list[k][1]:
                    tuples = pair_list[k][2:] + (nums[i],)
                    print tuples
                    print sorted(tuples)
                    tuples = tuple(sorted(tuples))
                    ans_set.add(tuples)
    return list(ans_set)
"""

def three_sum_short(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    print nums
    for i, num in enumerate(nums[:-2]):
        print 'enumerate: ', i, num
        # skip if previous num is same as the current
        # cause that means we'll be adding the same stuff to set / dict
        if i >= 1 and num == nums[i-1]:
            continue
        d = {}
        for x in nums[i+1:]:
            print 'x ', x
            # n1 + n2 + x = 0
            # x = 0 - n1 - n2 (what - num - x mean)
            if x not in d:
                d[-num-x] = 1
            else:
                res.add((num, -num-x, x))
    return map(list, res)

def main():
    nums = sys.argv[1].split(",")
    nums = [int(num) for num in nums]
    # print three_sum(nums)
    print three_sum_short(nums)

if __name__ == '__main__':
    main()

## arr_TwoSum.py:
'''
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

import sys 

def two_sum(nums, target):
    i = 0
    length = len(nums)
    while i < length:
        k = i+1
        while k < length:
            if nums[i] + nums[k] == target:
                return [i, k]
            k += 1
        i += 1

def two_sum_dict(nums, target):
    nums_dict = {}
    for i in range(len(nums)):
        if nums[i] in nums_dict:
            return [nums_dict[nums[i]], i]
        nums_dict[target - nums[i]] = i

def main():
    args = sys.argv[1:]
    nums = [int(i) for i in args[0].split(",")]
    # nums = map(int, args[0].split(","))
    target = int(args[1])
    # print two_sum(nums, target)
    print two_sum_dict(nums, target)

if __name__ == '__main__':
    main()

## bin_CountBits.py:
'''
https://leetcode.com/problems/counting-bits/description/

Given a non negative integer number num. For every numbers i in the range 0 <= i <= num calculate the number of 1's in their binary representation and return them as an array.
Example:
For num = 5 you should return [0,1,1,2,1,2]

[0]
[0, 1]
[0, 1]
[0, 1, 1, 2]
[0, 1, 1, 2]
[0, 1, 1, 2, 1, 2, 2, 3]
[0, 1, 1, 2, 1, 2, 2, 3]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
ans: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]
'''

import sys

def count_bits(num):
    ans = []
    for n in range(num+1):
        count = 0
        while n:
            n &= n-1
            count += 1
        ans.append(count)
    return ans

def count_bits_short(num):
    res=[0]
    while len(res)<=num:
        print res
        res += [i+1 for i in res]
        print res
    return res[:num+1]

def main():
    num = int(sys.argv[1])
    print count_bits(num)
    print count_bits_short(num)

if __name__ == '__main__':
    main()

## bin_HammingWeight.py:
'''
https://leetcode.com/problems/number-of-1-bits/description/

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3
'''

import sys

def hamming_weight(num):
    binary = "{0:b}".format(num)
    count = 0
    for bit in binary:
       if bit == '1':
        count += 1 
    return count

def hamming_weight_short(num):
    count = 0
    while num:
        num = num & (num-1)
        count += 1
    return count

def hamming_weight_supershort(num):
    return bin(num).count('1')

def main():
    num = int(sys.argv[1])
    print hamming_weight(num)
    print hamming_weight_short(num)
    print hamming_weight_supershort(num)

if __name__ == '__main__':
    main()

## bin_ReverseBits.py:
'''
https://leetcode.com/problems/reverse-bits/description/

Reverse bits of a given 32 bits unsigned integer.
For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
'''

import sys

def reverse_bits(num):
    binary ="{0:b}".format(num)
    # pad zereos in front! 
    binary = '0' * (32-len(binary)) + binary
    # reverse string and convert to int
    reverse = binary[::-1]
    return int(reverse, 2)

# or, we could do a 32 bits format 
def reverse_bits_short(num):
    binary ="{0:032b}".format(num)
    reverse = binary[::-1]
    return int(reverse, 2)

def main():
    num = int(sys.argv[1])
    print reverse_bits(num)
    print reverse_bits_short(num)

if __name__ == '__main__':
    main()

## dp_Steps.py:
"""
A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

// input = 3, ouput is 4 ways
// input = 4, ouput is 7 ways

Note:
Approach 1) Implement the solution recursively.
Approach 2) dynamic programming (top down approach - memoization)
Approach 3) dynamic programming (bottom up approach)
"""

import sys 

def ways(n, steps):
    # print n, steps
    if steps == n:
        # print 'return'
        return 1
    if steps > n:
        return 0
    return ways(n, steps+1) + ways(n, steps+2) + ways(n, steps+3)

# array stores the number of ways to reach that step 
# e.g. arr[2] : # ways to reach 2 steps 
def top_down(arr, n, steps):
    print n, steps
    if steps == n:
        print 'return 1'
        return 1
    if steps > n:
        print 'return 0'
        return 0
    if arr[steps]: 
        print 'return arr[steps]: ' + str(arr[steps])
        return arr[steps]
    arr[steps] = top_down(arr, n, steps+1) + top_down(arr, n, steps+2) + top_down(arr, n, steps+3)
    print 'steps: ' + str(steps) + ' arr[steps]: ' + str(arr[steps])
    return arr[steps] # mistake was to return arr[0]

# usually using for loops 
def bottom_up(n):
   return '' 

def main():
    arg = sys.argv[1]
    n = int(arg)
    print ways(n, 0)
    arr = [0] * (n)
    print top_down(arr, n, 0)

if __name__ == '__main__':
    main()

## graph_CloneGraph.py:
'''
https://leetcode.com/problems/clone-graph/description/
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
'''

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# keep a visited dictionary
# traverse through neighbor list
# if neighbor hasnt been visited, add it to visited and queue
# add neighbor to currently clone-ing neighbor list
def clone_bfs(node):
    if not node:
        return node
    q = []
    visited = {node: UndirectedGraphNode(node.label)}
    q.append((node, visited[node]))
    while q:
        curr, clone = q.pop(0)
        for n in curr.neighbors:
            if n not in visited:
                visited[n] = UndirectedGraphNode(n.label)
                q.append((n, visited[n]))
            clone.neighbors.append(visited[n])
    return visited[node]

# keep a visited dictionary
# if node is visited, then return cloned node
# else, create a clone node from current node 
# add it to visited
# for each neighbor, dfs and append returned node/clone to neighbor list
# if no/no more neighbors, return clone
def clone_dfs(node):
    if not node:
        return node
    visited = {}

    def dfs(node, visited):
        if node in visited:
            return visited[node]

        clone = UndirectedGraphNode(node.label)
        visited[node] = clone

        for n in node.neighbors:
            clone.neighbors.append(dfs(n, visited))
        return clone 
    return dfs(node, visited)

def dfs_start(node):
    if not node:
        return node
    visited = {}
    def dfs(node, visited):
        visited[node] = True
        print(node.label)
        for n in node.neighbors:
            if n not in visited:
                dfs(n, visited)
    dfs(node, visited)

# keep a hash to keep track of visited nodes
def bfs(node):
    q = [node]
    visited = {node: True}
    ans = '' 
    while q:
        curr = q.pop(0)
        ans += str(curr.label) + ' '
        neighbors = curr.neighbors
        for n in curr.neighbors:
            if n not in visited:
                visited[n] = True
                q.append(n)
    print(ans)

node = UndirectedGraphNode(1)
a = UndirectedGraphNode(2)
b = UndirectedGraphNode(3)
c = UndirectedGraphNode(4)
node.neighbors = [a, b, c]

d = UndirectedGraphNode(5)
e = UndirectedGraphNode(6)
a.neighbors = [d, e]

first = UndirectedGraphNode(-1)
one = UndirectedGraphNode(1)
first.neighbors = [one]
#bfs(clone_bfs(first))
#dfs_start(clone_bfs(node))
dfs_start(clone_dfs(node))

## graph_CourseSchedule.py:
'''
https://leetcode.com/problems/course-schedule/description/

There are a total of n courses you have to take, labeled from 0 to n - 1. Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

e.g. 2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
ans: https://discuss.leetcode.com/topic/13412/python-20-lines-dfs-solution-sharing-with-explanation/5
'''

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def can_finish(numCourses, prerequisites):
    adjlist = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]

    # build adjlist
    for edge in prerequisites:
        x, y = edge
        adjlist[x].append(y)
    
    def dfs(i, visited, adjlist):
        # if node is being visited, means there's a cycle, ret False
        if visited[i] == -1:
            return False
        # node is visited, don't need to visit again, ret true
        if visited[i] == 1:
            return True
        # mark as being visited
        visited[i] = -1
        # visit each neighbor
        neighbors = adjlist[i]
        for n in neighbors:
            if not dfs(n, visited, adjlist):
                return False
        # mark visited when all neighbors are visited
        visited[i] = 1
        return True

    # visit each node
    for i in range(numCourses):
        if not dfs(i, visited, adjlist):
            return False
    return True

print(can_finish(2, [[1,0]])) # True
print(can_finish(3, [[1,0],[2,0]])) # True
print(can_finish(3, [[0,1],[0,2],[1,2]])) # True
print(can_finish(2, [[1,0],[0,1]])) # False
print(can_finish(4, [[0,1],[1,2],[2,3]])) # True
print(can_finish(4, [[1,0],[2,1],[3,2],[1,3]])) # False
print(can_finish(4, [[0,1],[1,2],[0,3],[3,0]])) # False

## graph_PacificAtlantic.py:
'''
https://leetcode.com/problems/pacific-atlantic-water-flow/description/

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
'''

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

# keep two bool matrix for pacific and atlantic
# start from the sides in 
# Check if current index is <= next index. If yes, then dfs 
# loop through both matrix and check if node is True on both matrix
# True, means node is reachable from both sides. add to list
def pacific_atlantic(matrix):
    if not matrix: return []
    rows, cols = len(matrix), len(matrix[0])
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    p_visited = [[False for _ in range(cols)] for _ in range(rows)]
    a_visited = [[False for _ in range(cols)] for _ in range(rows)]
    result = []

    def dfs(i, j, visited):
        visited[i][j] = True
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols and matrix[i][j] <= matrix[next_i][next_j] and not visited[next_i][next_j]:
                dfs(next_i, next_j, visited)

    for i in range(rows):
        dfs(i, 0, p_visited)
        dfs(i, cols-1, a_visited)
    for j in range(cols):
        dfs(0, j, p_visited)
        dfs(rows-1, j, a_visited)
    
    for i in range(rows):
        for j in range(cols):
            if p_visited[i][j] and a_visited[i][j]:
                result.append([i, j])
    return result

def traverse_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    
    # right, up, left, down
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(i, j):
        if (i, j) in visited:
            return 
        visited.add((i, j))
        print('i ', i, ' j ', j, ' matrix[i][j] ', matrix[i][j])
        for direction in directions:
            next_i, next_j = i+direction[0], j+direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                dfs(next_i, next_j)

    for i in range(rows):
        for j in range(cols):
            dfs(i, j)

matrix = [[1,2,2,3,5], [3,2,3,4,4], [2,4,5,3,1], [6,7,1,4,5], [5,1,1,2,4]]
print(pacific_atlantic(matrix))

## Inorder.py:
# Definition for a binary tree node.
# class TreeNode(object):
#   def __init__(self, x):
#   	self.val = x
#     self.left = None
#     self.right = None

class Solution(object):
    # append doesn't return a new list 
    # so we can't do first.append(root.val) + second
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
			
	first = Solution.inorderTraversal(self, root.left)
	first.append(root.val)
	second = Solution.inorderTraversal(self, root.right)
        return first + second

    def inorder_short(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
			
        return Solution.inorder_short(self, root.left) + [root.val] + Solution.inorder_short(self, root.right)

## ll_DetectCycle.py:
'''
https://leetcode.com/problems/linked-list-cycle/description/

Given a linked list, determine if it has a cycle in it.
Follow up: Can you solve it without using extra space?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# save encountered nodes to a dict and check 
# note: use the ListNode as the key instead of its value
# as there can be duplicate elements
# O(n) time, O(n) space
def detect_cycle(head):
    seen = {}
    index = 0
    while head:
        if head in seen:
            return True
        seen[head] = True
        head = head.next
        index += 1
    return False

# without using extra space:
# changed the value of nodes, which.. probably isn't recommended 
# O(n) time, O(1) space
def detect_cycle_short(head):
    dummy = ListNode(float('inf'))
    while head:
        if head.val == dummy.val:
            return True
        head.val = dummy.val
        head = head.next
    return False

# O(n) time, O(1) space
# will throw exception if fast.next.next is None, 
# and that means we don't have a cycle. so return False
def detect_cycle_s(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

# without using exceptions:
def detect_cycle_ss(head):
    slow = fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True
    return False


head = ListNode(1)
head.next = head

print(detect_cycle(head))
print(detect_cycle_s(head))
print(detect_cycle_short(head))

## ll_MergeKLists.py:
'''
https://leetcode.com/problems/merge-k-sorted-lists/description/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# add elements to min-heap
# while heap, pop min, add min to new list
# return list
# complexity: let n be total num of elements.
# O(n log(n)) time complexity O(n) space complexity
def merge(lists):
    minheap = [] 
    dummyhead = dummy = ListNode(float('inf'))
    while True:
        count = 0
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minheap, lists[i].val)
                lists[i] = lists[i].next
                count += 1
        if count == 0:
            break
    while minheap:
        num = heapq.heappop(minheap)
        dummy.next = ListNode(num)
        dummy = dummy.next
    return dummyhead.next

from queue import PriorityQueue

# add first elements of list to priority queue
# while queue is not empty, 
# add next element of smallest element in priority queue to q
# this will ensure we're adding the smaller elements from each list first 
# complexity: let n be total num of elements.
# : O(n log(k)) time and O(k) space complexity
def merge_pqueue(lists):
    dummyhead = dummy = ListNode(float('inf'))
    q = PriorityQueue()
    for node in lists:
        if node:
            q.put((node.val, node))
    while q.qsize() > 0:
        dummy.next = q.get()[1]
        dummy = dummy.next
        if dummy.next: 
            q.put((dummy.next.val, dummy.next))
    return dummyhead.next

def printlist(head): 
    ans = ''
    while head:
        ans += str(head.val) + ' '
        head = head.next
    print(ans)

head = ListNode(-3)
head.next = ListNode(-2)
head.next.next = ListNode(-1)
head.next.next.next  = ListNode(4)
head.next.next.next.next = ListNode(5)

head1 = ListNode(-5)
head1.next = ListNode(1)
head1.next.next = ListNode(2)
head1.next.next.next = ListNode(3)

printlist(merge([head, head1]))
printlist(merge_pqueue([head, head1]))

## ll_MergeSortedList.py:
'''
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def merge_list_short(l1, l2):
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = merge_list_short(l1.next, l2)
    return l1 or l2


def printlist(head):
    ans = ''
    while head:
        ans += str(head.val) + ' '
        head = head.next
    print(ans)

l1 = ListNode(2)
l2 = ListNode(1)

printlist(merge_list_short(l1, l2)) # 1 2

## ll_PartitionList.py:
'''
https://leetcode.com/problems/partition-list/description/
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# keep two dummy pointers 
# one for nodes with values < x 
# another for nodes with values >= x 
# stitch left to right, return dummyleft.next
def partition(head, x):
    dummyleft = left = ListNode(float('inf'))
    dummyright = right = ListNode(float('inf'))
    
    while head:
        if head.val < x:
            left.next = head
            left = left.next
        else:
            right.next = head
            right = right.next
        head = head.next
    right.next = None
    left.next = dummyright.next
    return dummyleft.next

def printlist(head): 
    ans = ''
    while head:
        ans += str(head.val) + ' '
        head = head.next
    print(ans)

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next  = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

head1 = ListNode(2)
head1.next = ListNode(1)

printlist(partition(head1, 2))
printlist(partition(head, 3))

## ll_RemoveNthFromList.py:
'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given a linked list, remove the nth node from the end of list and return its head.
Given linked list: 1->2->3->4->5, and n = 2
After removing the second node from the end, the linked list becomes 1->2->3->5.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_nth(head, n):
    prev = dummy = ListNode(float('inf'))
    prev.next = slow = fast = head
    if head.next is None:
        return None
    for i in range(n):
        fast = fast.next
    while fast:
        prev = prev.next
        slow = slow.next
        fast = fast.next
    if prev == dummy:
        head = slow.next
    else:
        prev.next = slow.next
    return head

# without using dummy node 
# if fast is None, just return head.next 
# means we're removing the first element
def remove_nth_short(head, n):
    slow = fast = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
    
def printlist(head):
    ans = ''
    while head:
        ans += str(head.val) + ' '
        head = head.next
    print(ans)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next  = ListNode(4)
head.next.next.next.next = ListNode(5)

head1 = ListNode(1)

head2 = ListNode(1)
head2.next = ListNode(2)

printlist(remove_nth(head, 2)) # 1 2 3 5 
printlist(remove_nth(head1, 1)) # None
printlist(remove_nth(head2, 2)) # 2

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next  = ListNode(4)
head.next.next.next.next = ListNode(5)

head1 = ListNode(1)

head2 = ListNode(1)
head2.next = ListNode(2)
printlist(remove_nth_short(head, 2)) # 1 2 3 5 
printlist(remove_nth_short(head1, 1)) # None
printlist(remove_nth_short(head2, 2)) # 2

## ll_ReorderList.py:
'''
https://leetcode.com/problems/reorder-list/description/
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.
For example, Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# get the middle using slow/fast pointer
# mid, midsec
# reverse the second half using midsec pointer
# 1 2 3 # head: 1, 2. last: 3
# link mid1 - mid while both is not None
# do it in-place, dont return anything
def reorder(head):
    if not head or not head.next:
        return

    # find mid+1 point
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    midsec = slow.next
    slow.next = None
    printlist(head) # 1 2 3 
    printlist(midsec) # 4 5 

    # reverse second half (midsec)
    prev = None
    while midsec:
        curr = midsec
        midsec = midsec.next
        curr.next = prev
        prev = curr
    last = prev
    printlist(last) # 5 4
    
    # link them together
    while head and last:
        curr1, curr2 = head, last
        head, last = head.next, last.next
        curr1.next, curr2.next = curr2, curr1.next
     
def printlist(head): 
    ans = ''
    while head:
        ans += str(head.val) + ' '
        head = head.next
    print(ans)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next  = ListNode(4)
head.next.next.next.next = ListNode(5)

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
reorder(head)  
printlist(head) # 1 5 2 4 3
reorder(head1) 
printlist(head1) # 1 4 2 3 

## ll_ReverseList.py:
'''
https://leetcode.com/problems/reverse-linked-list/description/

Reverse a singly linked list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# head -> next node | head -> next node 
# want to make the nextnode point to head 
# at every node i'll have head and next 
# want to make next.next = head 
# need to keep pointer of next.next 
# if next node is None, then i stop and return head 
# have the head of the list 
def reverse_list(head):
    prev = None
    nnext = head.next
    while head is not None:
        head.next = prev
        if nnext is not None:
            temp = nnext.next
            nnext.next = head
            #update 
            prev = head
            head = nnext
            nnext = temp
        else:
            break
    return head

# only do it for one node 
def reverse_list_short(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

head = ListNode(1)
head.next = ListNode(2)

print(reverse_list(head).val) # 2
print(reverse_list_short(head).val) # 1 (reversed list)

## math_facTrailingZeroes.py:
'''
https://leetcode.com/problems/factorial-trailing-zeroes/description/

Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
'''

# every 5 * 2 creates a trailing 0
# every 5 factor creates a 0 
# so we count the number of 5, 5*5, 5*5*5 etc. in the n
def trailing(n):
    count = 0
    while n > 0:
        n = n / 5
        count += n
    return count

def trailing_recur(n):
    if n == 0: return 0
    return n/5 + trailing_recur(n/5)

print(trailing(25)) # 6
print(trailing_recur(25)) # 6

## RectArea.py:
"""
https://leetcode.com/problems/rectangle-area/description/

Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
"""

# know right > left
def compute_area(A, B, C, D, E, F, G, H):
    # check if rects overlap 
    overlap = x = y = total = 0
    if E >= C or G <= A:
        overlap = 0
    elif F >= D or H <= B:
        overlap = 0
    else: 
        # 4 cases
        # R1 x inside R2 
        # R1 right x inside R2 
        # R1 left x inside R2
        # R1 x outside R2 
        if A >= E and C <= G:
            x = C - A 
        elif E <= C <= G:
            x = C - E 
        elif E <= A <= G:
            x = G - A
        else:
            x = G - E

        # 4 cases
        # R1 y inside R2 
        # R1 top y inside R2 
        # R1 bottom y inside R2
        # R1 y outside R2 
        if B >= F and D <= H:
            y = D - B
        elif F <= D <= H:
            y = D - F
        elif F <= B <= H:
            y = H - B
        else:
            y = H - F

    overlap = x * y
    total = (C-A)*(D-B) + (G-E)*(H-F) - overlap
    return total

def compute_area_short(A, B, C, D, E, F, G, H):
    # check if rects overlap 
    overlap = x = y = total = 0
    if E >= C or G <= A:
        overlap = 0
    elif F >= D or H <= B:
        overlap = 0
    else: 
        x = min(G, C) - max(E, A)
        y = min(D, H) - max(B, F)
    
    overlap = x * y
    total = (C-A)*(D-B) + (G-E)*(H-F) - overlap
    return total 

def main():
    print(compute_area(-3, 0, 3, 4, 0, -1, 9, 2)) # 45
    print(compute_area(-2, -2, 2, 2, 3, -4, 4, -3)) # 17 
    print(compute_area(-5, 4, 0, 5, -3, -3, 3, 3)) # 41
    print(compute_area_short(-3, 0, 3, 4, 0, -1, 9, 2)) # 45
    print(compute_area_short(-2, -2, 2, 2, 3, -4, 4, -3)) # 17 
    print(compute_area_short(-5, 4, 0, 5, -3, -3, 3, 3)) # 41

if __name__ == '__main__':
    main()

## recur_Subsets.py:
'''
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
    return ans

print(subsets([1,2,3])) # [[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]
print(subsets_short([1,2,3])) # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


## recur_SubsetsDuplicate.py:
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

## script.py:
import glob

read_files = glob.glob("*.py")

with open("result.py", "w") as outfile:
    for f in read_files:
        with open(f, "r") as infile:
            outfile.write("## " + f + ":\n")
            outfile.write(infile.read())
            outfile.write("\n")

## tree_Buildtree.py:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if preorder == []:
        return None
    if len(inorder) == 1: 
        return TreeNode(inorder[0])

    root = preorder[0]
    rootindex = inorder.index(root)
    leftinorder = inorder[:rootindex]
    len_left = len(leftinorder)
    rightinorder = inorder[rootindex+1:]
    len_right = len(rightinorder)

    root = TreeNode(root)
    root.left = build_tree(preorder[1:len_left+1], leftinorder)
    root.right = build_tree(preorder[len_left+1:len_left+1+len_right], rightinorder)
    return root

def level_order(root):
    index = 0
    ans, queue = [], [(root, index)]
    while queue:
        node, level = queue.pop(0)
        if node:
            if len(ans) == level:
                ans.append([])
            ans[level] = ans[level] + [node.val]
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
    return ans

preorder = [8,5,9,7,1,12,2,4,11,3]
inorder = [9,5,1,7,2,12,8,4,3,11]
root = build_tree(preorder, inorder)
print(level_order(root))

## tree_InvertTree.py:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
:type root: TreeNode
:rtype: List[int]p
"""
def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def invert_tree(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left 

    invert_tree(root.left)
    invert_tree(root.right)
    return root

def invert_tree_short(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
        return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('invert tree, printed using preorder')
print(preorder(invert_tree(root)))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(preorder(invert_tree_short(root)))

## tree_KSmallest.py:
'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# check left children. if found, return left immediately 
# else, left child returned, add 1 to count and check == k
# check right children. if found, return immediately
# return (node, count, true), keep a boolean to check if element has been found 
# check if boolean is true first
# check if node is none, return count 
def kth_smallest(root, k):
    def kth(node, k, count, found):
        if found or node is None:
            return (node, count, found)
        lnode, count, found = kth(node.left, k, count, found)
        if found:
            return (lnode, count, found)
        else: 
            count += 1
            if count == k:
                return (node, count, True)
        rnode, count, found = kth(node.right, k, count, found)
        if rnode and found:
            return (rnode, count, True)
        return (node, count, found)
    return kth(root, k, 0, False)[0].val

# or just use inorder and check! 
def kth_smallest_short(root, k):
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            if k == 1:
                return root.val
            k -= 1
            root = root.right


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

root1 = TreeNode(1)
root1.right = TreeNode(2)

root2 = TreeNode(2)
root2.left = TreeNode(1)

print('kth smallest: ', kth_smallest(root, 4)) # 4?
print('kth smallest: ', kth_smallest(root1, 2)) # 2
print('kth smallest: ', kth_smallest(root2, 1)) # 1 
print('kth smallest: ', kth_smallest_short(root, 4)) # 4?
print('kth smallest: ', kth_smallest_short(root1, 2)) # 2
print('kth smallest: ', kth_smallest_short(root2, 1)) # 1 

## tree_LevelOrderTraversal.py:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def level_order(root):
    index = 0
    ans, queue = [], [(root, index)]
    while queue:
        node, level = queue.pop(0)
        if node:
            if len(ans) == level:
                ans.append([])
            ans[level] = ans[level] + [node.val]
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
    return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('level order')
print(level_order(root))

## tree_LowestCommonAncestor.py:
'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
                   _______6______
                  /              \
               ___2__          ___8__
              /      \        /      \
             0      _4       7       9
                   /  \
                  3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# check if value is p or q 
# if it is, return p or q
# if both left and right children have value, means p and q is found 
# return current node 
# else, return left or right 
def lowest(root, p, q):
    if root is None:
        return None

    if root.val == p.val:
        return p
    elif root.val == q.val:
        return q

    left = lowest(root.left, p, q)
    right = lowest(root.right, p, q)

    if left and right:
        return root
    return left or right

# if both p and q are smaller than root, go left subtree to check
# if both p and q are larger than root, go right subtree to check
# else, p and q are left children or
# p is root and q is child || q is root and p is child
def lowest_short(root, p, q):
    if p.val < root.val and q.val < root.val:
        return lowest_short(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowest_short(root.right, p, q)
    return root

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)

p = TreeNode(2)
q = TreeNode(8)

print(lowest(root, p, q).val)
print(lowest_short(root, p, q).val)

## tree_MaxDepth.py:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_depth(root):
    if root is None:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('max depth of tree: ', max_depth(root))

## tree_MaxPathSum.py:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# want to compare right and left, return max 
# keep maxsum check at each node 
# dfs returns both
def max_path_sum(root):
    def dfs(node):
        left = right = 0
        leftsum = rightsum = float('-inf')
        if node.left:
            left, leftsum = dfs(node.left)
            left = max(left, 0)
        if node.right:
            right, rightsum = dfs(node.right)
            right = max(right, 0)
        return node.val + max(left, right), max(node.val + left + right, leftsum, rightsum)
    if root:
        return dfs(root)[1]
    return 0


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('max path sum')
print(max_path_sum(root))

## tree_SameTree.py:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def same_tree(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)

def same_tree_iter(p, q):
    stack = [(p, q)]
    while stack:
        n, m = stack.pop()
        if n and m:
            if n.val != m.val:
                return False
            stack.append((n.right, m.right))
            stack.append((n.left, m.left))
        elif n is not m:
            return False
    return True

def same_tree_short(p, q):
    # checking if both nodes are None
    if p and q:
        return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)
    # checking p == q, but using reference 
    return p is q

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('same tree')
print(same_tree(root, root))
print(same_tree_iter(root, root))
print(same_tree_short(root, root))

## tree_Serialise.py:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialise(root):
    def doit(node):
        if node:
            vals.append(str(node.val))
            doit(node.left)
            doit(node.right)
        else:
            vals.append('#')
    vals = []
    doit(root)
    print(' '.join(vals))
    return ' '.join(vals)

def deserialise(data):
    def doit():
        val = next(vals)
        print('val ', val, ' vals ', vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = doit()
        node.right = doit()
        print('node ', node.val)
        return node
    vals = iter(data.split())
    print(data.split())
    return doit()

'''
def serialise(root):
    ans, queue = "", [root]
    while queue:
        node = queue.pop(0)
        if node:
            ans += str(node.val) + ","
            queue.append(node.left)
            queue.append(node.right)
    return ans[:-1]

def deserialise(data):
    if data == '': return TreeNode(data)
    qdata = data.split(",")
    queue = []
    for num in qdata:
        if num == 'None':
            queue.append(None)
        else:
            queue.append(int(num))
    print(queue)

    pointer, length = 0, len(queue)
    node = TreeNode(queue[0])
    queue[0] = node
    for i in range(length):
        node = queue[i]
        if pointer == 0: root = node
        print('node.val ', node.val)
        if node.val is None:
            print('pointer - i ', i, ' pointer ', pointer)
            pointer -= 1
        else:
            print('pointer + i ', i, ' pointer ', pointer)
            pointer += 1
        
            print('i ', i, ' pointer ', pointer)
            if i+pointer < length:
                left = queue[i+pointer]
                node.left = TreeNode(left)
                queue[i+pointer] = node.left
            if i+pointer+1 < length:
                right = queue[i+pointer+1]
                node.right = TreeNode(right)
                queue[i+pointer+1] = node.right
            print('current ', queue[i].val, ' left ', left, ' right ', right)
    return root
 '''
 
def level_order(root):
    index = 0
    ans, queue = [], [(root, index)]
    while queue:
        node, level = queue.pop(0)
        if node:
            if len(ans) == level:
                ans.append([])
            ans[level] = ans[level] + [node.val]
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
    return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

ans = deserialise(serialise(root))
print(level_order(ans))

'''
root = deserialise("5,4,7,3,None,2,None,-1,None,9")
print(level_order(root))
print(serialise(root))
'''

## tree_Subtree.py:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_subtree(s, t):
    def sametree(p, q):
        if p and q:
            return p.val == q.val and sametree(p.left, q.left) and sametree(p.right, q.right)
        return p is q

    if s is None:
        return False
    if sametree(s, t):
        return True
    return is_subtree(s.left, t) or is_subtree(s.right, t)
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
print(is_subtree(root, root2))

## tree_TreeTraversals.py:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
:type root: TreeNode
:rtype: List[int]p
"""
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def inorder_iter(root):
    if root is None: return []
    stack, visited = [root], []
    while stack:
        root = stack[-1]
        if root.left:
            stack.append(root.left)
            root.left = None # so that it will not add back the same node
        else:
            visited.append(stack.pop().val)
            if root.right:
                stack.append(root.right)
                root.right = None 
    return visited

def inorder_iter_short(root):
    visited, stack = [], []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            temp = stack.pop()
            visited.append(temp.val)
            root = temp.right
    return visited

def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def preorder_iter(root):
    ans, stack = [], []
    while stack or root:
        if root:
            ans.append(root.val)
            stack.append(root)
            root = root.left
        else:
            temp = stack.pop()
            root = temp.right
    return ans

# add root to ans, then add right and left child 
# always pop left child first
def preorder_iter_short(root):
    ans, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            ans.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return ans

def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

def postorder_iter(root):
    ans, stack = [], [(root, False)]
    while stack:
        node, visited_twice = stack.pop()
        if node:
            if visited_twice:
                ans.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('inorder')
print(inorder(root))
print(inorder_iter(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(inorder_iter_short(root))

print('preorder')
print(preorder(root))
print(preorder_iter(root))
print(preorder_iter_short(root))

print('postorder')
print(postorder(root))
print(postorder_iter(root))

## tree_ValidBST.py:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_valid_bst(root):
    def is_valid(node):
        if node is None:
            return (node, float('inf'), float('-inf'), True)
        lnode, lmin, lmax, lbool = is_valid(node.left)
        if lnode:
            if lnode.val >= node.val or lmax >= node.val:
                return (node, lmin, lmax, False)
            lmin, lmax = min(lmin, lnode.val),  max(lmax, lnode.val)
        rnode, rmin, rmax, rbool = is_valid(node.right)
        if rnode:
            if rnode.val <= node.val or rmin <= node.val:
                return (node, rmin, rmax, False)
            rmin, rmax = min(rmin, rnode.val), max(rmax, rnode.val)
        return (node, min(lmin, rmin), max(lmax, rmax), lbool == rbool)
    return is_valid(root)[3]

def is_valid_short(root):
    def is_valid(node, nmin, nmax):
        if not node:
            return True
        if node.val >= nmin or node.val <= nmax:
            return False
        return is_valid(node.left, min(nmin, node.val), nmax) and is_valid(node.right, nmin, max(nmax, node.val))
    return is_valid(root, float('inf'), float('-inf'))

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)

print('is valid bst: ', is_valid_bst(root))
print('is valid bst: ', is_valid_short(root))

## trees.py:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
:type root: TreeNode
:rtype: List[int]p
"""
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def inorder_iter(root):
    if root is None: return []
    stack, visited = [root], []
    while stack:
        root = stack[-1]
        if root.left:
            stack.append(root.left)
            root.left = None # so that it will not add back the same node
        else:
            visited.append(stack.pop().val)
            if root.right:
                stack.append(root.right)
                root.right = None 
    return visited

def inorder_iter_short(root):
    visited, stack = [], []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            temp = stack.pop()
            visited.append(temp.val)
            root = temp.right
    return visited

def preorder(root):
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def preorder_iter(root):
    ans, stack = [], []
    while stack or root:
        if root:
            ans.append(root.val)
            stack.append(root)
            root = root.left
        else:
            temp = stack.pop()
            root = temp.right
    return ans

# add root to ans, then add right and left child 
# always pop left child first
def preorder_iter_short(root):
    ans, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            ans.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return ans

def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

def postorder_iter(root):
    ans, stack = [], [(root, False)]
    while stack:
        node, visited_twice = stack.pop()
        if node:
            if visited_twice:
                ans.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return ans
                
def max_depth(root):
    if root is None:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1

def same_tree(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)

def same_tree_iter(p, q):
    stack = [(p, q)]
    while stack:
        n, m = stack.pop()
        if n and m:
            if n.val != m.val:
                return False
            stack.append((n.right, m.right))
            stack.append((n.left, m.left))
        elif n is not m:
            return False
    return True

def same_tree_short(p, q):
    # checking if both nodes are None
    if p and q:
        return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)
    # checking p == q, but using reference 
    return p is q

def invert_tree(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left 

    invert_tree(root.left)
    invert_tree(root.right)
    return root

def invert_tree_short(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
        return root

def level_order(root):
    index = 0
    ans, queue = [], [(root, index)]
    while queue:
        node, level = queue.pop(0)
        if node:
            if len(ans) == level:
                ans.append([])
            ans[level] = ans[level] + [node.val]
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
    return ans

'''
def max_path_sum(root):
    ans, stack = [], [(root, None, False)]
    c1, c2, curr, maxsum, curr_parent = 0, 0, 0, 0, None
    while stack:
        node, parent, visited_twice = stack.pop()
        if node: 
            print('node ', node.val, ' visited_twice ', visited_twice)
            print('c1 ', c1, ' c2 ', c2, ' maxsum ', maxsum)
            if parent is None and visited_twice:
                maxsum = max(maxsum, node.val + c1 + c2)
            elif visited_twice:
                if c1 is None and c2 is None:
                    curr_parent = parent
                elif parent == curr_parent:
                    if c1 is None:
                        c1 = node.val
                    elif c2 is None:
                        c2 = node.val
                else:
                    curr_parent = parent
                    maxsum = max(node.val + c1 + c2, maxsum)
                    c1 = max(node.val + c1, node.val + c2)
                    c2 = 0
                print('in visited node ', node.val, ' parent ', parent.val , ' visited_twice ', visited_twice)
                print('in visited c1 ', c1, ' c2 ', c2, ' maxsum ', maxsum, ' currparent ', curr_parent.val)
            else:
                stack.append((node, parent, True))
                stack.append((node.right, node, False))
                stack.append((node.left, node, False))
    return maxsum
'''

# want to compare right and left, return max 
# keep maxsum check at each node 
# dfs returns both
def max_path_sum(root):
    def dfs(node):
        left = right = 0
        leftsum = rightsum = float('-inf')
        if node.left:
            left, leftsum = dfs(node.left)
            left = max(left, 0)
        if node.right:
            right, rightsum = dfs(node.right)
            right = max(right, 0)
        return node.val + max(left, right), max(node.val + left + right, leftsum, rightsum)
    if root:
        return dfs(root)[1]
    return 0


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('inorder')
print(inorder(root))
print(inorder_iter(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(inorder_iter_short(root))

print('preorder')
print(preorder(root))
print(preorder_iter(root))
print(preorder_iter_short(root))

print('postorder')
print(postorder(root))
print(postorder_iter(root))

print('max depth of tree: ', max_depth(root))

print('same tree')
print(same_tree(root, root))
print(same_tree_iter(root, root))
print(same_tree_short(root, root))

print('invert tree, preorder')
print(preorder(invert_tree(root)))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(preorder(invert_tree_short(root)))

print('level order')
print(level_order(root))

print('max path sum')
print(max_path_sum(root))

