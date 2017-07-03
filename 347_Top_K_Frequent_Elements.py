class Solution(object):
    """ Heap. Time O(n+klogn). Space O(n). """
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = collections.defaultdict(int)
        for num in nums:
            dic[num] += 1
        h = [[-val, key] for key, val in dic.items()]
        heapq.heapify(h)
        return [heapq.heappop(h)[1] for _ in range(k)]
        
class Solution(object):
    """ Heap. """
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = collections.defaultdict(int)
        for num in nums:
            dic[num] += 1
        h = [[val, key] for key, val in dic.items()]
        return [key for val, key in heapq.nlargest(k, h)]
    
class Solution(object):
    """ Bucket Sort. """
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        dic = collections.defaultdict(int) # Or: dic = collections.Counter(nums)
        for num in nums:
            dic[num] += 1
        
        max_freq = max([value for _, value in dic.items()])   
        buckets = [[] for i in range(max_freq + 1)]
        for num, cnt in dic.items():
            buckets[cnt].append(num)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if len(res) == k:
                return res
            if buckets[i]:
                res.extend(buckets[i])

class Solution(object):
    """ One-liner python """
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Use Counter to extract the top k frequent elements
        # most_common(k) return a list of tuples, where the first item of the tuple is the element,
        # and the second item of the tuple is the count
        # Thus, the built-in zip function could be used to extract the first item from the tuples
        return zip(*collections.Counter(nums).most_common(k))[0]
