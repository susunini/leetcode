class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        r_num = nums[0]
        for num in nums[1:]:
            r_num ^= num
        return r_num
    
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res
