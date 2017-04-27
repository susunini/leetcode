# Note:
# DP
# But there are several ways of writing the recursion function

# Solution 1
# buy[i], sell[i], cool[i] - the last transaction at day i is buy, sell or cooldown, respectively 
# p.s. there could be no transaction on day i
# sell[i] = max(sell[i-1], buy[i-1] + prices[i])
# buy[i] = cool[i-1] - prices[i])
# cool[i] = max(cool[i-1], sell[i-1])

# Some people intepret the problem as a state machine
# https://leetcode.com/discuss/72030/share-my-dp-solution-by-state-machine-thinking

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1: return 0
        
        buy = -prices[0]
        sell = cool = 0
        for i in range(1, len(prices)):
            buy_next = max(buy, cool - prices[i])
            sell_next = buy + prices[i]
            cool_next = max(cool, sell)
            buy, sell, cool = buy_next, sell_next, cool_next
        return max(buy, sell, cool) # or return max(sell, cool)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        sell = 0
        buy = -prices[0]
        cool = 0
        for price in prices[1:]:
            cur_sell = max(sell, buy + price)
            cur_buy = max(buy, cool - price)
            cur_cool = max(cool, sell)
            sell, buy, cool = cur_sell, cur_buy, cur_cool
        return max(sell, buy, cool)
    
