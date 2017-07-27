class Solution(object):
    """ Binary Search. """
    def helper(self, nums, target, start, end):
        mid = start+(end-start)/2
        if target == nums[mid]:
            return mid
        if (end-start) == 1:
            return end
        if target < nums[mid]:
            return self.helper(nums, target, start, mid)
        else:
            return self.helper(nums, target, mid, end)
        
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        return self.helper(nums, target, 0, len(nums)-1)
    
 class Solution(object):
    """ 84%. """
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0; end = len(nums)-1
        while start+1 < end:
            mid = start+(end-start)/2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                end = mid
            else:
                start = mid
        if target in [nums[start], nums[end]]:
            return start if target == nums[start] else end
        if target < nums[start]:
            return start
        if target > nums[end]:
            return end+1
        return end
