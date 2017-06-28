"""
As a followup question, it naturally also requires maintaining a window of size k. When t == 0, it reduces to the previous question so we 
just reuse the solution.
Since there is now a constraint on the range of the values of the elements to be considered duplicates, it reminds us of doing a range 
check which is implemented in tree data structure and would take O(LogN) if a balanced tree structure is used, or doing a bucket check 
which is constant time. We shall just discuss the idea using bucket here.

Bucketing means we map a range of values to the a bucket. For example, if the bucket size is 3, we consider 0, 1, 2 all map to the same 
bucket. However, if t == 3, (0, 3) is a considered duplicates but does not map to the same bucket. This is fine since we are checking the 
buckets immediately before and after as well. So, as a rule of thumb, just make sure the size of the bucket is reasonable such that 
elements having the same bucket is immediately considered duplicates or duplicates must lie within adjacent buckets. So this actually 
gives us a range of possible bucket size, i.e. t and t + 1. We just choose it to be (t + 1) and a bucket mapping to be num / (t + 1). We
did not choose t because t might be zero.

Another complication is that negative ints are allowed. A simple num / t just shrinks everything towards 0. Therefore, we can just 
reposition every element to start from Integer.MIN_VALUE. (I did not implement this part)
"""

class Solution(object):
    """ Bucket Sort. 98%. """
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 or not nums: # Corner cases: 1. t == -1 2. nums = []
            return False
        d = {}
        w = t+1; min_num = min(nums)
        for i, num in enumerate(nums):
            if i > k:
                remove_idx =(nums[i-k-1]-min_num)/w 
                del d[remove_idx] # No need to worry about deleting numbers within current sliding window because would have return True
                                  # if there are duplicates within previous sliding window
            idx = (num-min_num)/w # Wrong for corner cases like num = -5: num/w 
            if idx in d:
                return True
            if (idx-1) in d and abs(num-d[idx-1]) <= t:
                return True
            if (idx+1) in d and abs(num-d[idx+1]) <= t:
                return True
            d[idx] = num
        return False
            
        
