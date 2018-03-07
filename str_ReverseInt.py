'''
https://leetcode.com/problems/reverse-integer/
function returns 0 when the reversed integer overflows
'''

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    ans, sign = None, 1
    if x >= 0:
        ans = int(str(x)[::-1])
    else:
        ans, sign = int(str(x)[1:][::-1]), -1

    if abs(ans) > 2**31:
        return 0
    return ans * sign

print(reverse(-7463847412)) # -2147483647 
