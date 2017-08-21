class Solution:
    def binarySearch(self, nums, target):
        start = 0; end = len(nums)
        while start+1 < end:
            mid = start+(end-start)/2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
