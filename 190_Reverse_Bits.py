class Solution:
    """ Wrong. """
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        while n:
            res = res << 1 + n & 1
            n = n >> 1
        return res
        
class Solution:
    """ Bit Manipulation. """
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n = n >> 1
        return res
