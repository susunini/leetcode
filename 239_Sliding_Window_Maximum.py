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
    
class Solution(object):
    """ Deque. O(n). 71%.
    deque is a double linked list supporting O(1) pop and push from both ends. 
    deque 1. sotres indexes 
          2. monotonic decreasing queue (values)
          3. maxis always at head. 
    """
    def maxSlidingWindow(self, nums, k):
        d = collections.deque()
        out = []
        for i, num in enumerate(nums):
            while d and nums[d[-1]] < num:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out
