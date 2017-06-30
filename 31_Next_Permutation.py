class Solution(object):
    """ Wrong. """
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                nums[i:] = sorted(nums[i:])
                return
        nums.sort()
        
class Solution(object):
    """ Array. Permutation. 52ms(94%). """
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                for k in range(n-1, i-1, -1):
                    if nums[k] > nums[i-1]:
                         nums[k], nums[i-1] = nums[i-1], nums[k]  
                         nums[i:] = sorted(nums[i:]) # Wrong: nums[k:] = sorted(nums[k:])
                         return
        nums.sort()
