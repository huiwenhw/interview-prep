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
