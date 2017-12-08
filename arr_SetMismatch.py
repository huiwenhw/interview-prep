'''
https://leetcode.com/problems/set-mismatch/description/

The set S contains numbers from 1 to n. One of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.
Input: nums = [1,2,2,4]
Output: [2,3]
'''

# using xor and array, O(n) time, O(1) space
# numbers are from [1 ... n], we can xor index with nums[i]
# that'll leave us with index ^ repeated num
# when we find repeated num, we can just do index ^ rep ^ rep to get missing index 
def find_xor(nums):
    n = len(nums)
    s = 0
    for i in range(n):
        s ^= (i+1) ^ nums[i]

    for i in range(n):
        nums[abs(nums[i])-1] *= -1
        if nums[abs(nums[i])-1] > 0:
            rep = abs(nums[i])

    return [rep, s ^ rep]

# O(n) time, O(1) space
# using array itself to check for duplicate numbers
def find_short(nums):
    n = len(nums)
    total = int(n*(n+1)/2)
    ntotal = sum(nums) 

    for i in range(n):
        nums[abs(nums[i])-1] *= -1
        if nums[abs(nums[i])-1] > 0:
            diff = total - (ntotal - abs(nums[i]))
            return [abs(nums[i]), diff]
    return None

# O(n) time and space
def finderrornum(nums):
    n = len(nums)
    total = int(n*(n+1)/2)

    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1
        if d[n] > 1:
            diff = total - (sum(nums) - n)
            return [n, diff]
            break
    return None

print(finderrornum([1,2,2,4]))
print(find_short([1,2,2,4]))
print(find_short([2,2]))
print(find_xor([2,2]))
