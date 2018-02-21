/*
 * https://leetcode.com/problems/rotate-array/
 * Rotate an array of n elements to the right by k steps
 * n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]
 */

// O(n)? time, O(1) space
let rotate = (nums, k) => {
	for (let i = 0; i < k; i++) {
		nums.unshift(nums.pop());
	}
};

let nums = [1, 2, 3, 4, 5, 6, 7];
rotate(nums, 3);
console.log(nums); // [5,6,7,1,2,3,4]
