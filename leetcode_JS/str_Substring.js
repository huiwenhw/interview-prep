/*
https://leetcode.com/problems/implement-strstr/description
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
*/

var strStr = function(haystack, needle) {
    if (needle === '') { return 0; }
    for (let i=0 ; i<haystack.length ; i++) {
        if (haystack[i] === needle[0]) {
            substr = haystack.substr(i, needle.length);
            if (needle === substr) { return i; }
        }
    }
    return -1;
};

console.log(strStr("mississippi", "issip")); // 4
