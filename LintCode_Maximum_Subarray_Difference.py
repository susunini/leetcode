class Solution:
    """ Array. 四轮maximum subarray. """
    def maxDiffSubArrays(self, nums):
         """
         @param: nums: A list of integers
         @return: An integer indicate the value of maximum difference between two substrings
         """
        if len(nums) < 2:
            return None
        n = len(nums);
        dp1 = [0]*n; dp2 = [0]*n; dp3 = [0]*n; dp4 = [0]*n
        prev_max = prev_min = dp1[0] = dp2[0] = nums[0]
        for i in range(1, n):
            prev_max = max(0, prev_max) + nums[i]
            prev_min = min(0, prev_min) + nums[i]
            dp1[i] = max(dp1[i-1], prev_max)
            dp2[i] = min(dp2[i-1], prev_min)
        prev_max = prev_min = dp3[-1] = dp4[-1] = nums[-1] # Wrong
        for i in range(n-2, -1, -1):
            prev_max = max(0, prev_max) + nums[i]
            prev_min = min(0, prev_min) + nums[i]
            dp3[i] = max(dp3[i+1], prev_max)
            dp4[i] = min(dp4[i+1], prev_min)
        result = -sys.maxint-1
        for i in range(n-1):
            result = max([result, 
                          abs(dp1[i]-dp4[i+1]), 
                          abs(dp3[i+1]-dp2[i])])
        return result
