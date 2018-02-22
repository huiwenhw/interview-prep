/*
https://leetcode.com/problems/valid-anagram/description/
*/

var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;
    obj = {};
    for (let i=0 ; i<s.length ; i++) {
        obj[s[i]] = obj[s[i]] + 1 || 1;
    }
    for (let i=0 ; i<t.length ; i++) {
        if (t[i] in obj && obj[t[i]] > 0) {
            obj[t[i]] -= 1;
        } else {
            return false;
        }
    }
    return true;
};

console.log(isAnagram('anagram', 'nagaram')); // true
console.log(isAnagram('rat', 'tac')); // false

var isAnagram = function(s, t) {
    return s.split('').sort().toString() === t.split('').sort().toString();
};

console.log(isAnagram('anagram', 'nagaram')); // true
console.log(isAnagram('rat', 'tac')); // false
