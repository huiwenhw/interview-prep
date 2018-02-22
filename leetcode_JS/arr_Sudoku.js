/*
https://leetcode.com/problems/valid-sudoku/
*/

var isValidSudoku = function(board) {
    for (let i=0 ; i<9 ; i+=3) {
        for (let k=0 ; k<9 ; k+=3) {
            arr = [];
            arr.push(board[i][k]);
            arr.push(board[i][k+1]);
            arr.push(board[i][k+2]);
            arr.push(board[i+1][k]);
            arr.push(board[i+1][k+1]);
            arr.push(board[i+1][k+2]);
            arr.push(board[i+2][k]);
            arr.push(board[i+2][k+1]);
            arr.push(board[i+2][k+2]);
            if (checkDup(arr)) {
                return false;
            }
        }
    }
    
    for (let i=0 ; i<9 ; i++) {
        obj1 = {}, obj2 = {};
        for (let k=0 ; k<9 ; k++) {
            if (board[i][k] !== '.' && board[i][k] in obj1) {
                return false;
            }
            if (board[k][i] !== '.' && board[k][i] in obj2) {
                return false;
            }
            obj1[board[i][k]] = true;
            obj2[board[k][i]] = true;
        }
    }
    
    return true;
};

var checkDup = function(arr) {
    obj = {};
    for (let i=0 ; i<arr.length ; i++) {
        if (arr[i] !== '.' && arr[i] in obj) {
            return true;
        }
        obj[arr[i]] = true;
    }
    return false;
}


grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
console.log(isValidSudoku(grid)); // true
grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
console.log(isValidSudoku(grid)); // false
