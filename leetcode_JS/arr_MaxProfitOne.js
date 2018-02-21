/*
* https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

* Array: ith element is the price of a given stock on day i.
* Find: max profit for at most one transaction 
*/

// Check max profit at each day
let maxProfitShort = prices => {
	if (!prices.length) return 0;
	let minp = Number.MAX_SAFE_INTEGER;
	let maxp = 0;
	for (let i = 0; i < prices.length; i++) {
		minp = Math.min(minp, prices[i]);
		maxp = Math.max(maxp, prices[i] - minp);
	}
	return maxp;
};

console.log(maxProfitShort([7, 1, 5, 3, 6, 4])); // 6-1 = 5
console.log(maxProfitShort([7, 6, 4, 3, 1])); // 0
console.log(maxProfitShort([2, 4, 1])); // 2

// When minn updates, update maxn too so that index(minn < maxn)
let maxProfit = function(prices) {
	if (prices.length === 0) return 0;

	let minn = prices[0],
		maxn = prices[0],
		mp = 0;
	for (let i = 1; i < prices.length; i++) {
		if (prices[i] < minn) {
			minn = prices[i];
			maxn = prices[i];
		} else if (prices[i] > maxn) {
			maxn = prices[i];
		}
		mp = Math.max(mp, maxn - minn);
	}

	return mp;
};

console.log(maxProfit([7, 1, 5, 3, 6, 4])); // 6-1 = 5
console.log(maxProfit([7, 6, 4, 3, 1])); // 0
console.log(maxProfit([2, 4, 1])); // 2
