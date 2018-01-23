## arr_Calculator.py:
'''
https://leetcode.com/problems/basic-calculator/description/

Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.
Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
'''

# works 
# if its digit, get all digits (e.g. could be 20) 
# keep a signs array, use the previous sign and * either 1 or -1 (if its minus)
# this ensures that 1-(2-3) = 1+1
def calc_short(s):
    total = 0
    i, signs = 0, [1, 1]
    while i < len(s):
        print('%11s   %-16s %2d' % (s[i:], signs, total))
        ch = s[i]
        if ch.isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            total += int(s[start:i]) * signs.pop()
            continue
        if ch in "(+-":
            signs.append(signs[-1] * [1, -1][ch == '-'])
        elif ch == ")":
            signs.pop()
        print('%11s   %-16s %2d' % (s[i:], signs, total))
        i += 1
    return total

# push to stack expressions
# if +, push 1 
# if -, push -1
# if (, push 1
# if ), pop
# will not work for '1-(5)' or '2-(5-6)' 
def calc(s):
    s = s.replace(' ', '')
    stack, sumn, snum = [1], 0, ''
    for i in range(len(s)):
        print('i ', i, ' s[i] ', s[i], ' s ', stack, ' sum ', sumn)
        if s[i].isdigit() and s[i+1:i+2].isdigit():
            snum += s[i]
        elif s[i].isdigit():
            snum += s[i]
            sumn += int(snum) * stack.pop()
            snum = ''
        elif s[i] == "+":
            stack.append(1)
        elif s[i] == "-":
            stack.append(-1)
        elif s[i] == "(":
            stack.append(1)
        elif s[i] == ")":
            stack.pop()
    return sumn

s = "1+1"
print(calc_short(s))
s = "(1-2)+(3-4)"
print(calc_short(s))
s = "3-(2+(9-4))"
print(calc_short(s))
s = '2-(5-6)'
print(calc_short(s))
s = '1-(5)' # -4
s = ' 30 + ( 25 + 1 ) '
s = "2-1+2" # 3
s = "(1+(4+5+2)-3)+(6+8)" # 23
s = "  30" # 20

## arr_CalculatorTwo.py:
'''
https://leetcode.com/problems/basic-calculator-ii/description/

Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

Note: Do not use the eval built-in library function.
'''
import re

# separate all digits, operators into iterable (0, -, 2147483647)
# iterate through, if its +/-, we add that to the total, update the sign
# if its */, we calc the term and kiv that
# if its digit, we update the term
# at the end, we need to add term*sign, cause the last one will be left out
def calc_short(s):
    tokens = iter(re.findall('\d+|\S', s))
    total, term, sign, num2 = 0, 0, 1, 0
    for token in tokens:
        if token in '+-':
            total += sign * term
            sign = ' +'.find(token) # 1 if +, -1 if -
        elif token in '*/':
            num2 = int(next(tokens))
            term = term * num2 if token == '*' else int(term/num2)
        else:
            term = int(token)
    return total + term * sign

# if its digit, get all digits
# if its +-*/, we append that to sign and continue
# else we pop from sign, if its +-, we add that to total, update prev with +/-
# if its */, we calc and update prev and kiv
# at the end, we need to add prev
def calc(s):
    s = s.replace(' ', '')
    i = prev = total = 0
    sign = ['+']
    while i < len(s):
        ch = s[i]
        print('ch ', ch, ' prev ', prev, ' total ', total)
        if ch in '+-*/':
            sign.append(ch)
            i += 1
            continue
        if ch.isdigit():
            while i+1 < len(s) and s[i+1].isdigit():
                i += 1
                ch += s[i]
        exp = sign.pop()
        if exp in '+-':
            total += prev
            prev = int(ch) * [-1, 1][exp == '+']
        else:
            curr = prev * int(ch) if exp == '*' else prev / int(ch)
            prev = int(curr)
        i += 1
    print('ch ', ch, ' prev ', prev, ' total ', total)
    total += prev
    return total

# works only for single digit
def calculate(s):
    stack = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == '*' or ch == '/':
            num1 = stack.pop()
            num2 = s[i+1]
            i += 1
            if ch == '*':
                evl = int(num1) * int(num2)
            else:
                evl = int(num1) / int(num2)
            stack.append(int(evl))
        else:
            stack.append(ch)
        i += 1
        print(stack)

    while len(stack) > 1:
        num1 = stack.pop()
        exp = stack.pop()
        num2 = stack.pop()
        if exp == '+':
            evl = int(num1) + int(num2)
        else:
            evl = int(num1) - int(num2)
        stack.append(int(evl))
        print(stack)
    return stack[0] 

print('hi ', calc_short('14-3/2'))
print(calc_short("0-2147483647")) # -2147483647
print(calc_short('0*0')) # 0
print(calc_short('  42 ')) # 42
print(calc_short('3+2')) # 5
print(calc_short('3+2*2')) # 7
print(calc_short('3/2')) # 1 
print(calc_short('3+5/2')) # 5
print(calc_short('3+2*2/2+10')) # 14

'''
print('hi ', calc('14-3/2'))
print(calc("0-2147483647")) # -2147483647
print(calc('0*0')) # 0
print(calc('  42 ')) # 42
print(calc('3+2')) # 5
print(calc('3+2*2')) # 7
print(calc('3/2')) # 1 
print(calc('3+5/2')) # 5
print(calc('3+2*2/2+10')) # 14

print(calculate('3+2')) # 5
print(calculate('3+2*2')) # 7
print(calculate('3/2')) # 1 
print(calculate('3+5/2')) # 5
'''

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
        print(start, end, area)
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

## arr_CryptSolution.py:
'''
Given array of strings crypt and an array containing the mapping of letters and digits, solution,
encrypt the words to be word1 + word2 = word3

If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it does not become a valid arithmetic solution, the answer is false.
'''

def isCryptSolution(crypt, solution):
    # convert solution to hash
    d = {}
    for l in solution:
        d[l[0]] = l[1]

    nl = []
    for word in crypt:
        nw = ''
        for n in word:
            nw += d[n]
        if nw[0] == '0' and len(nw) > 1:
            return False
        nl.append(nw)

    if int(nl[0]) + int(nl[1]) == int(nl[2]):
        return True
    return False

crypt = ["SEND", "MORE", "MONEY"]
solution = [['O', '0'],
        ['M', '1'],
        ['Y', '2'],
        ['E', '5'],
        ['N', '6'],
        ['D', '7'],
        ['R', '8'],
        ['S', '9']]
print(isCryptSolution(crypt, solution)) # 9567 + 1085 = 10652, True

crypt = ["TEN", "TWO", "ONE"]
solution = [['O', '1'],
        ['T', '0'],
        ['W', '9'],
        ['E', '5'],
        ['N', '4']]
print(isCryptSolution(crypt, solution)) # 054 + 091 = 145, False cause 054 and 091 both contain leading zeroes

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

## arr_DiagonalSame.py:
'''
https://leetcode.com/contest/weekly-contest-68/problems/toeplitz-matrix/
'''

def matrix(matrix):
    for i in range(0, len(matrix)-1):
        length = len(matrix[i])
        arr = matrix[i]
        arr_sec = matrix[i+1]
        print(arr[:length-1], arr_sec[1:])
        if not arr[:length-1] == arr_sec[1:]:
            return False
    return True

print(matrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))

## arr_FindDuplicate.py:
'''
https://leetcode.com/problems/find-the-duplicate-number/description/

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
'''

# similar to linkedlist II
# find where slow and fast meet == cycle means got dup 
# dist from start to cycle == dist from X to entry point
# entry point == duplicate number
def dup_short(nums):
    slow = nums[0]
    fast = nums[nums[0]]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

# O(n) time and space
def dup(nums):
    d = {}
    for n in nums:
        d[n] = d.get(n, 0) + 1

    for k,v in d.items():
        if v > 1:
            return k
    return None

# Modifying array
def dup_shorter(nums):
    n = len(nums)
    
    for i in range(n):
        nums[abs(nums[i])-1] *= -1
        if nums[abs(nums[i])-1] > 0:
            return abs(nums[i])
    return None

print(dup([1,2,4,5,6,7,8,9,2])) # 2
print(dup_short([1,2,4,5,6,7,8,9,2])) # 2
print(dup_shorter([1,2,4,5,6,7,8,9,2])) # 2

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

## arr_FirstDuplicate.py:
'''
Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example 
For a = [2, 3, 3, 1, 5, 2], the output should be
firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than than second occurrence of 2 does, so the answer is 3.

For a = [2, 4, 3, 5, 1], the output should be
firstDuplicate(a) = -1.
'''

import collections 

# once we find the first element, we return 
def firstDuplicate(a):
    if sum(a) == (len(a)*(len(a)+1))/2:
        return -1
    d = collections.defaultdict(int)
    index, element = float('inf'), -1
    for i in range(len(a)):
        if a[i] in d:
            element = a[i]
            break
        d[a[i]] = 1
    return element

# use array element to check if there's duplicate
# use abs(a[i]) so we use the original element and not the 'marked' one 
# if arr = [2,3,3,1,5,2], 
# after first round = [2,-3,3,1,5,2] # arr[1] (arr[2]-1) is marked as visited by * -1
def firstDuplicate_short(a):
    for i in range(len(a)):
        if a[abs(a[i])-1]<0:
            return abs(a[i])
        else:
            a[abs(a[i])-1] *= -1
    return -1

a = [2,3,3,1,5,2]
print(firstDuplicate(a))
a = [2,1,3,3,5,2]
print(firstDuplicate_short(a))

## arr_FirstNotRepeatingChar.py:
'''
Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.
Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you would be asked to do during a real interview.
'''

# O(n) time and space
def first(s):
    d = {}
    for i in range(len(s)):
        d[s[i]] = d.get(s[i], [0, i])
        d[s[i]][0] += 1
    min_i = float('inf')
    for k,v in d.items():
        if v[0] == 1 and v[1] < min_i:
            min_i = v[1]
    return [min_i, -1][min_i == float('inf')]

def first_short(s):
    letters = 'abcdefghijklmnopqrstuvwyz'
    min_i = float('inf')
    for i in range(len(s)):
        if s.count(s[i]) == 1 and i < min_i:
            min_i = i
    return [min_i, -1][min_i == float('inf')]
print(first("abacabad")) # c
print(first("abacabaabacaba")) # '_'

## arr_GroupAnagrams.py:
'''
https://leetcode.com/problems/group-anagrams/description/
Given an array of strings, group anagrams together.
'''

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    d = {}
    for s in strs:
        sorteds = ''.join(sorted(s))
        d[sorteds] = d.get(sorteds, []) + [s]

    ans = []
    for key, value in d.items():
        ans.append(value)
    print(d.values())
    return ans

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [["ate", "eat","tea"], ["nat","tan"], ["bat"]]

## arr_LargestRectangleArea.py:
'''
https://leetcode.com/problems/largest-rectangle-in-histogram/description/
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

For example, given heights = [2,1,5,6,2,3], return 10.
'''

# keep ascending buildings index in a stack
# if a descending building is detected, pop out the latest building from the stack
# checks for every peak in the array and keeps the ascending elements 
# once all ascendings buildings are added at index i, check 
# use dummy building at the end to calc the 'final' ascending buildings
def area_short(height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        print('i ', i, ' s ', stack, ' height[i] ', height[i], ' h[s[-1]] ', height[stack[-1]])
        while height[i] < height[stack[-1]]:
            print('h[i] ', height[i], ' < h[s[-1]] ', height[stack[-1]])
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            print('h', h, ' w', w, ' hw', h*w, ' i ', i, ' s ', stack)
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans

# naive way TLE
def area(heights):
    if not heights: return 0
    start, end = 0, len(heights)-1
    area = maxa = 0
    for i in range(len(heights)):
        for k in range(i, len(heights)):
            minn = min(heights[i:k+1])
            area = ((k-i)+1) * minn
            maxa = max(maxa, area)
    return maxa

# didnt pass, did the container way which was wrong
def area(heights):
    if not heights: return 0
    start, end = 0, len(heights)-1
    area = maxa = 0
    while start <= end:
        minn = min(heights[start:end+1])
        area = ((end-start)+1) * minn
        print('s ', start, ' e ', end, ' h[s] ', heights[start], ' h[e] ', heights[end], area)
        maxa = max(maxa, area)
        if heights[start] <= heights[end]:
            start += 1
        elif heights[start] > heights[end]:
            end -= 1
    return maxa


heights = [4,2,0,3,2,4,3,4]
heights = [5,5,1,7,1,1,5,2,7,6]
heights = [1,2,3,4]
heights = [2,1,5,6,2,3]
print(area_short(heights))
heights = [4,3,2,1]
print(area_short(heights))

'''
#print(area(heights)) # 10
heights = [1,5,1]
print(area_short(heights))
#print(area(heights)) # 5
heights = [11]
print(area_short(heights))
#print(area(heights)) # 11
heights = [4,2,0,3,2,4,3,4]
print(area_short(heights))
#print(area(heights)) # 10
heights = [5,5,1,7,1,1,5,2,7,6]
print(area_short(heights))
#print(area(heights)) # 12
'''

## arr_LetterCombinations.py:
'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
Given a digit string, return all possible letter combinations that the number could represent.
'''

def letter(digits):
    if not digits: return []
    mapping = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z']}
    
    return recur(digits, mapping)

def recur(digits, mapping):
    if len(digits) == 1: return mapping[digits[0]]

    first = digits[0]
    for i in range(1, len(digits)):
        arr = recur(digits[1:], mapping)
        firststr = mapping[first]
        newarr = []
        for char in firststr:
            newarr += [char+x for x in arr]
        return newarr

print(letter("")) # []
print(letter("23")) # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

def letter_nonrecur(digits):
    if not digits: return []
    mapping = {"2":"abc" , "3":"def" , "4":"ghi" , "5":"jkl" , "6":"mno" , "7":"pqrs" , "8":"tuv" , "9":"wxyz"}

    ans = [""]
    for digit in digits:
        word = mapping[digit]
        temp = []
        for char in word:
            for newchar in ans:
                temp += [newchar + char]
        ans = temp
    return ans

print(letter_nonrecur("")) # []
print(letter_nonrecur("23")) # ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

## arr_LongestConsecutive.py:
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

def missing_number(nums):
    n = len(nums)
    return n*(n+1)/2 - sum(nums)

def main():
    nums = sys.argv[1].split(",")
    nums = [int(i) for i in nums]
    print missing_number(nums)

if __name__ == '__main__':
    main()

## arr_Permutations.py:
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

## arr_ReorganizeString.py:
'''
https://leetcode.com/problems/reorganize-string/description/
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
'''

# Sort the string according to freq of characters
# find middle
# place start to middle at odd indices and middle to end at even indices
# letters cannot be rearranged if last 2 characters are the same
def string(S):
    a = sorted(sorted(S), key=S.count)
    h = int(len(a)/2)
    a[1::2], a[::2] = a[:h], a[h:]
    return ''.join(a) * (a[-1:] != a[-2:-1]) 

print(string("vvvlo")) # vlvov
print(string("lovvv")) # vlvov
print(string("a")) # a
print(string("aa"))
print(string("aab")) # aba
print(string("aaab"))
print(string("baaba")) # ababa
print(string("abaaaba"))
print(string("bbbbbbb"))

'''
def string(S):
    start, end, nextn = 1, len(S), 0
    quit = False
    while start < end:
        if S[start] == S[start-1]:
            if nextn >= end: 
                return ""
            while S[nextn] == S[start] or nextn+1 < end and S[nextn-1] == S[nextn+1]:
                nextn += 1
                if nextn >= end: 
                    return ""
            print('start ', start, ' nextn ', nextn, ' end ', end, ' S ', S)
            if nextn < start:
                S = S[:nextn] + S[nextn+1:start] + S[nextn] + S[start:]
            else:
                S = S[:start] + S[nextn] + S[start:nextn] + S[nextn+1:]
                nextn += 1
            start += 1
            print('after start ', start, ' nextn ', nextn, ' end ', end, ' S ', S)
        else:
            start += 1
    return S 
'''

## arr_Rotate.py:
'''
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
'''

# O(n^2) time and space
def rotate(a):
    rows, cols = len(a), len(a[0])
    res = [[] for _ in range(rows)]

    for i in range(rows):
        for k in range(cols):
            res[k].insert(0, a[i][k])
    return res

# O(n^2) time, in-place: no additional memory
def rotate_inplace(a):
    rows, cols = len(a), len(a[0])
    res = [[0 for _ in range(cols)] for _ in range(rows)]

    matrix(a)
    for i in range(int(rows/2)):
        start, end = i, rows-1-i
        offset = 0
        for k in range(start, end):
            print('i ', i, ' k ', k, ' start ', start, ' end ', end)
            temp = a[start][k]

            a[start][k] = a[end-offset][start]
            a[end-offset][start] = a[end][end-offset]
            a[end][end-offset] = a[k][end]
            a[k][end] = temp
            matrix(a)
            offset += 1
    return a

def matrix(a):
    for i in range(len(a)):
        print(a[i])
    print()

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(rotate_inplace(a))
a = [[10,9,6,3,7], [6,10,2,9,7], [7,6,3,8,2], [8,9,7,9,9], [6,8,6,8,2]]
# expected: [[6,8,7,6,10],[8,9,6,10,9],[6,7,3,2,6],[8,9,8,9,3],[2,9,2,7,7]]
print(rotate_inplace(a))

## arr_RotateArr.py:
'''
https://leetcode.com/problems/rotate-array/description/
'''

# O(n) space, since slicing creates a new copy of the list 
# O(1) time...
def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if not nums: return nums
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums) # [5,6,7,1,2,3,4]

## arr_RotateMatrix.py:
'''
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
'''

# O(n^2) time and space
def rotate(a):
    rows, cols = len(a), len(a[0])
    res = [[] for _ in range(rows)]

    for i in range(rows):
        for k in range(cols):
            res[k].insert(0, a[i][k])
    return res

# O(n^2) time, in-place: no additional memory
def rotate_inplace(a):
    rows, cols = len(a), len(a[0])
    res = [[0 for _ in range(cols)] for _ in range(rows)]

    matrix(a)
    for i in range(int(rows/2)):
        start, end = i, rows-1-i
        offset = 0
        for k in range(start, end):
            print('i ', i, ' k ', k, ' start ', start, ' end ', end)
            temp = a[start][k]

            a[start][k] = a[end-offset][start]
            a[end-offset][start] = a[end][end-offset]
            a[end][end-offset] = a[k][end]
            a[k][end] = temp
            matrix(a)
            offset += 1
    return a

def matrix(a):
    for i in range(len(a)):
        print(a[i])
    print()

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(rotate_inplace(a))
a = [[10,9,6,3,7], [6,10,2,9,7], [7,6,3,8,2], [8,9,7,9,9], [6,8,6,8,2]]
# expected: [[6,8,7,6,10],[8,9,6,10,9],[6,7,3,2,6],[8,9,8,9,3],[2,9,2,7,7]]
print(rotate_inplace(a))

## arr_SelfDividingNumbers.py:
'''
https://leetcode.com/contest/weekly-contest-59/problems/self-dividing-numbers/

A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
'''

def self_dividing_numbers_short(left, right):
    is_dividing = lambda num: '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))
    return list(filter(is_dividing, range(left, right+1)))

def selfDividingNumbers(left, right):
    ans = []
    for num in range(left, right+1):
        strnum = str(num)
        length = len(strnum)
        if length == 1:
            ans.append(num)
            continue
        divided = True
        for i in range(length):
            if strnum[i] == '0':
                divided = False
                break
            print('num ', num, ' strnum[i] ', strnum[i])
            if num % int(strnum[i]) != 0:
                divided = False
        if divided: ans.append(num)
    return ans

print(selfDividingNumbers(1, 22)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
print(self_dividing_numbers_short(1, 22)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

## arr_SetMismatch.py:
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

## arr_SingleNumber.py:
'''
https://leetcode.com/problems/single-number/description/
Given an array of integers, every element appears twice except for one. Find that single one.
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

# O(n) time, O(1) space
# ^ is the xor operator in python. 
# 9 ^ 9 = 0, 9 ^ 5 ^ 9 = 5
def single_short(nums):
    res = 0
    for n in nums:
        res ^= n
    return res

# O(n) time and space
def single_number(nums):
    d = {}
    for n in nums:
        if n not in d:
            d[n] = 0
        d[n] += 1

    ans = -1
    for k,v in d.items():
        if v == 1:
            ans = k
    return ans

nums = [9,3,9,3,9,7,9]
print(single_number(nums)) # 7
print(single_short(nums)) # 7
nums = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
print(single_number(nums)) # 16
print(single_short(nums)) # 16

## arr_Sudoku.py:
'''
Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.
'''

def sudoku2_short(grid):
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        first, sec = set(), set()
        for c in range(cols):
            if grid[c][r] != '.' and grid[c][r] in first:
                return False
            first.add(grid[c][r])
            if grid[r][c] != '.' and grid[r][c] in sec:
                return False
            sec.add(grid[r][c])

    # check 3x3
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            d = set()
            nlist = grid[r][c:c+3] + grid[r+1][c:c+3] + grid[r+2][c:c+3]
            for n in nlist:
                if n != '.' and n in d:
                    return False
                d.add(n)
    return True

def sudoku2(grid):
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        first, sec = set(), set()
        for c in range(cols):
            # add to dict, ensure that there's no same element 
            if grid[r][c] == '.' and grid[c][r] == '.':
                continue
            if grid[c][r] != '.' and grid[c][r] in first:
                return False
            elif grid[c][r] != '.':
                first.add(grid[c][r])
            if grid[r][c] != '.' and grid[r][c] in sec:
                return False
            elif grid[r][c] != '.':
                sec.add(grid[r][c])

        # check 3x3
        for r in range(rows):
            if r%3 == 0:
                first, sec, third = set(), set(), set()
            for c in range(cols):
                if grid[r][c] == '.':
                    continue
                if 0 <= c < 3:
                    if grid[r][c] in first:
                        return False
                    first.add(grid[r][c])
                if 3 <= c < 6:
                    if grid[r][c] in sec:
                        return False
                    sec.add(grid[r][c])
                if 6 <= c < 9:
                    if grid[r][c] in third:
                        return False
                    third.add(grid[r][c])
    return True

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
print(sudoku2(grid)) # True
print(sudoku2_short(grid)) # True
grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
print(sudoku2(grid)) # False
print(sudoku2_short(grid)) # False

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

## backtrack_NQueens.py:
'''
https://leetcode.com/problems/n-queens/description/
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Queens can't be on the same row, same col, diagonal 
'''

# nums = where queens are in cols [1,3] means first queen on col1, sec queen on col3
# index = current row, path = list 
def queens_short(n):
    res = []
    dfs([-1]*n, 0, [], res)
    return res

def dfs(nums, index, path, res):
    if index == len(nums):
        res.append(path)
        return 
    for i in range(len(nums)):
        nums[index] = i
        if valid(nums, index):
            curr_row = '.' * len(nums)
            dfs(nums, index+1, path + [curr_row[:i] + 'Q' + curr_row[i+1:]], res)
            
def valid(nums, index):
    for i in range(index):
        if abs(nums[index] - nums[i]) == index - i or nums[i] == nums[index]:
            return False
    return True

ans = queens_short(4)
for i in ans:
    print(i)
print()

import copy

# start from every row, proceed onto row+1, col+2 onwards
# need to wrap col+2 onwards
# if out of bounds, go back 
def queens(n):
    def recur(newl, r, c):
        # print('start: r ', r, ' c ', c, ' newl ', newl)
        # checking for same col and diagonals for curr [r][c]
        for k in range(r-1, -1, -1):
            if newl[k][c] == 'Q': return None
        col = c-1
        for k in range(r-1, -1, -1):
            # print('check left diag, k: ', k, k, ' newl ', [''.join(x) for x in newl])
            if col >= 0 and  newl[k][col] == 'Q': return None
            col -= 1
        col = c+1
        for k in range(r-1, -1, -1):
            # print('check right diag, k: ', k, k, ' newl ', [''.join(x) for x in newl])
            if col < len(newl) and newl[k][col] == 'Q': return None
            col += 1
        newl[r][c] = 'Q'
        if r == len(newl)-1:
            return newl
        # print('r ', r, ' c ', c, ' newl ', newl)
        for i in range(len(newl)):
            res = recur(newl, r+1, i)
            # print('in for r ', r, ' c ', c, ' res ', res)
            if res is None: newl[r+1][i] = '.'
            if res is not None:
                b = copy.deepcopy(newl)
                ans.append([''.join(x) for x in b])
                newl[r+1][i] = '.'

    ans = []
    for i in range(n):
        newl = [['.' for _ in range(n)] for _ in range(n)]
        recur(newl, 0, i)
    return ans

'''
ans = queens(4)
for i in ans:
    print(i)
print()
ans = queens(5)
for i in ans:
    print(i)
print()
'''

## bin_BinaryGap.py:
'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.
'''

# O(n) time and space, assuming N is max length of binary representation
def solution(N):
    bin = "{0:b}".format(N)
    count, maxn = 0, 0
    for b in bin:
        if b == '0':
            count += 1
        else:
            maxn = max(maxn, count)
            count = 0
    return maxn

print(solution(9)) # 2
print(solution(1041)) # 5

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

## data_Segments.py:
'''
Given data, event and array of segments, I want to find what's the analytics for a given event based on the segments 
Given event: 'Signup' and segments: ['city', 'gender', 'origin'], 
Output: {'Signup': {'NYC': {'M': {'twitter': 1}, 'F': {'google': 2, 'twitter': 1}}, 'Oakland': {'M': {'google': 1}}}}
'''

def getsegments(data, event, segments):
    nlist = []
    for i in range(len(data)):
        if data[i]['event'] == event:
            nlist.append(data[i]['properties'])

    # run once
    d = {event: {}}
    # run at the start of every loop
    newd = d[event]
    for i in range(len(nlist)):
        for k in range(len(segments)):
            key = nlist[i][segments[k]]
            if k == len(segments)-1:
                if key not in newd:
                    newd[key] = 0
                newd[key] += 1
            else:
                if key not in newd:
                    newd[key] = {}
            newd = newd[key]
        newd = d[event]
    d[event] = newd
    return d

data = [{'properties': {'item_id': 876, 'hair': 'brown', 'gender': 'M', 'city': 'NYC', 'value': 23}, 'event': 'Purchase'}, {'properties': {'hair': 'green', 'gender': 'M', 'city': 'NYC', 'origin': 'twitter'}, 'event': 'Signup'}, {'properties': {'item_id': 876, 'hair': 'blue', 'gender': 'M', 'city': 'SF', 'value': 20}, 'event': 'Purchase'}, {'properties': {'item_id': 123, 'hair': 'red', 'gender': 'F', 'city': 'SF', 'value': 55}, 'event': 'Purchase'}, {'properties': {'hair': 'brown', 'gender': 'F', 'city': 'NYC', 'origin': 'google'}, 'event': 'Signup'}, {'properties': {'hair': 'purple', 'gender': 'F', 'city': 'NYC', 'origin': 'twitter'}, 'event': 'Signup'}, {'properties': {'hair': 'brown', 'gender': 'M', 'city': 'Oakland', 'origin': 'google'}, 'event': 'Signup'}, {'properties': {'hair': 'blond', 'gender': 'F', 'city': 'NYC', 'origin': 'google'}, 'event': 'Signup'}, {'properties': {'item_id': 123, 'hair': 'red', 'gender': 'M', 'city': 'Oakland', 'value': 55}, 'event': 'Purchase'}]
print(getsegments(data, 'Signup', ['city', 'gender', 'origin']))

## design_LeastRecentlyUsedCache.py:
'''
https://leetcode.com/problems/lru-cache/description/
'''

# get: if key not in dict, return -1 
#      if key is in dict, get index, slice to append at the back
# put: if key is in dict, simply change value
#      if len(cache) same as capacity, remove LRU from cache
#      add new key, value to dict and cache 
class LRUCache(object):
    def __init__(self, capacity):
       self.capacity = capacity
       self.d = {}
       self.lrulist = []

    def get(self, key):         # O(n) cause of slicing
        if key not in self.d:
            return -1
        i = self.lrulist.index(key)
        self.lrulist = self.lrulist[:i] + self.lrulist[i+1:] + [key]
        return self.d.get(key)

    def put(self, key, value):# O(n) cause of slicing
        if key in self.d:
            self.d[key] = value
            i = self.lrulist.index(key)
            self.lrulist = self.lrulist[:i] + self.lrulist[i+1:] + [key]
        else:
            if len(self.lrulist) == self.capacity:
                self.d.pop(self.lrulist[0], None)
                self.lrulist = self.lrulist[1:]
            self.d[key] = value
            self.lrulist.append(key)

# Using doubly linked list to provide O(1) get / put
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

# dict: {key: node}
# get: if key not in dict, return -1 
#      if key in dict, remove node, add node to before tail, return val
# put: if key in dict, remove node
#      if capacity is up, remove head.next, remove from dict
#      then create and add node to tail.prev and to dict
class LRUCacheTwo(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail 
        self.tail.prev = self.head 

    def get(self, key):
        if key not in self.d:
            return -1
        n = self.d[key]
        self.remove(n)
        self.add(n)
        return n.val

    def put(self, key, value):
        if key in self.d:
            self.remove(self.d[key])
        elif len(self.d) == self.capacity:
            n = self.head.next
            self.remove(n)
            self.d.pop(n.key, None)
        n = Node(key, value)
        self.d[key] = n
        self.add(n)

    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

def main():
    obj = LRUCacheTwo(2)
    obj.put(1,1)
    obj.put(2,2)
    print(obj.get(1)) # 1
    obj.put(3,3)
    print(obj.get(2)) # -1
    obj.put(4,4)
    print(obj.get(1)) # -1
    print(obj.get(3)) # 3
    print(obj.get(4)) # 4
    # print(obj.d, obj.lrulist)

    obj = LRUCacheTwo(2)
    print(obj.get(2)) # -1 
    obj.put(2, 6)
    print(obj.get(1)) # -1 
    obj.put(1, 5)
    obj.put(1, 2)
    print(obj.get(1)) # 2 
    print(obj.get(2)) # 6
    # print(obj.d, obj.lrulist)

    obj = LRUCacheTwo(2)
    obj.put(2,1)
    obj.put(1,1)
    obj.put(2,3)
    obj.put(4,1)
    print(obj.get(1)) # -1 
    print(obj.get(2)) # 3
    # print(obj.d, obj.lrulist)

if __name__ == "__main__":
    main()

## dp_CanJump.py:
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

## dp_CoinChange.py:
'''
https://leetcode.com/problems/coin-change/description/
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.
'''

# use only one dp array
# for each amount, create a list of # coins needed to fulfil that amount
# take the min of that list and store it in dp[current amount]
# finally, dp[amount] will be number of coins needed 
# if its float('inf') value, it means that the coins were unable to add up to amount
def coinchange(coins, amount):
    maxn = float('inf')
    dp = [0] + [maxn] * amount

    for i in range(1, amount+1):
        dp[i] = min([dp[i-c] if i-c >= 0 else maxn for c in coins]) + 1
    return [dp[amount], -1][dp[amount] == maxn]
    # means: [falsevalue, truevalue][true condition]

def coinchange_ori(coins, amount):
    #dp = [[float('inf') for _ in range(amount+1)] for _ in range(len(coins)+1)]
    coins = [x for x in coins if x <= amount]
    if amount == 0: return 0
    if len(coins) == 0: return -1

    dp = [[float('inf') for _ in range(amount+1)] for _ in range(2)]
    mincoin = min(coins)-1

    for i in range(1, len(coins)+1):
        ir = i % 2 
        if amount < coins[i-1]:
            dp[ir] = dp[ir-1]
            continue
        for k in range(1, amount+1):
            if k == coins[i-1]:
                dp[ir][k] = 1
            elif k < coins[i-1]:
                dp[ir][k] = dp[ir-1][k]
            else:
                dp[ir][k] = min(dp[ir][k-coins[i-1]]+1, dp[ir-1][k])
    #print(dp)
    if dp[ir][amount] == float('inf'):
        return -1
    return dp[ir][amount]

print(coinchange([1,2,5], 11))
print(coinchange([1,3,4], 6))
print(coinchange([214783647], 2))
'''
print(coinchange([125,146,125,252,226,25,24,308,50], 8402))
print(coinchange([112,149,215,496,482,436,144,397,500,189], 8480))
print(coinchange([492,364,366,144,492,316,221,326,16,166,353], 5253))
print(coinchange([9,183,255,407,102,174,230], 627)) # 9
print(coinchange([84,457,478,309,350,349,422,469,100,432,188], 6993))
'''

## dp_CombinationSumIV.py:
'''
https://leetcode.com/problems/combination-sum-iv/description/

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3], target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.
Therefore the output is 7.
'''

# dp[i] == how many ways to reach this 
# dp[0] = 0
def combi(nums, target):
    dp = [0] * (target+1)

    for i in range(1, target+1):
        for k in range(len(nums)):
            if i == nums[k]:
                dp[i] += 1
            elif i > nums[k]:
                dp[i] += dp[i-nums[k]]
    return dp[-1]

print(combi([1,2,3], 4))

## dp_DecodeWays.py:
'''
https://leetcode.com/problems/decode-ways/description/

A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1, 'B' -> 2, ..., 'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example, Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12). The number of ways decoding "12" is 2.
'''

def num_decodings(s):
    if len(s) == 0: return 0
    if s[0] == "0": return 0
    ways = 1
    for i in range(1, len(s)):
        if s[i-1:i+1] == "00": return 0
        elif s[i-1] == "0" or s[i] == "0": continue
        elif int(s[i-1:i+1]) <= 26:
            ways += 1
    return ways

# use int(s>'') to assign 1 / 0 to ways 
# if we reach a '0', discard prev ways, find if [i-1,i] is btwn 9 and 27
# if it is, means its 10/20 and we're discarding all the '02, 03 ..' at this check
# and we multiply that to prev num of ways to ensure that we can cont decoding
def decodings(s):
    pways, ways, pdigit = 0, int(s>''), ''
    for d in s:
        pways, ways, pdigit = ways, (d>'0')*ways + (9<int(pdigit+d)<27)*pways, d
        print('d ', d, ' pways ', pways, ' ways ', ways, ' pdigit ', pdigit)
    return ways

print(decodings("1234")) # 3
print(decodings("10")) # 1
print(decodings("100")) # 0
print(decodings("0")) # 0
print(decodings("01")) # 0
print(decodings("101")) # 1
print(decodings("11")) # 2
print(decodings("110")) # 1
print(decodings("11011")) # 2

## dp_HouseRobber.py:
'''
https://leetcode.com/problems/house-robber/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

# dp[i] contains max amt
# check from dp[0:i-1], what's the max amount
# use that 
# O(n) time and space
def rob(nums):
    if not nums: return 0
    dp = [0] * len(nums)
    for i in range(len(nums)):
        if i-1 > 0:
            dp[i] = nums[i] + max(dp[:i-1])
        else:
            dp[i] = nums[i]
    return max(dp)

# O(n) time, O(1) space
def rob_constant(nums):
    if not nums: return 0
    # dp = [0] * len(nums)
    i = e = 0
    for n in nums:
        i, e = n + e, max(i, e)
    return max(i, e)

print(rob([1,2,1,2,1])) # 4
print(rob([1,2,1,2])) # 4
print(rob([2,1,1,2])) # 4

print(rob_constant([1,2,1,2,1])) # 4
print(rob_constant([1,2,1,2])) # 4
print(rob_constant([2,1,1,2])) # 4

## dp_HouseRobberTwo.py:
'''
https://leetcode.com/problems/house-robber-ii/description/

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

# dp[i] contains max amt
# check from dp[0:i-1], what's the max amount
# O(n) time and space
# take max of nums[1:] and nums[:-1]
def rob(nums):
    def rob_inner(nums):
        print(nums)
        if not nums: return 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i-1 > 0:
                dp[i] = nums[i] + max(dp[:i-1])
            else:
                dp[i] = nums[i]
        return max(dp)
    return max(rob_inner(nums[len(nums) != 1:]), rob_inner(nums[:-1]))
    # if my len of nums is 1, take [0:] == nums[0] else, take [1:] == []

def rob_short(nums):
    def rob(nums):
        now = prev = 0
        for n in nums:
            now, prev = max(now, prev+n), now
        return now
    return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))

print(rob([2,1,1,2])) # 3
print(rob([0,0,0])) # 0
print(rob([1,1,1])) # 1
print(rob([1,3,1])) # 3
print(rob([2,7,9,3,1])) # 11
print(rob([1,2,1,1])) # 3

print(rob_short([2,7,9,3,1])) # 11
print(rob_short([1,2,1,1])) # 3

## dp_LongestIncreasingSubsequence.py:
'''
https://leetcode.com/problems/longest-increasing-subsequence/description/

Given an unsorted array of integers, find the length of longest increasing subsequence.
For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.
'''

def lis(nums):
    if not nums: return 0
    dp = [0] * (len(nums))
        
    for i in range(len(nums)):
        maxn = 0
        for k in range(i, -1, -1):
            if nums[k] < nums[i]:
                maxn = max(maxn, dp[k] + 1)
                dp[i] = maxn
        if dp[i] == 0: dp[i] = 1
    return max(dp)

# tails: at i, tails stores the smallest number of each increasing subsequence at length i+1
# if num is larger than all smallest number, append it to the list
# else if num is in btwn a certain tail, tails[i-1] < x <= tails[i], change tails[i]
def lis_short(nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = int((i + j) / 2)
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
        print(i, j, tails)
    return size

#print(lis([10, 9, 2, 5, 3, 7, 101, 18]))
#print(lis([1,3,6,7,9,4,10,5,6]))
print(lis_short([10, 9, 2, 5, 3, 7, 101, 18])) # 4
print(lis_short([1, 3, 4, 2, 10])) # 4

## dp_MeetupSteps.py:
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

## dp_MinPathSum.py:
'''
https://leetcode.com/problems/minimum-path-sum/description/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1 3 1 1 1 minimizes the sum.
'''

# O(mn) time, O(mn) space
def min_path_sum(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for k in range(cols):
            if i == 0 and k == 0:
                dp[i][k] = grid[i][k]
            elif i == 0:
                dp[i][k] = grid[i][k] + dp[i][k-1]
            elif k == 0:
                dp[i][k] = grid[i][k] + dp[i-1][k]
            else:
                dp[i][k] = grid[i][k] + min(dp[i-1][k], dp[i][k-1])
    return dp[rows-1][cols-1]

# O(mn) time, O(2n) space
def min_space(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[float('inf') for _ in range(cols)] for _ in range(2)]

    for i in range(rows):
        ir = i%2
        for k in range(cols):
            if i == 0 and k == 0:
                dp[ir][k] = grid[i][k]
            elif i == 0:
                dp[ir][k] = grid[i][k] + dp[ir][k-1]
            elif k == 0:
                dp[ir][k] = grid[i][k] + dp[ir-1][k]
            else:
                dp[ir][k] = grid[i][k] + min(dp[ir-1][k], dp[ir][k-1])
    return dp[ir][cols-1]

# making it look cleaner
def min_clean(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]

    dp[0][0] = grid[0][0]
    for i in range(1, cols):
        dp[0][i] = grid[0][i] + dp[0][i-1]
    for i in range(1, rows):
        dp[i][0] = grid[i][0] + dp[i-1][0]
    for i in range(1, rows):
        for k in range(1, cols):
            dp[i][k] = grid[i][k] + min(dp[i-1][k], dp[i][k-1])
    return dp[rows-1][cols-1]

grid = [[1,3,1], [1,5,1], [4,2,1]]
print(min_path_sum(grid))
print(min_space(grid))
print(min_clean(grid))

## dp_Steps.py:
'''
https://leetcode.com/problems/climbing-stairs/description/
You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

# top down
def climbstairs(n):
    arr = [0] * (n+1)
    return recur(arr, n)

def recur(arr, n):
    if n < 0:
        return 0
    if n == 0:
        arr[0] = 1
        return 1

    if arr[n]: return arr[n]
    arr[n] = recur(arr, n-1) + recur(arr, n-2)
    print(arr)
    return arr[n]

# bottom up 
def climbstairs_btm(n):
    arr = [0] * (n+1)
    arr[0], arr[1] = 1, 2
    for i in range(2, len(arr)):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n-1]
    
print(climbstairs(2)) # 2
print(climbstairs_btm(1)) # 1

## dp_Triangle.py:
'''
https://leetcode.com/problems/triangle/description/

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''

import collections 

# bottom up, O(n^2) space
def minimum_total(triangle):
    if len(triangle) == 1: return triangle[0][0]
    
    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
    for i in range(len(triangle)-1, -1, -1):
        curr = triangle[i]
        if i == len(triangle)-1:
            dp[i] = list(triangle[i])
            continue
        for k in range(len(curr)):
            dp[i][k] = curr[k] + min(dp[i+1][k], dp[i+1][k+1])
    return dp[0][0]

# bottom up, O(n) space
def minimum_total_short(triangle):
    if not triangle: return
    
    # dont need to check for length, cause this takes in the last array
    # which could also be the first if triangle = [[-10]]
    # and dp[0] will just return -10 cause the loop wont run
    dp = list(triangle[-1]) # list(triangle[-1]) to copy, and not change the original array
    for i in range(len(triangle)-2, -1, -1):
        for k in range(len(triangle[i])):
            dp[k] = triangle[i][k] + min(dp[k], dp[k+1])
    return dp[0]

def min_total_topdown(triangle):
    if not triangle: return 
    dp = [[0 for _ in range(len(row))] for row in triangle]
    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for k in range(len(triangle[i])):
            if k == 0:
                dp[i][k] = triangle[i][k] + dp[i-1][k]
            elif k == len(triangle[i])-1:
                dp[i][k] = triangle[i][k] + dp[i-1][k-1]
            else:
                dp[i][k] = triangle[i][k] + min(dp[i-1][k-1], dp[i-1][k])
    return min(dp[-1])

triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]
print(minimum_total(triangle)) # 11
print(minimum_total_short(triangle)) # 11
print(min_total_topdown(triangle))

## dp_UniquePaths.py:
'''
https://leetcode.com/problems/unique-paths/description/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

# m = rows, n = cols
# dp[i][k] stores number of unique paths to reach that grid
# and that's a combination of the up and the left grids 
# if its row 0 or col 0, there can only be one way to reach that grid
# initialise row 0 and col 0 to 1 
# O(n^2) time and space 
def paths(m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for k in range(n):
            if i == 0:
                dp[i][k] = 1
            elif k == 0:
                dp[i][k] = 1
            else:
                dp[i][k] = dp[i-1][k] + dp[i][k-1]
    return dp[m-1][n-1]

def paths_refactor(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for k in range(1, n):
            dp[i][k] = dp[i-1][k] + dp[i][k-1]
    return dp[m-1][n-1]

# O(mn) time, O(n) space
# init all to 1, start from row 1 col 1
# using just one array, 
def paths_refactor_short(m, n):
    dp = [1] * n
    for i in range(1, m):
        for k in range(1, n):
            dp[k] += dp[k-1]
    return dp[n-1]

print(paths(2,2)) # 2
print(paths(1,2)) # 1 
print(paths_refactor(1,2)) # 1
print(paths_refactor(4,4)) # 20
print(paths_refactor_short(1,2)) # 1
print(paths_refactor_short(2,3)) # 3

## dp_WordBreak.py:
'''
https://leetcode.com/problems/word-break/description/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode", dict = ["leet", "code"].
Return true because "leetcode" can be segmented as "leet code".
'''

# any returns as early as it sees the first True value
def wordbreak(s, wordDict):
    ok = [True]
    for i in range(1, len(s)+1):
        # ok += [any(ok[j] and s[j:i] in wordDict for j in range(i))] # both works
        ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
        print(ok)
    return ok[-1]

def wordbreak_readable(s, wordDict):
    dp = [False for _ in range(len(s)+1)]
    dp[0] = True

    # dp[i] == True means: I can start my next word from there 
    for i in range(len(s)):
        if dp[i]:
            for k in range(i, len(s)):
                if s[i:k+1] in wordDict:
                    dp[k+1] = True
    return dp[-1]

print(wordbreak("leetcode", ["leet", "code"])) # True
print(wordbreak("water", ["wa", "ater"])) # False
print(wordbreak_readable("leetcode", ["leet", "code"])) # True
print(wordbreak_readable("water", ["wa", "ater"])) # False

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

## graph_NumIslands.py:
'''
https://leetcode.com/problems/number-of-islands/description/
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1

Example 2:
11000
11000
00100
00011
Answer: 3
'''

def islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])

    def dfs(i, j):
        # if 0, stop and go back 
        if grid[i][j] == 0:
            return
        grid[i][j] = 0
        
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for direction in directions:
            next_i, next_j = i+direction[0], j+direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                dfs(next_i, next_j)

    num = 0
    for i in range(rows):
        for k in range(cols):
            # if 1, search its neighbors, mark neighbors as 0
            if grid[i][k] == 1:
                dfs(i, k)
                num += 1
    return num

grid = [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0]]
print(islands(grid)) # 1
grid = [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]
print(islands(grid)) # 3
grid = [[0,0,0,0,0], [1,1,1,1,1], [0,0,0,0,0], [1,1,1,1,1]]
print(islands(grid)) # 2

## graph_PacificAtlantic.py:
'''
https://leetcode.com/problems/pacific-atlantic-water-flow/description/

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
'''

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
print(matrix)
print(pacific_atlantic(matrix))
traverse_matrix(matrix)

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

## interval_Calendar.py:
'''
https://leetcode.com/contest/weekly-contest-59/problems/my-calendar-i/

Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.
Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)
For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
'''

class MyCalendar:
    def __init__(self):
        self.intervals = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.intervals) == 0:
            self.intervals.append([start, end])
        else:
            for interval in self.intervals:
                if not (interval[1] <= start or end <= interval[0]):
                    return False
            self.intervals.append([start, end])
        return True 

    def book_short(self, start, end):
        for s, e in self.intervals:
            if not (start >= e or end <= s): return False
        self.intervals.append((start, end))
        return True

cal = MyCalendar()
print(cal.book(10, 20)) # returns true
print(cal.book(15, 25)) # returns false
print(cal.book(20, 30)) # returns true
cal2 = MyCalendar()
print(cal2.book_short(10, 20)) # returns true
print(cal2.book_short(15, 25)) # returns false
print(cal2.book_short(20, 30)) # returns true

## interval_CalendarTwo.py:
'''
https://leetcode.com/contest/weekly-contest-59/problems/my-calendar-ii/

Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
'''

class MyCalendarTwo:
    def __init__(self):
        self.intervals = []
        self.overlaps = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.intervals:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.intervals.append((start, end))
        return True

cal = MyCalendarTwo()
print(cal.book(10, 20)) # returns true
print(cal.book(50, 60)) # returns true
print(cal.book(10, 40)) # returns true
print(cal.book(5, 15)) # returns false
print(cal.book(5, 10)) # returns true
print(cal.book(25, 55)) # returns true

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

## ll_DetectCycleTwo.py:
'''
https://leetcode.com/problems/linked-list-cycle-ii/description/
https://discuss.leetcode.com/topic/17521/share-my-python-solution-with-detailed-explanation

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list. Can you solve it without using extra space?
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# dist from head to entry point === dist from where slow meets fast to entry point
# H: dist from head to entry point E
# D: dist from E to X (where slow meets fast)
# slow travelled H+D, fast travelled 2(H+D)
# 2H + 2D = H + D + nLoops -> H = nLoops - D (dist from X to E) 
# so all we gotta do is to find when head meets slow / fast
def detect_short(head):
    loop = None
    slow = fast = head 
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast: 
            loop = slow
            break

    if loop:
        while slow is not head:
            slow = slow.next
            head = head.next
        return slow
    return None

# check if there's loop
# add elements in loop to loopset
# start from head, check if curr in loopset
# first element to be in loopset == entry point
# O(N) time, O(loop) space
def detectCycle(head):
    loop = None
    slow = fast = head 
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast: 
            loop = slow
            break

    if loop:
        curr = loop.next
        loopset = {loop}
        while curr is not loop:
            loopset.add(curr)
            curr = curr.next

        slow = head
        while slow not in loopset:
            slow = slow.next
        return slow
    return None


head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next

print(detectCycle(head).val) # 2
print(detect_short(head).val) # 2

head = ListNode(1)
head.next = head

print(detectCycle(head).val) # 1
print(detect_short(head).val) # 1

head = ListNode(1)
head.next = ListNode(2)
head.next.next = head

print(detectCycle(head).val) # 1
print(detect_short(head).val) # 1

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

## matrix_SetZeroes.py:
'''
https://leetcode.com/problems/set-matrix-zeroes/description/
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
Follow up: Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

# O(n^2) time, O(m + n) space
def setzeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    r = [False for _ in range(rows)]
    c = [False for _ in range(cols)]

    # keep track of where the 0s are 
    for i in range(rows):
        for k in range(cols):
            if matrix[i][k] == 0:
                r[i] = True
                c[k] = True
    # set the zeroes
    for i in range(rows):
        for k in range(cols):
            if r[i] or c[k]:
                matrix[i][k] = 0
    print(matrix)

# using constant space, but still O(n^2) time
def followup(matrix):
    rows, cols = len(matrix), len(matrix[0])
    rowzero, colzero = False, False

    # first: mark if row 0 and col 0 have 0s in them 
    for i in range(rows):
        if matrix[i][0] == 0:
            colzero = True
    for i in range(cols):
        if matrix[0][i] == 0:
            rowzero = True

    # second: loop through matrix. if position [i][k] == 0,
    # use the first row/col to mark. [i][0] = 0 and [0][k] = 0
    for i in range(1, rows):
        for k in range(1, cols):
            if matrix[i][k] == 0:
                matrix[i][0] = 0
                matrix[0][k] = 0

    # third: loop through matrix again. if row / col is marked ^, then set that entire row / col to 0
    for i in range(1, rows):
        if matrix[i][0] == 0:
            for k in range(1, cols):
                matrix[i][k] = 0
    for i in range(1, cols):
        if matrix[0][i] == 0:
            for k in range(1, rows):
                matrix[k][i] = 0

    # fourth: if row 0 or col 0 had a 0 initially, set entire row / col to 0
    if rowzero:
        matrix[0] = [0] * cols
    if colzero:
        for i in range(rows):
            matrix[i][0] = 0
    print(matrix)

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setzeroes(matrix) # [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
matrix = [[1,1,1],[0,1,1],[1,1,1]]
followup(matrix) # [[0, 1, 1], [0, 0, 0], [0, 1, 1]]
matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
followup(matrix) # [[0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 3], [0, 0, 0, 0]]

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

## sort_Bubble.py:
# Swaps elements from 0...sorted index, bringing max to the end each time
# Best: O(n) sorted arr, Worst: O(n^2), In-place, Stable, Extra O(1)
def bubblesort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for k in range(n-i-1):
            if arr[k] > arr[k+1]:
                swapped = True
                arr[k], arr[k+1] = arr[k+1], arr[k]
        # if arr is sorted, don't need to spend time going through the arr again
        if not swapped: break
        print(arr)

arr = [64, 90, 34, 25, 12, 22, 11]
bubblesort(arr)
print('sorted arr: ', arr)


## sort_Insertion.py:
# Takes curr, moves elem up the list, places elem at found position in front
# Best O(n), Worst O(n^2) when reversed, In-place, Stable, Extra O(1)
# Insertion/Selection: Faster for small arrays
def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        k = i-1

        # using k to move elements up the list
        while k >= 0 and key < arr[k]:
            arr[k+1] = arr[k]
            k -= 1
        arr[k+1] = key
        print(arr, ' moving: ', key)

arr = [12, 11, 13, 5, 6]
insertion(arr)
print('sorted: ', arr)

## sort_Selection.py:
# finds min elem, swap with first elem of unsorted subarray
# Best/Worst: O(n^2), Inplace, Stable, Extra O(1) space
# Insertion/Selection: Faster for small arrays
def selection(arr):
    n = len(arr)

    for i in range(n):
        min_i = i
        for k in range(i+1, n):
            if arr[k] < arr[min_i]:
                min_i = k

        # swap min elem with first elem
        arr[i], arr[min_i] = arr[min_i], arr[i]
        print(arr, 'swapping ', arr[i], arr[min_i])

arr = [64, 25, 12, 22, 11]
print(arr, ' original')
selection(arr)
print(arr, ' sorted')

## str_IsSubsequence.py:
'''
https://leetcode.com/problems/is-subsequence/description/
Given a string s and a string t, check if s is subsequence of t.
e.g. s = "abc", t = "ahbgdc"
Return true.
'''

# will go through the entire t to check if 'x' exists. it doesn't exist, t comes to the end
# so StopIteration will be raised and subsequently all c are False
def is_subseq_short(s, t):
    t = iter(t)
    return all(c in t for c in s)

# If curr char is not in t, then we return False
# Else, we take the substring of t and start from there
def is_subseq_s(s, t):
    for c in s:
        i = t.find(c)
        if i == -1:
            return False
        else:
            t = t[i+1:]
    return True

# got TLE
def is_subseq(s, t):
    if s == '': return True
    sets = set()
    sets.add('')
    for ch in t:
        newsets = set()
        for st in sets:
            newstr = st + ch
            newsets.add(newstr)
        sets.update(newsets)
    sets.remove('')
    if s in sets: return True
    return False

print(is_subseq('abc', 'ahbgdc')) # True
print(is_subseq('axc', 'ahbgdc')) # False
print(is_subseq_s('abc', 'ahbgdc')) # True
print(is_subseq_s('axc', 'ahbgdc')) # False
print(is_subseq_short('abc', 'ahbgdc')) # True
print(is_subseq_short('axgd', 'ahbgdc')) # False, will give [T,F,F]

## str_SwapMaximum.py:
'''
https://leetcode.com/problems/maximum-swap/description/

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Inpu t: 9973
Output: 9973
Explanation: No swap.
'''

# break early if a swap happened, cause there wont be other numbers greater
def maxswap(num):
    n, newn, newk = str(num), '', 0
    for i in range(len(n)):
        maxn = -1
        for k in range(i+1, len(n)):
            if int(n[k]) >= maxn:
                maxn = int(n[k])
                newk = k
        if maxn > int(n[i]):
            newn = n[:i] + n[newk] + n[i+1:newk] + n[i] + n[newk+1:]
            break
    newn = int(newn) if newn else num
    return newn

# swap 
def max_swap(num):
    maxn = num
    n = str(num)
    for i in range(len(n)):
        for k in range(i+1, len(n)):
            newn = n[:i] + n[k] + n[i+1:k] + n[i] + n[k+1:]
            print('newn ', newn, ' n ', n, ' i ', i, ' k ', k)
            if int(newn) > maxn:
                maxn = int(newn)
    return maxn

print(maxswap(2736)) # 7236
print(maxswap(9973)) # 9973
print(maxswap(112)) # 211
print(maxswap(1012)) # 2011
print(maxswap(4973)) # 9473
print(maxswap(4579)) # 9574
print(maxswap(98368)) # 98863
print(maxswap(1993)) # 9913

print(max_swap(2736)) # 7236
print(max_swap(9973)) # 9973
print(max_swap(112)) # 211
print(max_swap(1012)) # 2011
print(max_swap(4973)) # 9473
print(max_swap(4579)) # 9574
print(max_swap(98368)) # 98863
print(max_swap(1993)) # 9913

## tree_Buildtree.py:
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

'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    return convert(0, len(nums)-1, nums)

def convert(start, end, nums):
    if start > end: return None
    mid = int((start + end) / 2)
    root = TreeNode(nums[mid])
    root.left = convert(start, mid-1, nums)
    root.right = convert(mid+1, end, nums)
    return root

root = sortedArrayToBST([-10,-3,0,5,9])
print(level_order(root))

'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
Given preorder and inorder traversal of a tree, construct the binary tree.
'''

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

preorder = [8,5,9,7,1,12,2,4,11,3]
inorder = [9,5,1,7,2,12,8,4,3,11]
root = build_tree(preorder, inorder)
print(level_order(root))

## tree_HasPathSum.py:
'''
https://leetcode.com/problems/path-sum/description/

determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
For example: given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def haspathsum_short(root, sumn):
    if not root:
        return False

    if not root.left and not root.right and root.val == sumn:
        return True

    sumn -= root.val
    return haspathsum_short(root.left, sumn) or haspathsum_short(root.right, sumn)

def haspathsum(root, sumn):
    if not root: return False
    return findpath(root, 0, sumn)

def findpath(root, curr, sumn):
    print(curr, root.val, sumn)
    if root.left and root.right:
        return findpath(root.left, curr+root.val, sumn) or findpath(root.right, curr+root.val, sumn)
    elif root.left:
        return findpath(root.left, curr+root.val, sumn)
    elif root.right:
        return findpath(root.right, curr+root.val, sumn)
    else:
        if curr + root.val == sumn:
            return True
    return False

root = TreeNode(1)
root.left = TreeNode(2)
print(haspathsum_short(root, 1))
print(haspathsum(root, 1))

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(5)
print(haspathsum_short(root, 6))
print(haspathsum(root, 6))

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.right = TreeNode(2)
root.left.left.left = TreeNode(7)
print(haspathsum_short(root, 22))
print(haspathsum(root, 22))

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

# use inorder and check! 
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
'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# adding by level 
def level_withoutlevel(root):
    if not root: return []
    ans, queue = [], [root]
    while queue:
        level = []
        num = len(queue)
        for i in range(num):
            node = queue.pop(0)
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        ans.append(level)
    return ans
            

# adding per node
def level(root):
    if not root: return []
    ans, queue = [], [(root, 0)]
    while queue:
        curr, level = queue.pop(0)
        if len(ans) == level: ans.append([])
        ans[level].append(curr.val)
        if curr.left: queue.append((curr.left, level+1))
        if curr.right: queue.append((curr.right, level+1))
    return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print('level order')
print(level(root))
print(level_withoutlevel(root))

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

## tree_s.py:
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
import collections 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1 2 # # 3 4 # # 5 # # 
def serialise(root):
    def ser(node):
        if node:
            vals.append(str(node.val))
            ser(node.left)
            ser(node.right)
        else:
            vals.append('#')
    vals = []
    ser(root)
    return ' '.join(vals)

# Changed to not use pop(0) as it is O(n)
# deque makes popleft O(1)
def deserialise(data):
    if not data: return
    def deser(vals):
        if len(vals) == 0: return
        # val = vals.pop(0) # so that we will go through the array in order
        val = vals.popleft()
        print(val, vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = deser(vals)
        node.right = deser(vals)
        return node
             
    # vals = data.split()
    vals = collections.deque(data.split())
    return deser(vals)

def deserialise_withiter(data):
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
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

data = serialise(root)
print('data ', data)
ans = deserialise(data)
print(level_order(ans))

'''
root = deserialise("5,4,7,3,None,2,None,-1,None,9")
print(level_order(root))
print(serialise(root))
'''

## tree_SerialiseBST.py:
'''
https://leetcode.com/problems/serialize-and-deserialize-bst/description/
'''

import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

# get preorder sequence
def serialize(root):
    """Encodes a tree to a single string.  
    :type root: TreeNode
    :rtype: str
    """
    def preorder(node):
        if node:
            ans.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        else: return
    ans = []
    preorder(root)
    return ' '.join(ans)

# using preorder sequence, and tracking min/max value
# pop(0) only if min < val < max 
# recurse down the same way to obtain a tree
def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    def build(vals, minn, maxn):
        if len(vals) == 0: return
        val = vals[0]
        if minn < val and val < maxn:
            val = vals.popleft()
            node = TreeNode(val)
            node.left = build(vals, minn, val)
            node.right = build(vals, val, maxn)
            return node 
        else: return

    vals = collections.deque(int(val) for val in data.split())
    return build(vals, float('-inf'), float('inf'))

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

root = TreeNode(10)
root.left = TreeNode(6)
root.right = TreeNode(20)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right.right = TreeNode(30)
data = serialize(root)
print('data ', data)
ans = deserialize(data)
print(level_order(ans))

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

## tree_Symmetric.py:
'''
https://leetcode.com/problems/symmetric-tree/description/
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetricIter(root):
    if not root: return True
    stack = [root.left, root.right]
    while stack:
        left, right = stack.pop(), stack.pop()
        if left is None and right is None: continue
        elif left == None or right == None: return False
        if left.val != right.val: return False
        stack.extend([left.left, right.right, left.right, right.left])
    return True

def isSymmetric(root):
    def sym(left, right):
        if not left and not right: 
            return True
        if left and right and left.val == right.val:
            return sym(left.left, right.right) and sym(left.right, right.left)
        return False
    return sym(root, root)

def isSym(left, right):
    if left == None and right == None:
        return True
    elif left == None or right == None:
        return False
    return left.val == right.val and isSym(left.right, right.left) and isSym(left.left, right.right)
    
def isSymmetricShort(root):
    if not root: return True
    return isSym(root.left, root.right)
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(isSymmetric(root)) # True 
print(isSymmetricShort(root)) # True 
print(isSymmetricIter(root)) # True 

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)
print(isSymmetric(root)) # False
print(isSymmetricShort(root)) # False
print(isSymmetricIter(root)) # False

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
# left, root, right
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

# root, left, right
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
    ans, stack = [], []
    while root or stack:
        if root:
            ans.append(root.val)
            stack.append(root.right)
            stack.append(root.left)
        root = stack.pop()
    return ans

# left, right, root
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

# reverse of root, right, left 
def postorder_iter_short(root):
    ans, stack = [], []
    while root or stack:
        if root:
            ans.append(root.val)
            stack.append(root.left)
            stack.append(root.right)
        root = stack.pop()
    return ans[::-1]

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
print(postorder_iter_short(root))

## tree_ValidBST.py:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_valid_short(root):
	return isValid(root, float('inf'), float('-inf'))

# not <= cause cant children must be < or > parent
def isValid(root, maxn, minn):
    if not root: return True
    if not (minn < root.val and root.val < maxn):
        return False
    return isValid(root.left, min(maxn, root.val), minn) and isValid(root.right, maxn, max(minn, root.val))

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

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)

print('is valid bst: ', is_valid_bst(root)) # False
print('is valid bst: ', is_valid_short(root)) # False

root = TreeNode(1)
root.left = TreeNode(1)

print('is valid bst: ', is_valid_bst(root)) # False
print('is valid bst: ', is_valid_short(root)) # False

## tree_ZigzagLevelOrder.py:
'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root: return []
    index = 0
    ans, queue = [], [root]
    while queue:
        level = []
        num = len(queue)
        for i in range(num):
            curr = queue.pop(0)
            level.append(curr.val)
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        if index % 2 == 1: level.reverse()
        index += 1
        ans.append(level)
    return ans

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(zigzagLevelOrder(root)) # [[3], [20, 9], [15, 7]]

