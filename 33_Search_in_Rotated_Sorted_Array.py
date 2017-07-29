class Solution(object):
    """ 模板，画图. 33%. """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        start = 0; end = len(nums)-1
        while start+1 < end:
            mid = start+(end-start)/2
            if target == nums[mid]:
                return mid
            if nums[start] < nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if target == nums[start]:
            return start
        if target == nums[end]:
            return end
        return -1
        
