class Solution(object):
    """ DP. 
    dp[i] - max profit given houses 0 to i
    dp[0] = nums[0]; dp[1] = max(nums[0], nums[1])
    dp[i] = max(dp[i-1], dp[i-2]+nums[i]"""
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        prev_prev = nums[0]
        prev = max(nums[0], nums[1])
        for num in nums[2:]:
            prev_prev, prev = prev, max(prev, prev_prev+num)
        return prev
