/*
https://leetcode.com/problems/move-zeroes/description/
Given array, move all 0s to end while maintaining relative order of non-zero elements
Example, given nums = [0, 1, 0, 3, 12], ans should be [1, 3, 12, 0, 0]

Do this in-place without making a copy of the array
Minimize the total number of operations
*/

// Start from the back so we wouldnt have to worry about index at the start 
moveZeroes = (nums) => {  
    for (let i=nums.length-1 ; i>=0 ; i--) {
        if (nums[i] === 0) {
            nums.splice(i, 1);
            nums.push(0);
        }
    }
};

nums = [1, 3, 12, 0, 0];
moveZeroes(nums);
console.log(nums); // [ 1, 3, 12, 0, 0 ]
