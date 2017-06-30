class Solution(object):
    """ O(nlogn). 44ms(91%). """
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: 
            return None
        return sorted(nums)[::-1][k-1]
        
class Solution(object):
    """ Heap. O(n+klogn). 106ms(45%). """
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = None
        nums = [-num for num in nums] # Wrong: nums = [num for num in nums]
        heapq.heapify(nums)
        for _ in range(k):
            res = heapq.heappop(nums) 
        return -res # Wrong: return res
        
class Solution(object):
    """ Heap. O(k+(n-k)logk). 115ms(42%).
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]: # Wrong: for num in nums
            heapq.heappush(heap, num) # Wrong: pop before push
            heapq.heappop(heap)
        return heap[0]
        
        
