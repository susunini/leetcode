class Solution(object):
    """ wrong """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        w = 1; r = 1
        while r < len(nums):
            if nums[r] != nums[r-1]:
                nums[w] = nums[r]
                w += 1
            r += 1
        return (w - 1)
                
class Solution(object):
    """ wrong """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        w = 1; r = 1
        while r < len(nums):
            if nums[r] != nums[r-1]:
                nums[w] = nums[r]
                w += 1
            r += 1
        return w
        
class Solution(object):
    """ Two pointers. """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        w = 1; r = 1
        while r < len(nums):
            if nums[r] != nums[r-1]:
                nums[w] = nums[r]
                w += 1
            r += 1
        return w
