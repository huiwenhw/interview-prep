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
