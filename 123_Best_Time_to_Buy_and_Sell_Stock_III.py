class Solution:
    """ Same Problem: LintCode_Maximum_Subarray_II.py
    def maxProfit(self, prices):
        """
        @param prices: Given an integer array
        @return: Maximum profit
        """
        if not prices:
            return 0
        n = len(prices)
        maxLeftToRight = [0]*n
        maxRightToLeft = [0]*n
        minPrice = prices[0]
        for i in range(1, n):
            maxLeftToRight[i] = max(maxLeftToRight[i-1], prices[i]-minPrice)
            minPrice = min(minPrice, prices[i])
        maxPrice = prices[-1]
        for i in range(n-2, -1, -1):
            maxRightToLeft[i] = max(maxRightToLeft[i+1], maxPrice-prices[i])
            maxPrice = max(maxPrice, prices[i])
        print maxLeftToRight, maxRightToLeft
        result = max(maxLeftToRight[-1], maxRightToLeft[0]) # only one transaction
        for i in range(n-1):
            result = max(result, maxLeftToRight[i]+maxRightToLeft[i+1])
        # same as
        for i in range(n):
            result = max(result, maxLeftToRight[i]+maxRightToLeft[i])
        return result
