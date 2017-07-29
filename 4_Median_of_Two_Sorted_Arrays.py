class Solution(object):
    """ Binary Search. """
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1); n = len(nums2)
        if (m+n)%2:
            return self.findKthElement(nums1, nums2, (m+n)/2+1)
        else:
            return (self.findKthElement(nums1, nums2, (m+n)/2) + self.findKthElement(nums1, nums2, (m+n)/2+1))/2.0
        
    def findKthElement(self, nums1, nums2, k):
        if not nums1:
            return nums2[k-1]
        if not nums2:
            return nums1[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        
        key1 = nums1[k/2-1] if k/2-1 < len(nums1) else sys.maxint
        key2 = nums2[k/2-1] if k/2-1 < len(nums2) else sys.maxint
        if key1 < key2:
            return self.findKthElement(nums1[k/2:], nums2, k-k/2)
        else:
            return self.findKthElement(nums1, nums2[k/2:], k-k/2)
