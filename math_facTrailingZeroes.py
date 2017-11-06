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
