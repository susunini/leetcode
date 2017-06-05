class Solution(object):
    """ Hash table. 589ms(92%). """
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        dic = dict()
        for i, w in enumerate(words):
            dic[w[::-1]] = i
        for i, w in enumerate(words):
            if '' in dic and dic[''] != i and self.isPalindrome(w):
                res.append([i, dic['']])
                res.append([dic[''], i])
            if w in dic and dic[w] != i:
                res.append([i, dic[w]])
            for j in range(1, len(w)):
                w1 = w[:j]; w2 = w[j:]
                if w1 in dic and dic[w1] != i and self.isPalindrome(w2):
                    res.append([i, dic[w1]])
                if w2 in dic and dic[w2] != i and self.isPalindrome(w1):
                    res.append([dic[w2], i])
        return res
        
    def isPalindrome(self, w):
        p1 = 0; p2 = len(w) - 1
        while p1 < p2:
            if w[p1] != w[p2]:
                return False
            p1 += 1; p2 -= 1
        return True
