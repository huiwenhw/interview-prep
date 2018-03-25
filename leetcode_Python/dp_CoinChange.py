'''
https://leetcode.com/problems/coin-change/description/
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.
'''

# use only one dp array
# for each amount, create a list of # coins needed to fulfil that amount
# take the min of that list and store it in dp[current amount]
# finally, dp[amount] will be number of coins needed 
# if its float('inf') value, it means that the coins were unable to add up to amount
def coinchange(coins, amount):
    maxn = float('inf')
    dp = [0] + [maxn] * amount

    for i in range(1, amount+1):
        dp[i] = min([dp[i-c] if i-c >= 0 else maxn for c in coins]) + 1
    return [dp[amount], -1][dp[amount] == maxn]
    # means: [falsevalue, truevalue][true condition]

def coinchange_ori(coins, amount):
    #dp = [[float('inf') for _ in range(amount+1)] for _ in range(len(coins)+1)]
    coins = [x for x in coins if x <= amount]
    if amount == 0: return 0
    if len(coins) == 0: return -1

    dp = [[float('inf') for _ in range(amount+1)] for _ in range(2)]
    mincoin = min(coins)-1

    for i in range(1, len(coins)+1):
        ir = i % 2 
        if amount < coins[i-1]:
            dp[ir] = dp[ir-1]
            continue
        for k in range(1, amount+1):
            if k == coins[i-1]:
                dp[ir][k] = 1
            elif k < coins[i-1]:
                dp[ir][k] = dp[ir-1][k]
            else:
                dp[ir][k] = min(dp[ir][k-coins[i-1]]+1, dp[ir-1][k])
    #print(dp)
    if dp[ir][amount] == float('inf'):
        return -1
    return dp[ir][amount]

print(coinchange([1,2,5], 11))
print(coinchange([1,3,4], 6))
print(coinchange([214783647], 2))
'''
print(coinchange([125,146,125,252,226,25,24,308,50], 8402))
print(coinchange([112,149,215,496,482,436,144,397,500,189], 8480))
print(coinchange([492,364,366,144,492,316,221,326,16,166,353], 5253))
print(coinchange([9,183,255,407,102,174,230], 627)) # 9
print(coinchange([84,457,478,309,350,349,422,469,100,432,188], 6993))
'''
