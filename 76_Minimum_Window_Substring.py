class Solution(object):
    """ Wrong. """
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)
        miss = len(t)
        start = 0
        min_start = -1; min_end = len(s)
        for i, ch in enumerate(s):
            if need[ch] > 0:
                miss -= 1
            need[ch] -= 1
            if miss > 0:
                continue
            while need[start] < 0:
                start += 1
            if (i-start) < (min_end-min_start):
                min_end, min_start = i, start
        return s[min_start:min_end+1] if min_start != -1 else ''
        
class Solution(object):
    """ Wrong. """
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)
        miss = len(t)
        start = 0
        min_start = -1; min_end = len(s)
        for i, ch in enumerate(s):
            if need[ch] > 0:
                miss -= 1
            need[ch] -= 1
            if miss > 0:
                continue
            while start <= i and need[start] < 0:
                start += 1
            if (i-start) < (min_end-min_start):
                min_end, min_start = i, start
        return s[min_start:min_end+1] if min_start != -1 else ''
        
class Solution(object):
    """ Wrong. """
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)
        miss = len(t)
        start = 0
        min_start = -1; min_end = len(s)
        for i, ch in enumerate(s):
            if need[ch] > 0:
                miss -= 1
            need[ch] -= 1
            if miss > 0:
                continue
            while start <= i and need[s[start]] < 0:
                start += 1
            if (i-start) < (min_end-min_start):
                min_end, min_start = i, start
        return s[min_start:min_end+1] if min_start != -1 else ''
        
class Solution(object):
    """ Two Pointers. """
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)
        miss = len(t)
        start = 0
        min_start = -1; min_end = len(s)
        for i, ch in enumerate(s):
            if need[ch] > 0:
                miss -= 1
            need[ch] -= 1
            if miss > 0:
                continue
            while start <= i and need[s[start]] < 0:
                need[s[start]] += 1
                start += 1
            if (i-start) < (min_end-min_start):
                min_end, min_start = i, start
        return s[min_start:min_end+1] if min_start != -1 else ''
