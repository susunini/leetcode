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
    """
    If a <= b <= c <= d, maxProfit = d - a =  (b - a) + (c - b) + …
    If a <= b > c <= d maxProfit = (b - a) + (d - a). 
    We can focus on finding monotone sequence.
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i-1])
        return res
