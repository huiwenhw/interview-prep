/*
https://leetcode.com/problems/reverse-string/description/
*/


// With string/arr methods 
var reverseString = function(s) {
    arr = s.split('');
    arr.reverse();
    return arr.join('');
};

console.log(reverseString('hello')); // 'olleh'

// Without string/arr methods, slower on leetcode
var reverseString = function(s) {
    let ans = '';
    for (let i=s.length-1 ; i>=0 ; i--) {
        ans += s[i];
    }
    return ans;
};

console.log(reverseString('hello')); // 'olleh'
