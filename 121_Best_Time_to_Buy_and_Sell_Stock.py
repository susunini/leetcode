class Solution(object):
    """ Wrong. """
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
