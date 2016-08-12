class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1: 
            return None
        r_max = max_i = min_i = nums[0]
        for i in range(1, len(nums)):
            nex_max_i = max(nums[i], max_i * nums[i], min_i * nums[i])
            nex_min_i = min(nums[i], max_i * nums[i], min_i * nums[i])
            max_i, min_i = nex_max_i, nex_min_i
            r_max = max(r_max, max_i)
        return r_max
