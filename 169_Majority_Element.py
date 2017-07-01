class Solution(object):
    """ Hash Table. Time O(n) Space O(n)"""
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dic = collections.Counter(nums)
        for key, val in dic.items():
            if val > n/2:
                return key
   
class Solution(object):
    """ Kth Largest Element. """
    def findKthLargest(self, nums, k):
        """
        Divide and Conquer (Quick Select). Best Case O(n) Worst Case O(n^2) Average Case O(n)
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(nums):
            return None
        if k == 1:
            return max(nums)
        if len(nums) == k:
            return min(nums)
        pivot = nums[0]
        left = [num for num in nums if num < pivot]  
        equal = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        if len(right) >= k:
            return self.findKthLargest(right, k)
        elif len(right)+len(equal) >= k:
            return pivot
        else:
            return self.findKthLargest(left, k-len(right)-len(equal))  
        
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.findKthLargest(nums, len(nums)/2+1)
        
class Solution(object):
    """ Moore's Voting. Time O(n) Space O(1). """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]; cnt = 1
        for num in nums[1:]:
            if num == res:
                cnt += 1
            elif cnt > 1:
                cnt -= 1
            else:
                res = num; cnt = 1
        return res
