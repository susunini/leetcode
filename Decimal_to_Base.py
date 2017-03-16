class Solution(object):
    """ Google. """
    def decimal_to_base(self, num, base):
        res = ''
        d = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        while num:
            num, mod = divmod(num, base)
            res = str(mod) + res if mod < 10 else d[mod] + res
        return res
         
    def base_to_decimal(self, s, base):
        res = 0
        d = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        for ch in s:
            try:
                res = res*base+int(ch)
            except ValueError:
                res = res*base+d[ch]
        return res
        
        
         
print Solution().decimal_to_base(282, 16)
print Solution().decimal_to_base(1234567, 16)
print Solution().decimal_to_base(282, 10)
print Solution().decimal_to_base(1234567, 10)
print Solution().base_to_decimal('11A', 16)
print Solution().base_to_decimal('1234567', 10)
