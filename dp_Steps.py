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
