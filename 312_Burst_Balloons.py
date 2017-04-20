class Solution(object):
    """ 3-D DP. O(n^3)
    
    dp[left][right] - maxium value of having nums[left] and nums[right] as left and right borders (will not be burst)
    dp[left][right] = max(dp[left][k] + nums[left]*nums[k]*nums[right] +dp[k][right]) 
    where k from left+1 to right-1 (burst k last)
    
    The order of traversal is by diagonal.
    For example, for a matrix n = 6, the order of traversal is
    (0,0), (1,1), (2,2), (3,3), (4,4), (5,5) diff = 0 (for this problem, don't need to traverse this diagonal)
    (0,1), (1,2), (2,3), (3,4), (4,5) diff = 1 (no need)
    (0,2), (1,3), (2,4), (3,5) diff = 2
    (0,3), (1,4), (2,5) diff = 3
    (0,4), (1,5) diff = 4
    (0,5) diff = 5
    """
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)
        dp = [[0]*n for _ in xrange(n)]
        
        for diff in range(2, n):
            for left in xrange(0, n-diff):
                right = left + diff
                for i in xrange(left+1, right):
                    dp[left][right] = max(dp[left][right], 
                                          dp[left][i] + nums[left]*nums[i]*nums[right] + dp[i][right])
                print left, right
        print dp
        return dp[0][n-1]
