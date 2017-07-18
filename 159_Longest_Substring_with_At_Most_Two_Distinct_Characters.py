class Solution(object):
    """ Google. String. Sliding Window. Two Pointers. """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = dict()
        p1 = p2 = 0; res = 0
        while p2 < len(s):
            dic[s[p2]] = p2
            if len(dic) <= 2:
                p2 += 1
            else:
                res = max(res, p2-p1)
                min_index = min(dic.values())
                del dic[s[min_index]]
                p1 = min_index+1
        res = max(res, p2-p1)
        return res
