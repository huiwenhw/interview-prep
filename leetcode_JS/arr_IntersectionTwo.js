/*
https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
Example: Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note: Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
*/

// Add nums1 into obj, loop through nums2
// If present in nums1 obj, add curr elem to ans array
// O(nums1 + nums2) time, O(nums1 + max(nums1,nums2)) space
intersect = (nums1, nums2) => {
    n1 = {};
    for (let i=0 ; i<nums1.length ; i++) {
        n1[nums1[i]] = n1[nums1[i]] + 1 || 1;
    }
    
    ans = []
    for (let i=0 ; i<nums2.length ; i++) {
        if (n1[nums2[i]] > 0) {
            ans.push(nums2[i]);
            n1[nums2[i]] -= 1;
        }
    }
    return ans;
};

console.log(intersect([1,2,2,1], [2,2])); // [2,2]

// Same as above, but using reduce and filter methods this time
intersectReduce = (nums1, nums2) => {
	// reduce nums1 to an obj of {elem: freq}
	let n1 = nums1.reduce((map, n) => {
		map[n] = map[n] + 1 || 1;
		return map;
	}, {});

	// filter nums2 to save only elem in nums1 and nums2
	let ans = nums2.filter(n => {
		if (n1[n] > 0) {
			n1[n] -= 1;
			return true;
		} else {
			return false;
		}
	});
	return ans;
}

console.log(intersectReduce([1,2,2,1], [2,2])); // [2,2]
