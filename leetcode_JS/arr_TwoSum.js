/*
https://leetcode.com/problems/two-sum/
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
*/


// obj contains difference of target - curr elements
// If curr elem is found in obj, means there's a match 
twoSum = (nums, target) => {
    obj = {}
    for (let i=0 ; i<nums.length ; i++) {
        if (nums[i] in obj) {
            return [obj[nums[i]], i];
        }
        obj[target - nums[i]] = i;
    }
};

console.log(twoSum([2, 7, 11, 15], 9)); // [0, 1]

twoSum = (nums, target) => {
    obj = {}
    for (let i=0 ; i<nums.length ; i++) {
        if (obj.hasOwnProperty(nums[i])) {
            return [obj[nums[i]], i];
        }
        obj[target - nums[i]] = i;
    }
};

console.log(twoSum([2, 7, 11, 15], 9)); // [0, 1]
console.log(twoSum([3, 3], 6)); // [0, 1]
