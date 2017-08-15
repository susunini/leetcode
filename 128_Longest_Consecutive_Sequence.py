class Solution(object):
    """ O(n) solution
    We will use HashMap. The key thing is to keep track of the sequence length and store that in the boundary points of the sequence. 
    For example, as a result, for sequence {1, 2, 3, 4, 5}, map.get(1) and map.get(5) should both return 5.
    Whenever a new element n is inserted into the map, do two things:
    See if n - 1 and n + 1 exist in the map, and if so, it means there is an existing sequence next to n. Variables left and right will be 
    the length of those two sequences, while 0 means there is no sequence and n will be the boundary point later. Store (left + right + 1) 
    as the associated value to key n into the map.Use left and right to locate the other end of the sequences to the left and right of n 
    respectively, and replace the value with the new length.
    Everything inside the for loop is O(1) so the total time is O(n). 
    """
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        num_to_len = {}
        for num in nums:
            if num in num_to_len:
                continue
            else:
                left_len = num_to_len.get(num - 1, 0)
                right_len = num_to_len.get(num + 1, 0)
                sum_len = left_len + 1 + right_len
                num_to_len[num] = num_to_len[num - left_len] = num_to_len[num + right_len] = sum_len
                res = max(res, sum_len)
        return res
    
class Solution(object):
        """ Refactor to help understanding. Only update border elements. """
        def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        num_to_len = {}
        for num in nums:
            if num in num_to_len:
                continue
            left_len = num_to_len.get(num-1, 0)
            right_len = num_to_len.get(num+1, 0)
            num_to_len[num] = 1
            num_to_len[num-left_len] = num_to_len[num+right_len] = left_len+1+right_len
            result = max(result, sum_len)
        return res
