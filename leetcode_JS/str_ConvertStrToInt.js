// https://leetcode.com/problems/string-to-integer-atoi/

var myAtoi = function(str) {
    let INT_MIN = -2147483648, INT_MAX = 2147483647;
    return Math.max(Math.min(INT_MAX, parseInt(str) || 0), INT_MIN);
};

console.log(myAtoi('+-2')); // 0
