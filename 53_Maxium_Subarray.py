class Solution(object):
    """ Dynamic Programming. 
    
    dp[i] - length of maxinum subarray ending at nums[i]
    dp[i] = max(nums[i], dp[i-1] + nums[i])
    return max(dp)
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = nums[0]
        res = nums[0]
        for num in nums[1:]:
            dp = max(num, num + dp)
            res = max(res, dp)
        return res
    
class Solution:
    """ 20170819. """
    def maxSubArray(self, nums):
        prev = 0; result = -sys.maxint-1
        for num in nums:
            prev = max(prev,0)+num
            result = max(result, prev)
        return result
    
            
            
            
