class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not amount:
            return 0
        dp = [0]+[-1]*amount
        for i in range(1, amount+1):
            li = [dp[i-c] for c in coins if i-c >= 0 and dp[i-c] >= 0]
            dp[i] = min(li) + 1 if li else -1
        return dp[amount]
    
 class Solution(object):
    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in xrange(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins if i-c >= 0]) + 1

        return [dp[amount], -1][dp[amount] == MAX]
