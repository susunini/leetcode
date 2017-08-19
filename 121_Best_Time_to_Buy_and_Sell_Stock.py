class Solution(object):
    """ Dynamic Programming. 
    
    dp[i]: maximum profit if selling at price i
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_price = prices[0]
        res = 0
        for price in prices[1:]:
            res = max(res, price-min_price)
            min_price = min(min_price, price)
        return res
    
class Solution(object):
    """ A variation of the orginal problem.
    
    if the interviewer twists the question slightly by giving the difference array of prices, Ex: for {1, 7, 4, 11}, 
    if he gives {0, 6, -3, 7}, the problem is same as 53 Maxium Subarray. """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        diffs = [0] * len(prices)
        for i in range(1, len(diffs)):
            diffs[i] = prices[i]-prices[i-1]
        dp = 0
        res = 0
        for diff in diffs[1:]:
            dp = max(0, dp) + diff
            res = max(res, dp)
        return res
    
  class Solution:
    """ 20170817. """
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        n = len(prices)
        diffs = [prices[i+1]-prices[i] for i in range(n-1)]
        result = 0; prev = 0
        for diff in diffs:
            prev = max(0, prev)+diff
            result = max(result, prev)
        return result
