'''
Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.
'''

def sudoku2_short(grid):
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        first, sec = set(), set()
        for c in range(cols):
            if grid[c][r] != '.' and grid[c][r] in first:
                return False
            first.add(grid[c][r])
            if grid[r][c] != '.' and grid[r][c] in sec:
                return False
            sec.add(grid[r][c])

    # check 3x3
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            d = set()
            nlist = grid[r][c:c+3] + grid[r+1][c:c+3] + grid[r+2][c:c+3]
            for n in nlist:
                if n != '.' and n in d:
                    return False
                d.add(n)
    return True

def sudoku2(grid):
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        first, sec = set(), set()
        for c in range(cols):
            # add to dict, ensure that there's no same element 
            if grid[r][c] == '.' and grid[c][r] == '.':
                continue
            if grid[c][r] != '.' and grid[c][r] in first:
                return False
            elif grid[c][r] != '.':
                first.add(grid[c][r])
            if grid[r][c] != '.' and grid[r][c] in sec:
                return False
            elif grid[r][c] != '.':
                sec.add(grid[r][c])

        # check 3x3
        for r in range(rows):
            if r%3 == 0:
                first, sec, third = set(), set(), set()
            for c in range(cols):
                if grid[r][c] == '.':
                    continue
                if 0 <= c < 3:
                    if grid[r][c] in first:
                        return False
                    first.add(grid[r][c])
                if 3 <= c < 6:
                    if grid[r][c] in sec:
                        return False
                    sec.add(grid[r][c])
                if 6 <= c < 9:
                    if grid[r][c] in third:
                        return False
                    third.add(grid[r][c])
    return True

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
print(sudoku2(grid)) # True
print(sudoku2_short(grid)) # True
grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
print(sudoku2(grid)) # False
print(sudoku2_short(grid)) # False
