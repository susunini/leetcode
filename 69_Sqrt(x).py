class Solution(object):
    """ Binary Search. """
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        s = 1; e = x
        while (e-s) > 1:
            m = (s+e)/2
            if m*m == x:
                return m
            if m*m < x:
                s = m
            else:
                e = m
        return e if e*e < x else s
