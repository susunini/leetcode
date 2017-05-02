class Solution(object):
    """ Wrong"""
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num+1)
        for i in range(1, num+1):
            res[i] = res[i>>1] + (i&1)
        return res
    
# Solution 1: My solution beats 26%
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        r_ints = [0] * (num + 1)
        for i in range(len(r_ints)):
            r_ints[i] = r_ints[i >> 1] + (i & 1)
        return r_ints
     
# Solution 2:
# i&(i-1) drops the lowest one bit of i
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        r_ints = [0] * (1 + num)
        for i in range(1, len(r_ints)):
            r_ints[i] = r_ints[i&(i-1)] + 1
        return r_ints
