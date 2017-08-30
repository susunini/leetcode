class Solution(object):
    """ DP. O(n^2). """
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0]*len(nums)
        result = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                dp[i] = max(dp[i], dp[j]+1)
            result = max(result, dp[i])
        return result

        
