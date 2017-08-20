class Solution:
    """
    Subarray. DP. 
    """
    def maxTwoSubArrays(self, nums):
        """ 
        @param nums: A list of integers
        @return: An integer denotes the sum of max two non-overlapping subarrays
        
        dp1[i] - maximum subarray for nums[:i]
        dp2[i] - maximum subarray for nums[i:]
        """
        if len(nums) < 2:
            return None
        n = len(nums)
        dp1 = [0]*n; dp2 = [0]*n
        prev = nums[0]
        dp1[0] = nums[0]
        for i in range(1, n):
            prev = max(prev, 0) + nums[i]
            dp1[i] = max(dp1[i-1], prev)
        prev = nums[-1]
        dp2[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            prev = max(prev, 0) + nums[i]
            dp2[i] = max(dp2[i+1], prev)
        result = -sys.maxint-1
        for i in range(n-1):
            result = max(result, dp1[i]+dp2[i+1])
        return result
    
    
