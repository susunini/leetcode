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
