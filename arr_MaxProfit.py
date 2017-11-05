'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Examples:
Input: [7, 1, 5, 3, 6, 4]
Output: 5
max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Input: [7, 6, 4, 3, 1]
Output: 0
In this case, no transaction is done, i.e. max profit = 0.
'''

import sys 

def max_profit(prices):
    length = len(prices)
    if length <= 1: return 0

    minp = prices[0]
    maxp = 0 
    diff = 0
    for i in range(length):
        if prices[i] < minp: 
            minp = prices[i]
        else: 
            curr_diff = prices[i] - minp
            if curr_diff > diff:
                diff = curr_diff
                maxp = prices[i]
    return diff

def max_profit_short(prices):
    maxp, minp = 0, float('inf')
    for price in prices:
        minp = min(minp, price)
        profit = price - minp
        maxp = max(maxp, profit) 
    return maxp 

def main():
    args = sys.argv[1:]
    prices = [int(i) for i in args[0].split(",")]
    print max_profit(prices)
    print max_profit_short(prices)

if __name__ == '__main__':
    main()
