class Solution(object):
    """
    0: corner cases: d == 0 n == 0
    1. sign
    2. integer part
    3. fractional part
    4. repeating numerator """
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        r_str = ""
        n = numerator; d = denominator
        if d == 0:
            return None
        if n == 0:
            return "0"
        if n * d < 0: 
            r_str += "-"
        n = abs(n); d = abs(d)
        r_str += str(n / d)
        if n % d == 0:
            return r_str
        r_str += "."
        n_to_idx = {}
        n = (n % d) * 10
        while n != 0:
            if n not in n_to_idx:
                r_str += str(n / d)
                n_to_idx[n] = len(r_str) - 1
                n = (n % d) * 10
            else:
                idx = n_to_idx[n]
                r_str = r_str[:idx] + "(" + r_str[idx:] + ")"
                break
        return r_str
        
class Solution(object):
    """ 99%.
    test cases: 1. 4/2 2. 1/2 3. -50/8 4. 1/3 5. 0.4(38)"""
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return ''
        sign = '' if numerator*denominator >= 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)
        div, mod = divmod(numerator, denominator)
        res = str(div)
        if mod == 0:
            return sign + res
        res += '.'
        dic = dict()
        while mod:
            if mod not in dic:
                dic[mod] = len(res)
                div, mod = divmod(mod*10, denominator)
                res += str(div)
            else:
                res = res[:dic[mod]] + '(' + res[dic[mod]:] + ')'
                break
        return sign + res
                
            
        
