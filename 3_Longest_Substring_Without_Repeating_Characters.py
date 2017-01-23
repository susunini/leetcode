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
        li = [None] * 256
        for i, ch in enumerate(s):
            ch = ord(ch)
            if li[ch] is not None and li[ch] >= start:
                res = max(res, i - start)
                start = li[ch] + 1
            li[ch] = i
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
    
class Solution(object):
    """ Wrong. """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        start = 0
        li = [None] * 256
        for i, ch in enumerate(s):
            if li[ch] is not None and li[ch] > start:
                res = max(res, i - start)
                start = li[ch] + 1
            li[ch] = i
        res = max(res, len(s) - start)
        return res
            
        
