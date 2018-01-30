'''
https://www.interviewcake.com/question/python/nth-fibonacci
'''

# O(2^n) time 
# if we draw out the call tree, we will see that height is n, so total number of nodes is O(2^n)
def fib_recur(n):
    if n in [0, 1]:
        return n
    return fib_recur(n-1) + fib_recur(n-2)

print(fib_recur(5)) # 5 

# O(n) time and space 
def fib_recur_memo(n):
    def fib(n):
        if n < 0: raise ValueError('No negative numbers')
        if n in [0, 1]: return n 
        if n in memo: return memo[n]

        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]

    memo = {}
    return fib(n)

print(fib_recur_memo(5)) # 5

# O(n) time, O(1) space 
# keep track of our previous and previous previous ans 
# do n-1 iterations to get nth fib
def fib_iter(n):
    if n < 0: raise ValueError('No negative numbers')
    if n in [0, 1]: return n 

    prevprev = 0
    prev = 1

    for _ in range(n-1):
        curr = prev + prevprev
        prevprev = prev
        prev = curr
        
    return curr 

print(fib_iter(5)) # 5 
