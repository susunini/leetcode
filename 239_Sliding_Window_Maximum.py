class Solution(object):
    """ Heap. O(nlogn). """
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)
        result = [-heap[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while i-heap[0][1] >= k:
                heapq.heappop(heap)
            result.append(-heap[0][0])
        return result
