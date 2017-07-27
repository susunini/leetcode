class Solution(object):
    """ Binary Search. 43%. """
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: # corner case: []
            return [-1, -1]
        res = [-1, -1]
        s = 0; e = len(nums)-1
        while s+1 < e:
            mid = s+(e-s)/2
            if nums[mid] == target:
                e = mid
            elif nums[mid] < target:
                s = mid
            else:
                e = mid
        if nums[s] == target or nums[e] == target:
            res[0] = s if nums[s] == target else e
            
        s = 0; e = len(nums)-1
        while s+1 < e:
            mid = s+(e-s)/2
            if nums[mid] == target:
                s = mid
            elif nums[mid] < target:
                s = mid
            else:
                e = mid
        if nums[s] == target or nums[e] == target:
            res[1] = e if nums[e] == target else s
        return res
            
                
                
            
        
