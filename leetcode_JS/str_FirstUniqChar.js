/*
https://leetcode.com/problems/first-unique-character-in-a-string/
*/

// If index of curr elem is the same as last index of curr elem in string
// Found first uniq char
var firstUniqChar = function(s) {
    for (let i=0 ; i<s.length ; i++) {
        if (s.indexOf(s[i]) === s.lastIndexOf(s[i])) {
            return i;
        }
    }
    return -1;
};

console.log(firstUniqChar('leetcode')); // 0

// with hashmap
var firstUniqChar = function(s) {
    let map = new Map();
    for (let i=0 ; i<s.length ; i++) {
        if (map.has(s[i])) {
            map.set(s[i], 2);
        } else {
            map.set(s[i], 1);
        }
    }
    
    for (let i=0 ; i<s.length ; i++) {
        if (map.has(s[i]) && map.get(s[i]) === 1) {
            return i;
        }
    }
    return -1;
};

console.log(firstUniqChar('leetcode')); // 0
