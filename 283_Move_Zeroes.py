class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        w = 0
        for r, num in enumerate(nums):
            if num is not 0:
                nums[w] = nums[r]
                w += 1
        for i in range(w, len(nums)):
            nums[i] = 0
            
