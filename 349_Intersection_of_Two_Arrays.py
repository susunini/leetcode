class Solution(object):
    """ Solution 1: Hash Table. """
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_dict = {num:True for num in nums1}
        return list(set([num for num in nums2 if num in nums1_dict]))
        
class Solution(object):
    """ Sort. """
    def intersection(self, nums1, nums2):
        nums1.sort(); nums2.sort()
        result = set()
        p1 = p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            num1 = nums1[p1]; num2 = nums2[p2]
            if num1 == num2:
                result.add(num1)
                p1 += 1; p2 += 1  # Miss
            elif num1 > num2:
                p2 += 1
            else:
                p1 += 1
        return list(result)
    
class Solution:
    """ Sort wo set. """
    def intersection(self, nums1, nums2):
        nums1.sort(); nums2.sort()
        p1 = p2 = 0
        result = list()
        while p1 < len(nums1) and p2 < len(nums2):
            while (p1+1) < len(nums1) and nums1[p1] == nums1[p1+1]:
                p1 += 1
            while (p2+1) < len(nums2) and nums2[p2] == nums2[p2+1]:
                p2 += 1
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1; p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return result
        
class Solution(object):
    """ Sort and Binary Search. """
    def intersection(self, nums1, nums2):
        pass
