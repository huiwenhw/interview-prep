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
