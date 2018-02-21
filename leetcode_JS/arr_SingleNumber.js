/*
 * https://leetcode.com/problems/single-number/
 * Array: every element appears twice except for one.
 * Find: that single one.
 */

// O(n) time, O(1) space
let singleNumber = function(nums) {
    let res = 0;
    for (let i = 0; i < nums.length; i++) {
        res ^= nums[i];
    }
    return res;
};

console.log(singleNumber([1,1,3,3,4])); // 4