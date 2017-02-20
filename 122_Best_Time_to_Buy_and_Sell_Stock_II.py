class Solution(object):   
    """ Wrong. """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = prices[0]
        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i-1])
        return res
        
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i-1])
        return res
