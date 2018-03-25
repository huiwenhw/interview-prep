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
