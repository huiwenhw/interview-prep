'''
https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
'''

# O(n) time, O(1) space
def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []: return 0
    length, maxn = 1, 1
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            length += 1
            maxn = max(maxn, length)
        else:
            length = 1
    return maxn
 
print(findLengthOfLCIS([1]))  # 1
print(findLengthOfLCIS([1,3,5,4,7])) # 3 (1,3,5)
