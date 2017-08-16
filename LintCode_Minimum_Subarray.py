class Solution:
    """ Maximum Subarray. 
    Test Cases: [-1,-1]=>-1 """
    def minSubArray(self, nums):
        """
        @param nums: a list of integers
        @return: A integer denote the sum of minimum subarray
        """
        if not nums:
            return 0
        for i in range(len(nums)):
            nums[i] = -nums[i]
        prev = result = nums[0]
        for i in range(1, len(nums)):
            prev = max(prev, 0) + nums[i]
            result = max(result, prev)
        return -result
        
class Solution:
    """ Wrong for test case [-1,-1] should return -1 instead of 0. """
    def minSubArray(self, nums):
        for i in range(len(nums)):
            nums[i] = -nums[i]
        prev = result = 0
        result = prev
        for i in range(len(nums)):
            prev = max(prev, 0) + nums[i]
            result = max(result, prev)
        return -result
        
class Solution:
    def minSubArray(self, nums):
        if not nums:
            return 0
        prev = result = -nums[0]
        for i in range(1, len(nums)):
            prev = max(prev, 0) - nums[i]
            result = max(result, prev)
        return -result
        
 class Solution:
    def minSubArray(self, nums):
        if not nums:
            return 0
        prev = result = nums[0]
        for i in range(1, len(nums)):
            prev = min(prev, 0) + nums[i]
            result = min(result, prev)
        return result
