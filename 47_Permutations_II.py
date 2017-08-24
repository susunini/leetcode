class Solution(object):
    def helper(self, nums, permutation, result):
        if not nums:
            result.append(permutation[:])
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.helper(nums[:i]+nums[i+1:], permutation+[num], result)
            
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = list()
        self.helper(nums, [], result)
        return result
    
class Solution(object):
    """ 20170824. """
    def helper(self, nums, permutation, result):
        if not nums:
            result.append(permutation[:])
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.helper(nums[:i]+nums[i+1:], permutation+[num], result)
            
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = list()
        self.helper(nums, [], result)
        return result
        
