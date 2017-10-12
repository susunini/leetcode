""" Find First Prefix-Match From a Sorted String Array.
"""


class Solution(object):
    def search_first(self, prefix, words):
        """ Search the first prefix from a list of words. """
        if not words:
            return -1
        start = 0; end = len(words)-1
        while start+1 < end:
            mid = end + (start - end) / 2
            compare_result = self.compare(prefix, words[mid])
            if compare_result == 0:
                end = mid # Wrong: return words[mid]
            if compare_result > 0:
                start = mid
            else:
                end = mid
        if self.compare(prefix, words[start]) == 0:
            return words[start]
        if self.compare(prefix, words[end]) == 0:
            return words[end]
        return -1
    
    def compare(self, prefix, word):
        """ Compare prefix with word.
        :return int: 0 if prefix is a prefix or word
                     1 if prefix is lexically larger than word
                     -1 otherwise (if prefix is lexically smaller than word)
        """
        m = len(prefix); n = len(word)
        i = 0
        while i < min(m,n):
            if prefix[i] == word[i]:
                i += 1
            else:
                break
        if m <= n:
            if i == m:
                return 0
            return 1 if prefix[i] > word[i] else -1
        else:
            if i == n:
                return 1
            return 1 if prefix[i] > word[i] else -1

words = ['Ann', 'App', 'Apple', 'Boy']
assert(Solution().search_first('Ap', words) == 'App')
assert(Solution().search_first('C', words) == -1)
assert(Solution().search_first('B', words) == 'Boy')
assert(Solution().search_first('B', []) == -1)
assert(Solution().search_first('', words) == 'Ann')
