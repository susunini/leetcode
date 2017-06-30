class Solution(object):
    """ 201606. Binary Search. Bit Manipulation. 
    Corner Cases. Integer Overflow.
    """
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        a = dividend; b = divisor
        if a == (-2**31) and b == -1:
            return 2 ** 31 - 1
        if b == 0:
            return None
        if a == 0:
            return 0
        if (a > 0 and b < 0) or (a < 0 and b > 0):
            sign = -1
        else:
            sign = 1
        a = long(abs(a)); b = long(abs(b)) # why long?
        r_int = 0
        while a >= b:
            cnt = 0
            while a >= (b << cnt):
                cnt += 1
            cnt -= 1
            a -= (b << cnt)
            r_int += (1 << cnt)
        return sign * r_int
        
class Solution(object):
    """ Wrong. """
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1 if dividend*divisor >= 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            while dividend >= (divisor<<res):
                res += 1
            res -= 1
            dividend -= (divisor<<res)
            
        return sign*(1<<res)
        
class Solution(object):
    """ Binary Search. 98%. 
    Integer Overflow."""
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == (-2**31) and divisor == -1:
            return 2**31-1
        sign = 1 if dividend*divisor >= 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)
        li = []
        while dividend >= divisor:
            cnt = 0
            while dividend >= (divisor<<cnt):
                cnt += 1
            cnt -= 1
            dividend -= (divisor<<cnt)
            li.append(cnt)
            
        return sign*sum([1<<cnt for cnt in li])
