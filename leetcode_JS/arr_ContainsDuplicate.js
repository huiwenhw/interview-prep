/* 
 * https://leetcode.com/problems/contains-duplicate/description/
 * Return: true if array contains duplicates
 */

// If curr element is in object, means we've passed it earlier, duplicate
containsDuplicateUsingBoolean = nums => {
	let obj = {};
    for (let i=0; i<nums.length ; i++) {
        if(obj[nums[i]]) return true;
        obj[nums[i]] = true;
    }
	return false;
}

console.log(containsDuplicateUsingBoolean([1, 2, 2])); // true
console.log(containsDuplicateUsingBoolean([0])); // false

containsDuplicate = nums => {
	if (!nums.length) return false;
	const numset = new Set(nums);
	let ans = numset.size !== nums.length ? true : false;
	return ans;
};

console.log(containsDuplicate([1, 2, 2])); // true
console.log(containsDuplicate([0])); // false

containsDuplicateWithoutSet = nums => {
	let obj = {};
	for (let i = 0; i < nums.length; i++) {
		obj[nums[i]] = obj[nums[i]] + 1 || 1; // + has precedence over || 
		if (obj[nums[i]] > 1) return true;
	}
	return false;
};

console.log(containsDuplicateWithoutSet([1, 2, 2])); // true
console.log(containsDuplicateWithoutSet([1, 2, 3])); // false
