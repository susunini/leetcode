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
    """ Binary Search. 98%. """
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
