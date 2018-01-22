'''
https://leetcode.com/contest/weekly-contest-68/problems/toeplitz-matrix/
'''

def matrix(matrix):
    for i in range(0, len(matrix)-1):
        length = len(matrix[i])
        arr = matrix[i]
        arr_sec = matrix[i+1]
        print(arr[:length-1], arr_sec[1:])
        if not arr[:length-1] == arr_sec[1:]:
            return False
    return True

print(matrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
