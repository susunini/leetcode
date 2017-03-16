class Solution(object):
    def decimal_to_base(self, num, base):
         res = ''
         d = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
         while num:
             num, mod = divmod(num, base)
             res = str(mod) + res if mod < 10 else d[mod] + res
         return res
         
    def base_to_decimal(self, str, base):
         pass
         
print Solution().decimal_to_base(282, 16)
print Solution().decimal_to_base(241, 16)
print Solution().decimal_to_base(1234567, 16)
print Solution().decimal_to_base(282, 10)
print Solution().decimal_to_base(241, 10)
print Solution().decimal_to_base(1234567, 10)
