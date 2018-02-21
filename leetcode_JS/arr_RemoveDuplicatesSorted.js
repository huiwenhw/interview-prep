/* 
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
 */ 

let removeDuplicates = function(nums) {
    for(let i = 1; i < nums.length ; i++) {
        if (nums[i] === nums[i-1]) {
            nums.splice(i, 1);
            i = i-1;
        }
    }
};

let nums = [1,1,2];
removeDuplicates(nums); // [1,2]
console.log(nums)

nums = [1,1,1];
removeDuplicates(nums); // [1]
console.log(nums)
