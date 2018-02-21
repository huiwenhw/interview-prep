/*
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/ 
 *
 * Array: ith element is the price of a given stock on day i.
 * Find max profit, can buy/sell stock multiple times. 
 */

// Add to max profit when curr stock price > previous day
let maxProfit = prices => {
	if (!prices.length) return 0;

	let maxp = 0;
	for (let i = 1; i < prices.length; i++) {
		if (prices[i] > prices[i - 1]) {
			maxp += prices[i] - prices[i - 1];
		}
		// or, maxp += Math.max(0, prices[i] - prices[i-1])
	}
	return maxp;
};

console.log(maxProfit([1, 2, 3])); // 2
console.log(maxProfit([2, 4, 3, 1])); // 2
