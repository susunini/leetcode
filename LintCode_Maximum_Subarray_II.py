class Solution:
    """
    Subarray. DP. 
    """
    def maxTwoSubArrays(self, nums):
        """ 
        @param nums: A list of integers
        @return: An integer denotes the sum of max two non-overlapping subarrays
        """
        n = len(nums)
        maxLeftToRight = [0]*n
        maxRightToLeft = [0]*n
        maxLeftToRight[0] = nums[0]
        for i in range(1, n):
            maxLeftToRight[i] = max(0, maxLeftToRight[i-1]) + nums[i]
        for i in range(1, n):
            maxLeftToRight[i] = max(maxLeftToRight[i-1], maxLeftToRight[i])
        maxRightToLeft[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            maxRightToLeft[i] = max(0, maxRightToLeft[i+1]) + nums[i]
        for i in range(n-2, -1, -1):
            maxRightToLeft[i] = max(maxRightToLeft[i+1], maxRightToLeft[i])
        result = 0
        for i in range(n-1):
            result = max(result, maxLeftToRight[i]+maxRightToLeft[i+1])
        return result
