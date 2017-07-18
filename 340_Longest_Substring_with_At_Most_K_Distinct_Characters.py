class Solution(object):
    """ Google. String. Sliding Window. Two Pointer. 91%. """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0: return 0
        dic = dict()
        res = 0; p1 = p2 = 0
        while p2 < len(s):
            dic[s[p2]] = p2
            if len(dic) <= k:
                p2 += 1
            else:
                res = max(res, p2-p1)
                min_index = min(dic.values())
                del dic[s[min_index]]
                p1 = min_index+1
        res = max(res, p2-p1)
        return res
