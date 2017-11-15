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
