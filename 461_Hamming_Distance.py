class Solution(object):
    """ Wrong. """
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        while x or y:
            res += ((x & 1) ^ (y & 1))
            x >= 1; y >= 1
        return res

class Solution(object):
    """ Bit Manipulation. """
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        while x or y:
            res += ((x & 1) ^ (y & 1))
            x >>= 1; y >>= 1
        return res
        
        
class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')
            
            
            
            
