class Solution(object):
    """ Two Pointers. """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        r = w = 1
        while r < len(nums):
            if r == len(nums) - 1 or nums[r] != nums[r-1] or nums[r] != nums[r+1]:
                nums[w] = nums[r]
                w += 1
            r += 1
        
        return w
        
class Solution(object):
    """ Compare current num with the last two nums before tail. """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        tail = 2
        for num in nums[2:]:
            if num != nums[tail - 1] or num != nums[tail - 2]:
                nums[tail] = num
                tail += 1
        return tail
