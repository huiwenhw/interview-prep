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
