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
