class Solution(object):
    """ Two Pointers. Hashtable. """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        start = 0
        d = {}
        for i, ch in enumerate(s):
            if ch in d and d[ch] >= start:
                res = max(res, i - start)
                start = d[ch] + 1
            d[ch] = i
        res = max(res, len(s) - start)
        return res
        
class Solution(object):
    """ Faster. Use list instead if dict. Confirm if all ASCII characters. """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        start = 0
        d = {}
        for i, ch in enumerate(s):
            if ch in d and d[ch] >= start:
                res = max(res, i - start)
                start = d[ch] + 1
            d[ch] = i
        res = max(res, len(s) - start)
        return res
        
class Solution(object):
    """ Wrong. """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        start = 0
        chs = [None] * 256
        for i, ch in enumerate(s):
            ch = ord(ch)
            if chs[ch] is not None and chs[ch] >= start:
                res = max(res, i - start)
                start = chs[ch] + 1
            chs[ch] = i
        return res
        
class Solution(object):
    """ Wrong. """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        start = 0
        d = {}
        for ch, i in enumerate(s):
            if ch in d and d[ch] >= start:
                res = max(res, i - start)
                print ch, res
                start = d[ch] + 1
            d[ch] = i
        res = max(res, len(s) - start)
        return res
