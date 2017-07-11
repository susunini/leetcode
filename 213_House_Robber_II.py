class Solution(object):
    def _rob(self, nums):
        prev_prev = prev = 0
        for num in nums:
            prev_prev, prev = prev, max(prev, prev_prev+num)
        return prev
    
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self._rob(nums[:n-1]), 
                   self._rob(nums[1:]))
